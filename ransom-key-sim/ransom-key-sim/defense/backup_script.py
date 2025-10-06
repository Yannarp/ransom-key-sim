#!/usr/bin/env python3
"""
backup_script.py
Copia a pasta test_files/ para backups/ com timestamp.
Uso educativo para demonstrar a importância de backups.
"""

import shutil
from pathlib import Path
import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "test_files"
BACKUPS_DIR = PROJECT_ROOT / "backups"

BACKUPS_DIR.mkdir(exist_ok=True)

def make_backup():
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    dest = BACKUPS_DIR / f"backup_{ts}"
    shutil.copytree(DATA_DIR, dest)
    print(f"Backup criado em: {dest}")

if __name__ == "__main__":
    make_backup()
