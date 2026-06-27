"""Motor-specific driver implementations.

The :class:`MotorDriver` ABC defines the high-level operations the server needs
(enable, move, jog-stop, e-stop, alarm-reset, save, read-status).  Each motor
family ships a concrete implementation that knows how to map those ops to its
own Modbus register layout.

Currently supported types:

==========   ===========================================================
Type key     Description
==========   ===========================================================
``icl_rs``   Leadshine iCL-RS / DM-RS family (PR0 register block at
             0x6200, status at 0x1003, enable at 0x000F, e-stop at
             0x6002, system commands at 0x1801).
``tl_r``     TL-R series RS485-integrated controllers (control word at
             PA_04E, auxiliary control at PA_04F, position path 0 at
             PA_050-PA_054, status at PA_004, position at PA_008/009,
             velocity at PA_00A).
``sim``      In-process simulator — bypasses Modbus entirely and drives
             a :class:`MotorSim` directly.
==========   ===========================================================
"""

from typing import TYPE_CHECKING

from .base import MotorDriver
from .icl_rs import ICLRSDriver
from .tl_r import TLRDriver
from .sim import SimDriver

if TYPE_CHECKING:
    from ..modbus_interface import ModbusInterface
    from ..motor_sim import MotorSim


# Display-friendly metadata used by the UI to populate the per-motor driver
# selector.  Keep keys lowercase; ``label`` is what the user sees.
DRIVER_CATALOG: dict[str, dict] = {
    "icl_rs": {"label": "iCL-RS / DM-RS (Leadshine PR0)"},
    "tl_r":   {"label": "TL-R series (RS485 Integrated)"},
}

# Per-driver-type pulses-per-rev. These are hardware-model constants: the
# iCL-RS takes 10000 command pulses/rev (Pr0.01) and reports a 65536-count
# encoder; the TL-R takes/reports 4000 (PA_101). A single global PPR can't
# serve a mixed bus, so each driver carries its own. ponytail: calibration
# knob — re-measure and edit here if a drive is configured differently.
DRIVER_PPR: dict[str, dict] = {
    "icl_rs": {"command_ppr": 10000, "encoder_ppr": 65536},
    # TL-R: measured empirically (PA_101's 4000 is wrong for these registers).
    # With the clean low→high move trigger, target pulses map 1:1 to encoder
    # counts, and the encoder is ~1000 counts/rev (jog 30rpm×20s → 9928 counts
    # over 10 revs). So 1000/1000: command 120° → 333 pulses → 333 counts → 120°
    # physical, and the UI reads it back as 120°.
    "tl_r":   {"command_ppr": 1000,  "encoder_ppr": 1000},
}


def make_hardware_driver(
    driver_type: str,
    modbus: "ModbusInterface",
    slave_id: int,
) -> MotorDriver:
    """Build a hardware driver of the given type for one motor."""
    key = (driver_type or "icl_rs").lower()
    ppr = DRIVER_PPR.get(key, {"command_ppr": 10000, "encoder_ppr": 10000})
    if key == "icl_rs":
        return ICLRSDriver(modbus, slave_id, **ppr)
    if key == "tl_r":
        return TLRDriver(modbus, slave_id, **ppr)
    raise ValueError(f"Unknown driver type: {driver_type!r}")


def make_sim_driver(motor: "MotorSim") -> MotorDriver:
    """Build a simulator driver bound to an in-process :class:`MotorSim`."""
    return SimDriver(motor)


__all__ = [
    "MotorDriver",
    "ICLRSDriver",
    "TLRDriver",
    "SimDriver",
    "DRIVER_CATALOG",
    "make_hardware_driver",
    "make_sim_driver",
]
