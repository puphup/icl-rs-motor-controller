"""TL-R series RS485-integrated controller driver.

The TL-R has **two distinct positioning systems**:

* **Single positioning** (PA_033–PA_038, regs 51-56) — triggered over RS485
  by writing Bit 0 of the **control word** (PA_04E). This is the path we use.
* **Internal multi-segment positioning** (PA_050+, regs 80+, "Path 0..15") —
  triggered by **digital input pins**, NOT over the bus. Leaving Path 0
  registers alone has no effect on a Bit-0 trigger.

Register map (all addresses DECIMAL, per the TL-R manual sections 3.1 & 3.5):

==========  =========  ===========================================  =====
Param       Address    Description                                  Mode
==========  =========  ===========================================  =====
PA_004        4        Operating Status                              RO
PA_005        5        Current Alarm                                 RO
PA_008/009    8/9      Current Position H/L (signed 32-bit pulses)   RO
PA_00A       10        Current Speed (signed r/min)                  RO
PA_034       52        Positioning Acceleration Time (ms)            RW
PA_035       53        Positioning Deceleration Time (ms)            RW
PA_036       54        Positioning Speed (r/min)                     RW
PA_037       55        Positioning Target H (signed pulses)          RW
PA_038       56        Positioning Target L                          RW
PA_04E       78        Control Word (bit-packed)                     RW
PA_04F       79        Auxiliary Control (command codes)             RW
==========  =========  ===========================================  =====

**Move sequence**: write the single-positioning block (regs 52-56, contiguous
5-reg write of accel/decel/speed/target_h/target_l), then write the control
word (reg 78) with Bit0=1 (positioning enable) | Bit1=mode (rel=0/abs=1) |
Bit2=1 (interrupt current motion if any). The drive picks up the rising edge
of Bit0 and executes the move.

**Operating status bits (reg 4)**: Bit0=in-position, Bit1=homing-complete,
Bit2=motor-running, Bit3=fault, Bit4=motor-enabled, Bit5/6=soft limits.
"""

from __future__ import annotations

from ..modbus_interface import ModbusInterface
from ..registers import (
    degrees_to_pulses, split_32, join_32_signed, pulses_to_degrees,
)
from .base import MotorDriver, MotorStatus


# ---------------------------------------------------------------------------
# Register addresses (decimal)
# ---------------------------------------------------------------------------
PA_OPERATING_STATUS = 4
PA_CURRENT_ALARM   = 5
PA_CURRENT_POS_H   = 8
PA_CURRENT_POS_L   = 9
PA_CURRENT_SPEED   = 10

# Single positioning parameters (used when triggering via control word Bit 0)
PA_POS_START_SPEED = 51          # PA_033 (not written by us — leave at NVRAM default)
PA_POS_ACCEL       = 52          # PA_034 — Positioning Acceleration Time (ms)
PA_POS_DECEL       = 53          # PA_035 — Positioning Deceleration Time (ms)
PA_POS_SPEED       = 54          # PA_036 — Positioning Speed (r/min)
PA_POS_TARGET_H    = 55          # PA_037 — Positioning Target H (pulses)
PA_POS_TARGET_L    = 56          # PA_038 — Positioning Target L

PA_CONTROL_WORD    = 78          # PA_04E
PA_AUX_CONTROL     = 79          # PA_04F

# ---------------------------------------------------------------------------
# Control word bit layout (PA_04E)
# ---------------------------------------------------------------------------
CW_POS_ENABLE      = 1 << 0      # rising edge starts the move
CW_POS_ABSOLUTE    = 1 << 1      # 0 = relative, 1 = absolute
CW_INTERRUPT       = 1 << 2      # 1 = interrupt current motion, 0 = queue/ignore
CW_JOG_ENABLE      = 1 << 3
CW_HOME_ENABLE     = 1 << 4
CW_STOP            = 1 << 5
CW_ESTOP           = 1 << 6

# ---------------------------------------------------------------------------
# Auxiliary control codes (PA_04F)
# ---------------------------------------------------------------------------
AUX_NONE              = 0x0000
AUX_RESTORE_FACTORY   = 0x0100
AUX_SAVE_PARAMETERS   = 0x0200
AUX_CLEAR_ALARM       = 0x0300
AUX_CLEAR_POSITION    = 0x0400
AUX_MOTOR_ENABLE      = 0x0500
AUX_MOTOR_RELEASE     = 0x0600

# ---------------------------------------------------------------------------
# Operating status bits (PA_004 / reg 4)
# ---------------------------------------------------------------------------
OS_IN_POSITION       = 1 << 0
OS_HOMING_COMPLETE   = 1 << 1
OS_MOTOR_RUNNING     = 1 << 2
OS_FAULT             = 1 << 3
OS_MOTOR_ENABLED     = 1 << 4


def _signed16(raw: int) -> int:
    """Decode a 16-bit unsigned register as signed int16."""
    return raw - 0x10000 if raw >= 0x8000 else raw


class TLRDriver(MotorDriver):
    """TL-R RS485 integrated controller."""

    def __init__(self, modbus: ModbusInterface, slave_id: int):
        self.modbus = modbus
        self.slave_id = slave_id

    async def _aux(self, code: int) -> None:
        await self.modbus.write_registers(self.slave_id, PA_AUX_CONTROL, [code])
        # Clear the aux command so the next write is fresh — the drive latches
        # on the value transition; some firmware versions require an explicit
        # clear before re-issuing the same code.
        await self.modbus.write_registers(self.slave_id, PA_AUX_CONTROL, [AUX_NONE])

    async def _control(self, bits: int) -> None:
        """Write the control word, then clear it so the next op sees a rising edge."""
        await self.modbus.write_registers(self.slave_id, PA_CONTROL_WORD, [bits])
        await self.modbus.write_registers(self.slave_id, PA_CONTROL_WORD, [0])

    async def enable(self) -> None:
        await self._aux(AUX_MOTOR_ENABLE)

    async def disable(self) -> None:
        await self._aux(AUX_MOTOR_RELEASE)

    async def start_move(self, mode, angle_deg, speed_rpm, accel, decel):
        pulses = degrees_to_pulses(angle_deg)
        pos_h, pos_l = split_32(pulses)
        # Stage SINGLE-positioning parameters. Writing one register at a time
        # (function 0x06 under the hood — pymodbus's write_registers with a
        # length-1 list still uses 0x10, which the TL-R also accepts, but a
        # multi-register write of 5 contiguous values is silently truncated by
        # this drive's firmware). One-at-a-time is reliable.
        await self.modbus.write_registers(self.slave_id, PA_POS_ACCEL,    [int(accel)])
        await self.modbus.write_registers(self.slave_id, PA_POS_DECEL,    [int(decel)])
        await self.modbus.write_registers(self.slave_id, PA_POS_SPEED,    [int(speed_rpm)])
        await self.modbus.write_registers(self.slave_id, PA_POS_TARGET_H, [pos_h])
        await self.modbus.write_registers(self.slave_id, PA_POS_TARGET_L, [pos_l])

        # Trigger via control word: positioning enable + mode + interrupt.
        bits = CW_POS_ENABLE | CW_INTERRUPT
        if mode == "absolute":
            bits |= CW_POS_ABSOLUTE
        await self._control(bits)

    async def stop_motion(self) -> None:
        # Use the "Stop" bit (not e-stop) so the drive decelerates without
        # latching a fault — the right primitive for jog-release.
        await self._control(CW_STOP)

    async def estop(self) -> None:
        await self._control(CW_ESTOP)

    async def alarm_reset(self) -> None:
        await self._aux(AUX_CLEAR_ALARM)

    async def save_params(self) -> None:
        await self._aux(AUX_SAVE_PARAMETERS)

    async def read_status(self) -> MotorStatus:
        try:
            # Status + alarm in two single reads (different banks).
            status_regs = await self.modbus.read_holding_registers(self.slave_id, PA_OPERATING_STATUS, 1)
            alarm_regs = await self.modbus.read_holding_registers(self.slave_id, PA_CURRENT_ALARM, 1)
            pos_regs = await self.modbus.read_holding_registers(self.slave_id, PA_CURRENT_POS_H, 2)
            vel_regs = await self.modbus.read_holding_registers(self.slave_id, PA_CURRENT_SPEED, 1)
        except Exception:
            return {
                "position_deg": 0.0, "position_pulses": 0, "velocity_rpm": 0,
                "running": False, "enabled": False, "estopped": False,
                "alarm": 0, "status_bits": 0, "offline": True,
            }

        status = status_regs[0]
        raw_pulses = join_32_signed(pos_regs[0], pos_regs[1])
        vel_rpm = _signed16(vel_regs[0])
        return {
            "position_deg": round(pulses_to_degrees(raw_pulses), 2),
            "position_pulses": raw_pulses,
            "velocity_rpm": vel_rpm,
            "running": bool(status & OS_MOTOR_RUNNING),
            "enabled": bool(status & OS_MOTOR_ENABLED),
            "estopped": False,
            "alarm": alarm_regs[0],
            "status_bits": status,
            "offline": False,
        }

    async def test_connection(self) -> dict:
        try:
            regs = await self.modbus.read_holding_registers(self.slave_id, PA_OPERATING_STATUS, 1)
            return {"ok": True, "slave_id": self.slave_id, "status": regs[0]}
        except Exception as e:
            return {"ok": False, "slave_id": self.slave_id, "error": str(e)}
