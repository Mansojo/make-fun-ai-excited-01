"""Copy the entry image to the output directory.

The image lives beside this file as entry.png; the program writes it to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png outside the sandbox).
Standard library only, deterministic, no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT_DIR.mkdir(parents=True, exist_ok=True)

shutil.copyfile(HERE / "entry.png", OUT_DIR / "entry.png")
