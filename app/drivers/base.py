"""Abstract base class for motor drivers."""

from abc import ABC, abstractmethod
from typing import TypedDict


class MotorStatus(TypedDict, total=False):
    """Normalized motor status returned by :meth:`MotorDriver.read_status`.

    All drivers return the same shape so the server / UI layer doesn't need to
    know which physical drive is on the other end of the bus.
    """

    position_deg: float       # current shaft angle, degrees; software zero applied by caller
    position_pulses: int      # raw encoder pulses (signed)
    velocity_rpm: int         # signed RPM feedback
    running: bool             # motor currently in motion
    enabled: bool             # software-enabled (motor energized)
    estopped: bool            # latched e-stop flag (sim-only on hardware)
    alarm: int                # current alarm code (0 = none)
    status_bits: int          # raw status register, motor-specific layout
    offline: bool             # True if the read transaction failed entirely


class MotorDriver(ABC):
    """High-level interface every motor type implements."""

    slave_id: int

    @abstractmethod
    async def enable(self) -> None: ...

    @abstractmethod
    async def disable(self) -> None: ...

    @abstractmethod
    async def start_move(
        self,
        mode: str,           # "absolute" or "relative"
        angle_deg: float,
        speed_rpm: int,
        accel: int,
        decel: int,
    ) -> None: ...

    @abstractmethod
    async def stop_motion(self) -> None:
        """Decelerate to stop without latching e-stop (used by jog release)."""

    @abstractmethod
    async def estop(self) -> None:
        """Emergency stop — may latch a fault depending on the drive."""

    @abstractmethod
    async def alarm_reset(self) -> None: ...

    @abstractmethod
    async def save_params(self) -> None:
        """Persist current parameters to non-volatile memory on the drive."""

    @abstractmethod
    async def read_status(self) -> MotorStatus: ...

    @abstractmethod
    async def test_connection(self) -> dict:
        """Lightweight ping: returns ``{"ok": bool, "slave_id": int, ...}``."""
