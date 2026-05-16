"""Config loader — reads/writes config.json."""

import json
import os
from pathlib import Path


def _config_path() -> Path:
    """Where config.json lives.

    When frozen by PyInstaller, the launcher sets PYSIM_CONFIG_DIR to the directory
    next to the .exe so the user can edit settings without unpacking the bundle.
    """
    env = os.environ.get("PYSIM_CONFIG_DIR")
    if env:
        return Path(env) / "config.json"
    return Path(__file__).parent.parent / "config.json"


CONFIG_PATH = _config_path()

MAX_MOTORS = 5

DEFAULTS = {
    "connection": {
        "mode": "simulation",
        "serial_port": "/dev/ttyUSB0",
        "baudrate": 38400,
        "data_bits": 8,
        "parity": "none",
        "stop_bits": 1,
    },
    "motors": {
        "slave_ids": [1, 2],
        "command_ppr": 10000,
        "encoder_ppr": 10000,
    },
    "server": {
        "host": "0.0.0.0",
        "port": 8000,
    },
}


def _normalize_motors(motors: dict) -> dict:
    """Migrate legacy motor1_slave_id/motor2_slave_id keys → slave_ids list, clamp to 1..MAX_MOTORS."""
    ids = motors.get("slave_ids")
    if not ids:
        ids = []
        for key in ("motor1_slave_id", "motor2_slave_id"):
            if key in motors:
                ids.append(motors[key])
        if not ids:
            ids = [1, 2]
    # Dedupe while preserving order, clamp count
    seen = set()
    deduped = []
    for sid in ids:
        sid = int(sid)
        if sid not in seen:
            seen.add(sid)
            deduped.append(sid)
        if len(deduped) >= MAX_MOTORS:
            break
    motors["slave_ids"] = deduped
    # Drop legacy keys
    motors.pop("motor1_slave_id", None)
    motors.pop("motor2_slave_id", None)
    return motors


def load_config() -> dict:
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            cfg = json.load(f)
    else:
        cfg = {k: v.copy() for k, v in DEFAULTS.items()}
    cfg.setdefault("motors", {})
    _normalize_motors(cfg["motors"])
    return cfg


def save_config(cfg: dict):
    if "motors" in cfg:
        _normalize_motors(cfg["motors"])
    with open(CONFIG_PATH, "w") as f:
        json.dump(cfg, f, indent=2)
