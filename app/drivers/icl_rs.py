"""Leadshine iCL-RS / DM-RS driver — PR0 register layout."""

from __future__ import annotations

from ..modbus_interface import ModbusInterface
from ..registers import (
    PR0_MODE, PR0_TRIGGER, PR0_TRIGGER_VAL,
    MOTION_STATUS, FEEDBACK_POS_H, FEEDBACK_VEL_H, CURRENT_ALARM,
    ESTOP_REG, ESTOP_VAL, SYSTEM_CMD_REG, ALARM_RESET_VAL, PERM_SAVE_VAL,
    SW_ENABLE_REG, SW_ENABLE_VAL,
    MODE_ABSOLUTE, MODE_RELATIVE,
    STATUS_RUNNING, STATUS_CMD_OK, STATUS_PATH_OK,
    degrees_to_pulses, split_32, join_32, join_32_signed, pulses_to_degrees,
)
from .base import MotorDriver, MotorStatus


class ICLRSDriver(MotorDriver):
    """Leadshine iCL-RS family. Move semantics: write PR0 block, then trigger."""

    def __init__(self, modbus: ModbusInterface, slave_id: int):
        self.modbus = modbus
        self.slave_id = slave_id

    async def enable(self) -> None:
        await self.modbus.write_registers(self.slave_id, SW_ENABLE_REG, [SW_ENABLE_VAL])

    async def disable(self) -> None:
        await self.modbus.write_registers(self.slave_id, SW_ENABLE_REG, [0])

    async def start_move(self, mode, angle_deg, speed_rpm, accel, decel):
        mode_val = MODE_ABSOLUTE if mode == "absolute" else MODE_RELATIVE
        pulses = degrees_to_pulses(angle_deg)
        pos_h, pos_l = split_32(pulses)
        await self.modbus.write_registers(
            self.slave_id, PR0_MODE,
            [mode_val, pos_h, pos_l, speed_rpm, accel, decel],
        )
        await self.modbus.write_registers(self.slave_id, PR0_TRIGGER, [PR0_TRIGGER_VAL])

    async def stop_motion(self) -> None:
        # iCL-RS doesn't expose a separate "clean stop" register — the e-stop
        # value also acts as a controlled-stop on most drives in this family,
        # and the display flag for estopped is computed locally in sim only.
        await self.modbus.write_registers(self.slave_id, ESTOP_REG, [ESTOP_VAL])

    async def estop(self) -> None:
        await self.modbus.write_registers(self.slave_id, ESTOP_REG, [ESTOP_VAL])

    async def alarm_reset(self) -> None:
        await self.modbus.write_registers(self.slave_id, SYSTEM_CMD_REG, [ALARM_RESET_VAL])

    async def save_params(self) -> None:
        await self.modbus.write_registers(self.slave_id, SYSTEM_CMD_REG, [PERM_SAVE_VAL])

    async def read_status(self) -> MotorStatus:
        try:
            status_regs = await self.modbus.read_holding_registers(self.slave_id, MOTION_STATUS, 1)
            pos_regs = await self.modbus.read_holding_registers(self.slave_id, FEEDBACK_POS_H, 2)
            vel_regs = await self.modbus.read_holding_registers(self.slave_id, FEEDBACK_VEL_H, 2)
            alarm_regs = await self.modbus.read_holding_registers(self.slave_id, CURRENT_ALARM, 1)
        except Exception:
            return {
                "position_deg": 0.0, "position_pulses": 0, "velocity_rpm": 0,
                "running": False, "enabled": False, "estopped": False,
                "alarm": 0, "status_bits": 0, "offline": True,
            }

        raw_pulses = join_32_signed(pos_regs[0], pos_regs[1])
        status = status_regs[0]
        # Velocity: high register reads 0xFFFF when idle/invalid; use low only in that case.
        vel_rpm = vel_regs[1] if vel_regs[0] == 0xFFFF else join_32(vel_regs[0], vel_regs[1])
        running = bool(status & STATUS_RUNNING)
        enabled = bool(status & (STATUS_CMD_OK | STATUS_PATH_OK | STATUS_RUNNING))
        return {
            "position_deg": round(pulses_to_degrees(raw_pulses), 2),
            "position_pulses": raw_pulses,
            "velocity_rpm": vel_rpm,
            "running": running,
            "enabled": enabled,
            "estopped": False,   # no per-drive estop latch on real hw
            "alarm": alarm_regs[0],
            "status_bits": status,
            "offline": False,
        }

    async def test_connection(self) -> dict:
        try:
            regs = await self.modbus.read_holding_registers(self.slave_id, MOTION_STATUS, 1)
            return {"ok": True, "slave_id": self.slave_id, "status": regs[0]}
        except Exception as e:
            return {"ok": False, "slave_id": self.slave_id, "error": str(e)}
