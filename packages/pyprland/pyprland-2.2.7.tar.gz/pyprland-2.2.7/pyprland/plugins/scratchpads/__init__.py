" Scratchpads addon "
import time
import asyncio
from functools import partial

from ...ipc import notify_error, get_client_props, get_focused_monitor_props
from ..interface import Plugin
from ...common import state, CastBoolMixin, apply_variables
from ...adapters.units import convert_coords, convert_monitor_dimension

from .animations import Animations
from .objects import Scratch
from .lookup import ScratchDB
from .helpers import (
    get_active_space_identifier,
    get_all_space_identifiers,
    get_match_fn,
)

AFTER_SHOW_INHIBITION = 0.3  # 300ms of ignorance after a show
DEFAULT_MARGIN = 60  # in pixels
DEFAULT_HIDE_DELAY = 0.2
DEFAULT_HYSTERESIS = 0.4  # In seconds


class Extension(CastBoolMixin, Plugin):  # pylint: disable=missing-class-docstring {{{
    procs: dict[str, asyncio.subprocess.Process] = {}  # pylint: disable=no-member
    scratches = ScratchDB()

    focused_window_tracking: dict[str, str] = {}

    workspace = ""  # Currently active workspace
    monitor = ""  # Currently active monitor

    _hysteresis_tasks: dict[str, asyncio.Task]  # non-blocking tasks

    def __init__(self, name):
        super().__init__(name)
        self._hysteresis_tasks = {}
        self.get_client_props = partial(get_client_props, logger=self.log)
        Scratch.get_client_props = self.get_client_props
        self.get_focused_monitor_props = partial(
            get_focused_monitor_props, logger=self.log
        )

    async def exit(self) -> None:
        "exit hook"

        async def die_in_piece(scratch: Scratch):
            if scratch.uid in self.procs:
                proc = self.procs[scratch.uid]
                proc.terminate()
                for _ in range(10):
                    if not await scratch.isAlive():
                        break
                    await asyncio.sleep(0.1)
                if await scratch.isAlive():
                    proc.kill()
                await proc.wait()

        await asyncio.gather(
            *(die_in_piece(scratch) for scratch in self.scratches.values())
        )

    async def on_reload(self) -> None:
        "config loader"
        # Create new scratches with fresh config items
        scratches = {
            name: Scratch(name, options) for name, options in self.config.items()
        }

        scratches_to_spawn = set()
        for name in scratches:
            scratch = self.scratches.get(name)
            if scratch:  # if existing scratch exists, overrides the conf object
                scratch.set_config(scratches[name].conf)
            else:
                # else register it
                self.scratches.register(scratches[name], name)
                is_lazy = self.cast_bool(scratches[name].conf.get("lazy"), False)
                if not is_lazy:
                    scratches_to_spawn.add(name)

        for name in scratches_to_spawn:
            if await self.ensure_alive(name):
                scratch = self.scratches.get(name)
                assert scratch
                scratch.meta["should_hide"] = True
            else:
                self.log.error("Failure starting %s", name)

        for scratch in list(self.scratches.getByState("configured")):
            assert scratch
            self.scratches.clearState(scratch, "configured")

    async def _configure_windowrules(self, scratch):
        "Setting up initial client window state (sets windowrules)"
        configured = self.scratches.hasState(scratch, "configured")
        if configured:
            return
        self.scratches.setState(scratch, "configured")
        animation_type: str = scratch.conf.get("animation", "fromTop").lower()
        defined_class: str = scratch.conf.get("class", "")
        if defined_class:
            monitor = await self.get_focused_monitor_props(
                name=scratch.conf.get("force_monitor")
            )
            width, height = convert_coords(scratch.conf.get("size", "80% 80%"), monitor)

            ipc_commands = [
                f"windowrule float,^({defined_class})$",
                f"windowrule workspace special:scratch_{scratch.uid} silent,^({defined_class})$",
            ]

            if animation_type:
                margin_x = (monitor["width"] - width) // 2
                margin_y = (monitor["height"] - height) // 2

                t_pos = {
                    "fromtop": f"{margin_x} -200%",
                    "frombottom": f"{margin_x} 200%",
                    "fromright": f"200% {margin_y}",
                    "fromleft": f"-200% {margin_y}",
                }[animation_type]
                ipc_commands.append(f"windowrule move {t_pos},^({defined_class})$")

            ipc_commands.append(f"windowrule size {width} {height},^({defined_class})$")

            await self.hyprctl(ipc_commands, "keyword")

    async def __wait_for_client(self, item, use_proc=True) -> bool:
        """Waits for a client to be up and running
        if `match_by=` is used, will use the match criteria, else the process's PID will be used.
        """
        self.log.info("==> Wait for %s spawning", item.uid)
        interval_range = [0.1] * 10 + [0.2] * 20 + [0.5] * 15
        for interval in interval_range:
            await asyncio.sleep(interval)
            is_alive = await item.isAlive()

            # skips the checks if the process isn't started (just wait)
            if is_alive or not use_proc:
                match_by = item.conf.get("match_by", "pid")
                if match_by != "pid":
                    info = await self.get_client_props(
                        match_fn=get_match_fn(match_by, item.conf[match_by]),
                        **{match_by: item.conf[match_by]},
                    )
                else:
                    info = await self.get_client_props(pid=item.pid)
                if info:
                    await item.updateClientInfo(info)
                    self.log.info(
                        "=> %s client (proc:%s, addr:%s) detected on time",
                        item.uid,
                        item.pid,
                        item.full_address,
                    )
                    self.scratches.register(item)
                    self.scratches.clearState(item, "respawned")
                    return True
            if use_proc and not is_alive:
                return False
        return False

    async def _start_scratch_nopid(self, item) -> bool:
        "Ensure alive, PWA version"
        uid = item.uid
        started = "nopid" in item.meta
        if not await item.isAlive():
            started = False
        if not started:
            self.scratches.reset(item)
            await self.start_scratch_command(uid)
            r = await self.__wait_for_client(item, use_proc=False)
            item.meta["nopid"] = r
            return r
        return True

    async def _start_scratch(self, item):
        "Ensure alive, standard version"
        uid = item.uid
        if uid in self.procs:
            try:
                self.procs[uid].kill()
            except ProcessLookupError:
                pass
        self.scratches.reset(item)
        await self.start_scratch_command(uid)
        self.log.info("starting %s", uid)
        if not await self.__wait_for_client(item):
            self.log.error("⚠ Failed spawning %s as proc %s", uid, item.pid)
            if await item.isAlive():
                error = "The command didn't open a window"
            else:
                await self.procs[uid].communicate()
                code = self.procs[uid].returncode
                if code:
                    error = f"The command failed with code {code}"
                else:
                    error = "The command terminated sucessfully, is it already running?"
            self.log.error('"%s": %s', item.conf["command"], error)
            await notify_error(error)
            return False
        return True

    async def ensure_alive(self, uid):
        """Ensure the scratchpad is started
        Returns true if started
        """
        item = self.scratches.get(name=uid)
        await self._configure_windowrules(item)
        assert item

        if self.cast_bool(item.conf.get("process_tracking"), True):
            if not await item.isAlive():
                self.log.info("%s is not running, starting...", uid)
                if not await self._start_scratch(item):
                    await notify_error(f'Failed to show scratch "{item.uid}"')
                    return False
            return True

        return await self._start_scratch_nopid(item)

    async def start_scratch_command(self, name: str) -> None:
        "spawns a given scratchpad's process"
        scratch = self.scratches.get(name)
        assert scratch
        self.scratches.setState(scratch, "respawned")
        old_pid = self.procs[name].pid if name in self.procs else 0
        command = apply_variables(scratch.conf["command"], state.variables)
        proc = await asyncio.create_subprocess_shell(command)
        self.procs[name] = proc
        pid = proc.pid
        scratch.reset(pid)
        self.scratches.register(scratch, pid=pid)
        self.log.info(
            "scratch %s (%s) has pid %s", scratch.uid, scratch.conf.get("command"), pid
        )
        if old_pid:
            self.scratches.clear(pid=old_pid)

    async def updateScratchInfo(self, orig_scratch: Scratch | None = None) -> None:
        """Update every scratchpads information if no `scratch` given,
        else update a specific scratchpad info"""
        pid = orig_scratch.pid if orig_scratch else None
        for client in await self.hyprctlJSON("clients"):
            assert isinstance(client, dict)
            if pid and pid != client["pid"]:
                continue
            # if no address registered, register it
            # + update client info in any case
            scratch = self.scratches.get(addr=client["address"][2:])
            if not scratch and client["pid"]:
                scratch = self.scratches.get(pid=client["pid"])
            if scratch:
                self.scratches.register(scratch, addr=client["address"][2:])
                await scratch.updateClientInfo(client)
                break
        else:
            self.log.info("Didn't update scratch info %s", self)

    # Events {{{
    async def event_monitorremoved(self, monitor_name) -> None:
        "Hides scratchpads on the removed screen"
        for scratch in self.scratches.values():
            if scratch.monitor == monitor_name:
                await self.run_hide(scratch.uid, autohide=True)

    async def event_configreloaded(self, _nothing):
        "Re-apply windowrules when hyprland is restarted"
        for scratch in list(self.scratches.getByState("configured")):
            self.scratches.clearState(scratch, "configured")
            await self._configure_windowrules(scratch)

    async def event_activewindowv2(self, addr) -> None:
        "active windows hook"
        for uid, scratch in self.scratches.items():
            if not scratch.client_info:
                continue
            if scratch.address == addr:
                self.cancel_task(uid)
            else:
                if scratch.visible and scratch.conf.get("unfocus") == "hide":
                    last_shown = scratch.meta.get("last_shown", 0)
                    if last_shown + AFTER_SHOW_INHIBITION > time.time():
                        self.log.debug(
                            "(SKIPPED) hide %s because another client is active",
                            uid,
                        )
                        continue

                    hysteresis = scratch.conf.get("hysteresis", DEFAULT_HYSTERESIS)
                    if hysteresis:
                        self.cancel_task(uid)

                        async def _task(scratch, delay):
                            await asyncio.sleep(delay)
                            if state.active_window == scratch.full_address:
                                self.log.debug(
                                    "Skipped hidding %s because client got the focus back",
                                    scratch.uid,
                                )
                                return
                            self.log.debug(
                                "hide %s because another client is active", scratch.uid
                            )
                            await self.run_hide(scratch.uid, autohide=True)

                            try:
                                del self._hysteresis_tasks[scratch.uid]
                            except KeyError:
                                pass

                        self._hysteresis_tasks[scratch.uid] = asyncio.create_task(
                            _task(scratch, hysteresis)
                        )
                    else:
                        self.log.debug("hide %s because another client is active", uid)
                        await self.run_hide(uid, autohide=True)

    async def _alternative_lookup(self):
        "if not matching by pid, use specific matching and return True"
        class_lookup_hack = [
            s
            for s in self.scratches.getByState("respawned")
            if s.conf.get("match_by", "pid") != "pid"
        ]
        if not class_lookup_hack:
            return False
        self.log.debug("Lookup hack triggered")
        # hack to update the client info from the provided match_by attribute
        clients = await self.hyprctlJSON("clients")
        for pending_scratch in class_lookup_hack:
            match_by = pending_scratch.conf["match_by"]
            match_value = pending_scratch.conf[match_by]
            match_fn = get_match_fn(match_by, match_value)
            for client in clients:
                assert isinstance(client, dict)
                if match_fn(client[match_by], match_value):
                    self.scratches.register(pending_scratch, addr=client["address"][2:])
                    self.log.debug("client class found: %s", client)
                    await pending_scratch.updateClientInfo(client)
        return True

    async def event_openwindow(self, params) -> None:
        "open windows hook"
        addr, _wrkspc, _kls, _title = params.split(",", 3)
        item = self.scratches.get(addr=addr)
        rs = list(self.scratches.getByState("respawned"))
        if rs and not item:
            # hack for windows which aren't related to the process (see #8)
            if not await self._alternative_lookup():
                self.log.info("Updating Scratch info")
                await self.updateScratchInfo()
            item = self.scratches.get(addr=addr)
            if item and item.meta["should_hide"]:
                await self.run_hide(item.uid, force=True)
        if item:
            await item.initialize(self)

    # }}}
    def cancel_task(self, uid):
        "cancel a task"
        task = self._hysteresis_tasks.get(uid)
        if task:
            task.cancel()
            self.log.debug("Canceled previous task for %s", uid)
            if uid in self._hysteresis_tasks:
                del self._hysteresis_tasks[uid]
            return True
        return False

    # Commands {{{
    async def run_toggle(self, uid_or_uids: str) -> None:
        """<name> toggles visibility of scratchpad "name" """
        if " " in uid_or_uids:
            uids = list(filter(bool, map(str.strip, uid_or_uids.split())))
        else:
            uids = [uid_or_uids.strip()]

        for uid in uids:
            self.cancel_task(uid)

        assert len(uids) > 0
        first_scratch = self.scratches.get(uids[0])
        if not first_scratch:
            self.log.warning("%s doesn't exist, can't toggle.", uids[0])
            await notify_error(
                f"Scratchpad '{uids[0]}' not found, check your configuration & the toggle parameter"
            )
            return

        if self.cast_bool(first_scratch.conf.get("alt_toggle")):
            # Needs to be on any monitor (if workspace matches)
            extra_visibility_check = first_scratch.meta[
                "space_identifier"
            ] in await get_all_space_identifiers(await self.hyprctlJSON("monitors"))
        else:
            self.log.debug(
                "visibility_check: %s == %s",
                first_scratch.meta["space_identifier"],
                get_active_space_identifier(),
            )
            # Needs to be on the active monitor+workspace
            extra_visibility_check = (
                first_scratch.meta["space_identifier"] == get_active_space_identifier()
            )  # visible on the currently focused monitor

        is_visible = first_scratch.visible and (
            first_scratch.conf.get("force_monitor") or extra_visibility_check
        )  # always showing on the same monitor
        tasks = []

        for uid in uids:
            item = self.scratches.get(uid)
            if not item:
                self.log.warning("%s is not configured", uid)
            else:
                self.log.debug(
                    "%s is visible = %s (but %s)", uid, item.visible, is_visible
                )
                if is_visible and await item.isAlive():
                    tasks.append(partial(self.run_hide, uid))
                else:
                    tasks.append(partial(self.run_show, uid))
        await asyncio.gather(*(asyncio.create_task(t()) for t in tasks))

    async def get_offsets(self, scratch, monitor=None):
        "Return offset from config or use margin as a ref"
        offset = scratch.conf.get("offset")
        rotated = monitor["transform"] in (1, 3)
        aspect = (
            reversed(scratch.client_info["size"])
            if rotated
            else scratch.client_info["size"]
        )

        if monitor is None:
            monitor = await get_focused_monitor_props(
                self.log, name=scratch.conf.get("force_monitor")
            )

        if offset:
            return [convert_monitor_dimension(offset, ref, monitor) for ref in aspect]

        # compute from client size & margin
        margin = scratch.conf.get("margin", DEFAULT_MARGIN)

        mon_size = (
            [monitor["height"], monitor["width"]]
            if rotated
            else [monitor["width"], monitor["height"]]
        )

        margins = [convert_monitor_dimension(margin, dim, monitor) for dim in mon_size]
        return map(int, [(a + m) / monitor["scale"] for a, m in zip(aspect, margins)])

    async def _hide_transition(self, scratch, monitor):
        "animate hiding a scratchpad"

        animation_type: str = scratch.conf.get("animation", "").lower()
        if not animation_type:
            return False

        off_x, off_y = await self.get_offsets(scratch, monitor)
        await self._slide_animation(animation_type, scratch, off_x, off_y)
        await asyncio.sleep(
            scratch.conf.get("hide_delay", DEFAULT_HIDE_DELAY)
        )  # await for animation to finish
        return True

    async def _slide_animation(self, animation_type, scratch, off_x, off_y):
        "Slides the window `offset` pixels respecting `animation_type`"
        addr = "address:" + scratch.full_address
        if animation_type == "fromtop":
            await self.hyprctl(f"movewindowpixel 0 {-off_y},{addr}")
        elif animation_type == "frombottom":
            await self.hyprctl(f"movewindowpixel 0 {off_y},{addr}")
        elif animation_type == "fromleft":
            await self.hyprctl(f"movewindowpixel {-off_x} 0,{addr}")
        elif animation_type == "fromright":
            await self.hyprctl(f"movewindowpixel {off_x} 0,{addr}")

    async def run_show(self, uid) -> None:
        """<name> shows scratchpad "name" """
        item = self.scratches.get(uid)

        if not item:
            self.log.warning("%s doesn't exist, can't hide.", uid)
            await notify_error(
                f"Scratchpad '{uid}' not found, check your configuration or the show parameter"
            )
            return

        self.focused_window_tracking[uid] = state.active_window

        self.cancel_task(uid)

        self.log.info("Showing %s", uid)
        was_alive = await item.isAlive()
        if not await self.ensure_alive(uid):
            self.log.error("Failed to show %s, aborting.", uid)
            return

        excluded = item.conf.get("excludes", [])
        if excluded == "*":
            excluded = [
                scratch.uid for scratch in self.scratches.values() if scratch.uid != uid
            ]
        for e_uid in excluded:
            scratch = self.scratches.get(e_uid)
            assert scratch
            if scratch.visible:
                await self.run_hide(e_uid, autohide=True)
        await item.updateClientInfo()
        await item.initialize(self)

        item.visible = True
        item.meta["space_identifier"] = get_active_space_identifier()
        monitor = await self.get_focused_monitor_props(
            name=item.conf.get("force_monitor")
        )

        assert monitor
        assert item.full_address, "No address !"

        await self._show_transition(item, monitor, was_alive)
        item.monitor = monitor["name"]

    async def _show_transition(self, item, monitor, was_alive):
        "perfoms the transition to visible state"
        animation_type = item.conf.get("animation", "").lower()
        wrkspc = monitor["activeWorkspace"]["name"]
        item.meta["last_shown"] = time.time()
        # Start the transition
        await self.hyprctl(
            [
                f"moveworkspacetomonitor special:scratch_{item.uid} {monitor['name']}",
                f"movetoworkspacesilent name:{wrkspc},address:{item.full_address}",
                f"alterzorder top,address:{item.full_address}",
            ]
        )
        preserve_aspect = self.cast_bool(item.conf.get("preserve_aspect"))
        should_set_aspect = (
            not (preserve_aspect and was_alive) or item.monitor != state.active_monitor
        )  # not aspect preserving or it's newly spawned
        if should_set_aspect:
            await self._fix_size(item, monitor)
        await item.updateClientInfo()
        position_fixed = False
        if should_set_aspect:
            position_fixed = await self._fix_position(item, monitor)
        if not position_fixed:
            if animation_type:
                if preserve_aspect and was_alive and not should_set_aspect:
                    # Relative positioning
                    if "size" not in item.client_info:
                        await self.updateScratchInfo(item)

                    ox, oy = await self.get_offsets(item, monitor)
                    await self._slide_animation(animation_type, item, -ox, -oy)
                else:
                    # Absolute positioning
                    fn = getattr(Animations, animation_type)
                    command = fn(
                        monitor,
                        item.client_info,
                        "address:" + item.full_address,
                        item.conf.get("margin", DEFAULT_MARGIN),
                    )
                    await self.hyprctl(command)
            else:
                self.log.warning(
                    "No position and no animation provided for %s, don't know where to place it.",
                    item.uid,
                )

        await self.hyprctl(f"focuswindow address:{item.full_address}")
        item.meta["last_shown"] = time.time()
        item.meta["monitor_info"] = monitor

    async def _fix_size(self, item, monitor):
        "apply the `size` config parameter"

        size = item.conf.get("size")
        if size:
            width, height = convert_coords(size, monitor)
            max_size = item.conf.get("max_size")
            if max_size:
                max_width, max_height = convert_coords(max_size, monitor)
                width = min(max_width, width)
                height = min(max_height, height)
            await self.hyprctl(
                f"resizewindowpixel exact {width} {height},address:{item.full_address}"
            )

    async def _fix_position(self, item, monitor):
        "apply the `position` config parameter"

        position = item.conf.get("position")
        if position:
            x_pos, y_pos = convert_coords(position, monitor)
            x_pos_abs, y_pos_abs = x_pos + monitor["x"], y_pos + monitor["y"]
            await self.hyprctl(
                f"movewindowpixel exact {x_pos_abs} {y_pos_abs},address:{item.full_address}"
            )
            return True
        return False

    async def run_hide(self, uid: str, force=False, autohide=False) -> None:
        """<name> hides scratchpad "name"
        if `autohide` is True, skips focus tracking
        `force` ignores the visibility check"""
        scratch = self.scratches.get(uid)

        if not scratch:
            await notify_error(
                f"Scratchpad '{uid}' not found, check your configuration or the hide parameter"
            )
            self.log.warning("%s is not configured", uid)
            return
        if not scratch.visible and not force and not autohide:
            await notify_error(f"Scratchpad '{uid}' is not visible, will not hide.")
            self.log.warning("%s is already hidden", uid)
            return
        scratch.visible = False
        scratch.meta["should_hide"] = False
        self.log.info("Hiding %s", uid)
        animated = await self._hide_transition(scratch, scratch.meta["monitor_info"])

        await self.hyprctl(
            f"movetoworkspacesilent special:scratch_{uid},address:{scratch.full_address}"
        )

        if (
            not autohide
            and animated
            and uid in self.focused_window_tracking
            and self.cast_bool(scratch.conf.get("restore_focus"), True)
        ):  # focus got lost when animating
            await self.hyprctl(
                f"focuswindow address:{self.focused_window_tracking[uid]}"
            )
            del self.focused_window_tracking[uid]

    # }}}


# }}}
