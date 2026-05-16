"""Windows launcher: opens the browser, starts uvicorn. Works both frozen (.exe) and from source.

When PyInstaller freezes this app:
  - The bundled read-only resources (e.g. the `static/` folder) live in sys._MEIPASS.
  - The user-editable config.json lives next to the .exe so they can change motor IDs
    or switch between simulation/hardware without unpacking the bundle.

We export both paths via env vars BEFORE importing the app, so `app.config` and
`app.server` pick them up on first read.
"""

import os
import sys
import threading
import time
import webbrowser
from pathlib import Path


def _resource_root() -> Path:
    """Where bundled read-only assets live (static/, app/)."""
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)  # type: ignore[attr-defined]
    return Path(__file__).resolve().parent


def _writable_root() -> Path:
    """Where user-editable config.json lives — next to the .exe when frozen."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


os.environ.setdefault("PYSIM_RESOURCE_ROOT", str(_resource_root()))
os.environ.setdefault("PYSIM_CONFIG_DIR", str(_writable_root()))

# Import after env vars are set so module-level path constants resolve correctly.
from app.config import load_config  # noqa: E402


def _open_browser_when_ready(url: str, delay: float = 1.5) -> None:
    def _open() -> None:
        time.sleep(delay)
        try:
            webbrowser.open(url)
        except Exception:
            pass

    threading.Thread(target=_open, daemon=True).start()


def main() -> None:
    cfg = load_config()
    host = cfg["server"]["host"]
    port = cfg["server"]["port"]
    browse_host = "127.0.0.1" if host in ("0.0.0.0", "::") else host
    _open_browser_when_ready(f"http://{browse_host}:{port}/")

    import uvicorn

    uvicorn.run("app.server:app", host=host, port=port, reload=False, log_level="info")


if __name__ == "__main__":
    main()
