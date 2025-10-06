#!/usr/bin/env python3
"""
file_integrity_monitor.py
Calcula SHA-256 dos arquivos em test_files/ e salva em defense/hashes.json.
Também pode comparar com hashes existentes para detectar alterações.
"""

import hashlib
import json
from pathlib import Path
import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "test_files"
DEF_DIR = PROJECT_ROOT / "defense"
HASH_FILE = DEF_DIR / "hashes.json"

DEF_DIR.mkdir(exist_ok=True)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def compute_hashes():
    hashes = {}
    for p in sorted(DATA_DIR.iterdir()):
        if p.is_file():
            hashes[str(p.relative_to(PROJECT_ROOT))] = {
                "hash": sha256(p),
                "size": p.stat().st_size,
                "mtime": datetime.datetime.utcfromtimestamp(p.stat().st_mtime).isoformat() + "Z"
            }
    return hashes

def load_existing():
    if HASH_FILE.exists():
        with open(HASH_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, "w", encoding="utf-8") as f:
        json.dump(hashes, f, indent=2)
    print(f"Hashes salvos em: {HASH_FILE}")

def compare_hashes(old, new):
    alerts = []
    for path, info in new.items():
        if path not in old:
            alerts.append(f"NOVO: {path}")
        elif old[path]["hash"] != info["hash"]:
            alerts.append(f"ALTERADO: {path}")
    for path in old:
        if path not in new:
            alerts.append(f"REMOVIDO: {path}")
    return alerts

if __name__ == "__main__":
    new_hashes = compute_hashes()
    old_hashes = load_existing()
    alerts = compare_hashes(old_hashes, new_hashes)
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    if alerts:
        print("ALERTAS DETECTADOS:")
        for a in alerts:
            print(" -", a)
    else:
        print("Nenhuma alteração detectada.")
    # salvar novo estado (para fins didáticos)
    save_hashes(new_hashes)
