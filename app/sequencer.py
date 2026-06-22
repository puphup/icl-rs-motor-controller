"""Multi-motor sequential control, keyed by motor_key (gateway.slave_id)."""

import asyncio
from dataclasses import dataclass

from .drivers import MotorDriver


@dataclass
class MotorStep:
    motor_key: str
    angle_deg: float
    speed_rpm: int
    accel: int
    decel: int


class MultiMotorSequencer:
    def __init__(self, drivers: dict[str, MotorDriver], motor_keys: list[str]):
        self.drivers = drivers
        self.motor_keys = list(motor_keys)
        self.phase: str = "idle"
        self.active: bool = False
        self.error: str | None = None
        self._cancelled: bool = False
        self._lock = asyncio.Lock()

    async def run_sequence(
        self,
        steps: list[MotorStep],
        delay_s: float = 1.0,
        mode: str = "relative",
    ):
        async with self._lock:
            self.active = True
            self._cancelled = False
            self.error = None
            try:
                await self._execute(steps, delay_s, mode)
            except asyncio.CancelledError:
                self.phase = "idle"
                raise
            except Exception as e:
                self.phase = "error"
                self.error = str(e)
            finally:
                self.active = False

    async def _execute(self, steps: list[MotorStep], delay_s: float, mode: str):
        self.phase = "enabling"
        for step in steps:
            d = self.drivers.get(step.motor_key)
            if d is not None:
                await d.enable()
        if self._cancelled:
            self.phase = "idle"
            return

        for idx, step in enumerate(steps):
            if self._cancelled:
                self.phase = "idle"
                return
            d = self.drivers.get(step.motor_key)
            if d is None:
                raise RuntimeError(f"No driver for motor {step.motor_key!r}")
            self.phase = f"moving:{step.motor_key}"
            await d.start_move(mode, step.angle_deg, step.speed_rpm, step.accel, step.decel)

            if idx < len(steps) - 1:
                if self._cancelled:
                    self.phase = "idle"
                    return
                self.phase = "delay"
                await asyncio.sleep(delay_s)

        self.phase = "waiting"
        for step in steps:
            d = self.drivers.get(step.motor_key)
            if d is not None:
                await self._wait_completion(d, timeout=60.0)

        self.phase = "complete"

    async def _wait_completion(self, driver: MotorDriver, timeout: float = 30.0):
        elapsed = 0.0
        await asyncio.sleep(0.1)
        while elapsed < timeout:
            if self._cancelled:
                return
            try:
                st = await driver.read_status()
            except Exception:
                await asyncio.sleep(0.1)
                elapsed += 0.1
                continue
            if not st.get("running"):
                return
            await asyncio.sleep(0.05)
            elapsed += 0.05
        raise TimeoutError(f"Motor {driver.slave_id} did not complete within {timeout}s")

    async def emergency_stop_all(self):
        self._cancelled = True
        for key in self.motor_keys:
            d = self.drivers.get(key)
            if d is None:
                continue
            try:
                await d.estop()
            except Exception:
                pass
        self.phase = "idle"
        self.active = False

    def cancel(self):
        self._cancelled = True
