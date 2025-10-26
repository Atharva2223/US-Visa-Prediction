# us_visa/logger/__init__.py
import logging
from datetime import datetime
from pathlib import Path

# 1) Resolve base dir safely
try:
    from from_root import from_root  # may be your util or the 'from-root' pkg
    _base = from_root()
except Exception:
    _base = None

# Fallbacks if from_root() is missing/broken/returns None
if not _base:
    _base = Path.cwd()
else:
    _base = Path(_base)  # normalize to Path

# 2) Create logs dir
logs_dir = (_base / "logs").resolve()
try:
    logs_dir.mkdir(parents=True, exist_ok=True)
except Exception as e:
    # Last-ditch fallback to current working dir
    logs_dir = (Path.cwd() / "logs").resolve()
    logs_dir.mkdir(parents=True, exist_ok=True)

# 3) Build log file path
log_file = logs_dir / f"{datetime.now():%m_%d_%Y_%H_%M_%S}.log"

# Helpful one-time prints so you can verify

# 4) Configure logging
logging.basicConfig(
    filename=str(log_file),            # cast to str for Windows compatibility
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
    encoding="utf-8",                  # avoids Unicode issues on Windows
)

logger = logging.getLogger("us_visa")
