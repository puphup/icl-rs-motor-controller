"""Trivision / triangular-prism show controller.

Each motor drives a 3-sided rotating prism. One *page* corresponds to every
motor showing the same face of its prism. ``current_page`` is tracked in-app
because all transitions are relative-mode 120° moves (no encoder homing per
transition); ``set_zero`` on every motor resets the reference for page 1.

A transition is a *coordinated* rotation across every motor — one of the
:data:`EFFECTS` strategies decides the per-motor start delay so the array
flips with a chosen visual rhythm.
"""

from __future__ import annotations

import asyncio
import random
from dataclasses import dataclass, field
from typing import Callable, Iterable

from .drivers import MotorDriver


PAGES = (1, 2, 3)                  # 3-sided prism
PAGE_STEP_DEG = 120.0              # 360 / 3


def face_for_position(position_deg: float) -> int:
    """Map an angle in degrees to the visible face (1, 2, or 3).

    Face 1 is centred on 0°, face 2 on 120°, face 3 on 240°. We snap to the
    nearest 120° increment and wrap, so a tiny drift either side of zero still
    reads as face 1 instead of flipping to 3 when the position dips negative.
    """
    if position_deg is None:
        return 1
    idx = round(position_deg / PAGE_STEP_DEG) % 3
    return int(idx) + 1
DEFAULT_SPEED_RPM = 60
DEFAULT_ACCEL = 200
DEFAULT_DECEL = 200
DEFAULT_STEP_MS = 100              # per-motor delay for wave-style effects


# ---------------------------------------------------------------------------
# Effect schedule builders
#
# Each builder takes the ordered list of motor keys + an options dict, and
# returns a list of (motor_key, delay_ms) tuples. The delay is how long each
# motor waits before issuing its move command, so the user sees a coordinated
# rhythm across the array.
# ---------------------------------------------------------------------------

Schedule = list[tuple[str, int]]


def _simultaneous(keys: list[str], opts: dict) -> Schedule:
    return [(k, 0) for k in keys]


def _wave(keys: list[str], opts: dict) -> Schedule:
    step = int(opts.get("step_ms", DEFAULT_STEP_MS))
    return [(k, i * step) for i, k in enumerate(keys)]


def _reverse_wave(keys: list[str], opts: dict) -> Schedule:
    step = int(opts.get("step_ms", DEFAULT_STEP_MS))
    n = len(keys)
    return [(k, (n - 1 - i) * step) for i, k in enumerate(keys)]


def _alternate(keys: list[str], opts: dict) -> Schedule:
    """Even-indexed motors first, then odd-indexed with a per-step delay."""
    step = int(opts.get("step_ms", DEFAULT_STEP_MS))
    gap = int(opts.get("gap_ms", step * 4))
    out: Schedule = []
    evens = [k for i, k in enumerate(keys) if i % 2 == 0]
    odds  = [k for i, k in enumerate(keys) if i % 2 == 1]
    for i, k in enumerate(evens):
        out.append((k, i * step))
    for i, k in enumerate(odds):
        out.append((k, gap + i * step))
    return out


def _random(keys: list[str], opts: dict) -> Schedule:
    max_jitter = int(opts.get("max_jitter_ms", 1500))
    return [(k, random.randint(0, max_jitter)) for k in keys]


def _center_out(keys: list[str], opts: dict) -> Schedule:
    """Motors closest to the middle of the array fire first, working outward."""
    step = int(opts.get("step_ms", DEFAULT_STEP_MS))
    n = len(keys)
    mid = (n - 1) / 2.0
    out: Schedule = []
    for i, k in enumerate(keys):
        out.append((k, int(abs(i - mid) * step)))
    return out


def _edges_in(keys: list[str], opts: dict) -> Schedule:
    """Mirror of center-out: outermost motors fire first."""
    step = int(opts.get("step_ms", DEFAULT_STEP_MS))
    n = len(keys)
    mid = (n - 1) / 2.0
    return [(k, int((mid - abs(i - mid)) * step)) for i, k in enumerate(keys)]


# Public catalog; UI loads from this via /api/show/effects.
EFFECTS: dict[str, dict] = {
    "simultaneous":   {"label": "Simultaneous",   "builder": _simultaneous,   "params": []},
    "wave":           {"label": "Wave ▶",     "builder": _wave,           "params": ["step_ms"]},
    "reverse_wave":   {"label": "Reverse wave ◀", "builder": _reverse_wave, "params": ["step_ms"]},
    "alternate":      {"label": "Alternate (even → odd)", "builder": _alternate, "params": ["step_ms", "gap_ms"]},
    "random":         {"label": "Random jitter",  "builder": _random,         "params": ["max_jitter_ms"]},
    "center_out":     {"label": "Center out",     "builder": _center_out,     "params": ["step_ms"]},
    "edges_in":       {"label": "Edges in",       "builder": _edges_in,       "params": ["step_ms"]},
}


def effects_catalog() -> list[dict]:
    """JSON-friendly catalog for the UI."""
    return [
        {"key": k, "label": v["label"], "params": v["params"]}
        for k, v in EFFECTS.items()
    ]


# ---------------------------------------------------------------------------
# Show controller
# ---------------------------------------------------------------------------

@dataclass
class TransitionOptions:
    effect: str = "simultaneous"
    speed_rpm: int = DEFAULT_SPEED_RPM
    accel: int = DEFAULT_ACCEL
    decel: int = DEFAULT_DECEL
    step_ms: int = DEFAULT_STEP_MS
    gap_ms: int = DEFAULT_STEP_MS * 4
    max_jitter_ms: int = 1500


@dataclass
class AutoCycle:
    running: bool = False
    direction: int = 1               # +1 = forward, -1 = backward
    hold_s: float = 5.0
    effect: str = "wave"
    options: TransitionOptions = field(default_factory=TransitionOptions)
    task: asyncio.Task | None = None


class ShowController:
    """Manages page state, transition orchestration, and auto-cycle."""

    def __init__(self):
        self.current_page: int = 1
        self.last_effect: str = "simultaneous"
        self.last_transition_at_motor_count: int = 0
        self._lock = asyncio.Lock()
        self.auto = AutoCycle()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def state(self) -> dict:
        return {
            "current_page": self.current_page,
            "pages": list(PAGES),
            "last_effect": self.last_effect,
            "auto": {
                "running": self.auto.running,
                "direction": self.auto.direction,
                "hold_s": self.auto.hold_s,
                "effect": self.auto.effect,
            },
        }

    async def next_page(self, drivers: dict[str, MotorDriver], opts: TransitionOptions):
        await self._step(drivers, +1, opts)

    async def prev_page(self, drivers: dict[str, MotorDriver], opts: TransitionOptions):
        await self._step(drivers, -1, opts)

    async def goto(self, drivers: dict[str, MotorDriver], target_page: int, opts: TransitionOptions):
        target_page = ((int(target_page) - 1) % 3) + 1
        if target_page == self.current_page:
            return
        # Shortest mechanical path — prefer the one-step rotation that gets
        # there, choosing sign. e.g. 1 → 3 picks -1 (reverse), not +2.
        raw = target_page - self.current_page                # ∈ {-2,-1,1,2}
        if raw == 2:   delta = -1
        elif raw == -2: delta = 1
        else:           delta = raw
        await self._step(drivers, delta, opts)

    async def set_current_page(self, page: int):
        """Manually set what page the array is considered to be on (e.g. after a
        Set Zero, when face 1 is freshly aligned). Doesn't move any motors."""
        self.current_page = ((int(page) - 1) % 3) + 1

    # ------------------------------------------------------------------
    # Auto-cycle
    # ------------------------------------------------------------------

    async def start_auto(self, drivers: dict[str, MotorDriver],
                         hold_s: float, direction: int,
                         opts: TransitionOptions):
        await self.stop_auto()
        self.auto = AutoCycle(
            running=True,
            direction=1 if direction >= 0 else -1,
            hold_s=max(0.5, float(hold_s)),
            effect=opts.effect,
            options=opts,
        )
        self.auto.task = asyncio.create_task(self._auto_loop(drivers))

    async def stop_auto(self):
        if self.auto.task and not self.auto.task.done():
            self.auto.task.cancel()
            try:
                await self.auto.task
            except (asyncio.CancelledError, Exception):
                pass
        self.auto.running = False
        self.auto.task = None

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    async def _step(self, drivers: dict[str, MotorDriver], delta_pages: int,
                    opts: TransitionOptions):
        """``delta_pages`` is signed — positive rotates forward (angle ↑),
        negative rotates backward (angle ↓). The page bookkeeping wraps mod 3
        either way."""
        delta_pages = int(delta_pages)
        if delta_pages == 0:
            return
        async with self._lock:
            await self._fire_transition(drivers, delta_pages, opts)
            self.current_page = ((self.current_page - 1 + delta_pages) % 3) + 1
            self.last_effect = opts.effect

    async def _fire_transition(self, drivers: dict[str, MotorDriver],
                               delta_pages: int, opts: TransitionOptions):
        # ``delta_pages`` is signed so motor angle moves the same direction
        # the operator clicked: Next → +120°, Prev → -120°.
        keys = list(drivers.keys())
        if not keys:
            return
        builder = EFFECTS.get(opts.effect, EFFECTS["simultaneous"])["builder"]
        schedule = builder(keys, vars(opts))
        self.last_transition_at_motor_count = len(keys)

        angle_deg = PAGE_STEP_DEG * delta_pages

        # Auto-enable every motor before firing. A Trivision controller is
        # operationally weird if "Next face" silently no-ops because the motors
        # happen to be disabled — much friendlier to just arm them on demand.
        async def _arm(motor_key: str):
            d = drivers.get(motor_key)
            if d is None:
                return
            try:
                await d.enable()
            except Exception:
                pass
        await asyncio.gather(*(_arm(k) for k, _ in schedule))

        async def one(motor_key: str, delay_ms: int):
            if delay_ms > 0:
                await asyncio.sleep(delay_ms / 1000.0)
            d = drivers.get(motor_key)
            if d is None:
                return
            try:
                await d.start_move("relative", angle_deg, opts.speed_rpm, opts.accel, opts.decel)
            except Exception:
                pass     # one bad motor shouldn't kill the whole transition

        await asyncio.gather(*(one(k, dly) for k, dly in schedule))

    async def _auto_loop(self, drivers: dict[str, MotorDriver]):
        try:
            while True:
                # Sleep the hold, then transition once
                await asyncio.sleep(self.auto.hold_s)
                if not self.auto.running:
                    return
                opts = self.auto.options
                await self._step(drivers, +1 if self.auto.direction >= 0 else -1, opts)
        except asyncio.CancelledError:
            return
        finally:
            self.auto.running = False
