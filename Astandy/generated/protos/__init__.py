from __future__ import annotations

import sys
from pathlib import Path


_PROTO_DIR = str(Path(__file__).resolve().parent)
if _PROTO_DIR not in sys.path:
    sys.path.insert(0, _PROTO_DIR)
