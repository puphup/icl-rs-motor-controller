"""Multi-motor sequential control logic with completion watchdog."""

import asyncio
from dataclasses import dataclass

from .modbus_interface import ModbusInterface
from .registers import (
    PR0_MODE, PR0_TRIGGER, PR0_TRIGGER_VAL,
    MOTION_STATUS, STATUS_CMD_OK,
    SW_ENABLE_REG, SW_ENABLE_VAL,
    ESTOP_REG, ESTOP_VAL,
    MODE_RELATIVE, degrees_to_pulses, split_32,
)


@dataclass
class MotorStep:
    slave_id: int
    angle_deg: float
    speed_rpm: int
    accel: int
    decel: int


class MultiMotorSequencer:
    def __init__(self, modbus: ModbusInterface, slave_ids: list[int]):
        self.modbus = modbus
        self.slave_ids = list(slave_ids)
        self.phase: str = "idle"  # idle | enabling | moving_<id> | delay | waiting | complete | error
        self.active: bool = False
        self.error: str | None = None
        self._cancelled: bool = False
        self._lock = asyncio.Lock()

    async def run_sequence(
        self,
        steps: list[MotorStep],
        delay_s: float = 1.0,
        mode: int = MODE_RELATIVE,
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

    async def _execute(self, steps: list[MotorStep], delay_s: float, mode: int):
        # Step 1: Enable all motors that will move
        self.phase = "enabling"
        for step in steps:
            await self.modbus.write_registers(step.slave_id, SW_ENABLE_REG, [SW_ENABLE_VAL])

        if self._cancelled:
            self.phase = "idle"
            return

        # Step 2: Trigger each motor in turn, with delay between triggers
        for idx, step in enumerate(steps):
            if self._cancelled:
                self.phase = "idle"
                return

            self.phase = f"moving_m{step.slave_id}"
            await self._send_move(step.slave_id, mode, step.angle_deg, step.speed_rpm, step.accel, step.decel)

            # Delay before triggering next motor (not after the last)
            if idx < len(steps) - 1:
                if self._cancelled:
                    self.phase = "idle"
                    return
                self.phase = "delay"
                await asyncio.sleep(delay_s)

        # Step 3: Wait for every motor to finish
        self.phase = "waiting"
        for step in steps:
            await self._wait_completion(step.slave_id, timeout=30.0)

        self.phase = "complete"

    async def _send_move(self, slave_id: int, mode: int, angle_deg: float, speed: int, accel: int, decel: int):
        pulses = degrees_to_pulses(angle_deg)
        pos_h, pos_l = split_32(pulses)
        await self.modbus.write_registers(slave_id, PR0_MODE, [mode, pos_h, pos_l, speed, accel, decel])
        await self.modbus.write_registers(slave_id, PR0_TRIGGER, [PR0_TRIGGER_VAL])

    async def _wait_completion(self, slave_id: int, timeout: float = 30.0):
        elapsed = 0.0
        while elapsed < timeout:
            if self._cancelled:
                return
            regs = await self.modbus.read_holding_registers(slave_id, MOTION_STATUS, 1)
            if regs[0] & STATUS_CMD_OK:
                return
            await asyncio.sleep(0.05)
            elapsed += 0.05
        raise TimeoutError(f"Motor {slave_id} did not complete within {timeout}s")

    async def emergency_stop_all(self):
        """Send e-stop to every configured motor."""
        self._cancelled = True
        for sid in self.slave_ids:
            try:
                await self.modbus.write_registers(sid, ESTOP_REG, [ESTOP_VAL])
            except Exception:
                pass
        self.phase = "idle"
        self.active = False

    def cancel(self):
        self._cancelled = True
