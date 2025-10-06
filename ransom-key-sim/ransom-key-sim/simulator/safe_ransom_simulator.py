#!/usr/bin/env python3
"""
safe_ransom_simulator.py
Simulação NÃO-DESTRUTIVA de comportamento de "ransomware":
- Cria cópias dos arquivos em `test_files/` para `simulated_encrypted/` com extensão .SIMLOCK
- Gera manifest.json e README_RESCUE.txt
ATENÇÃO: execute APENAS em ambiente de testes controlado.
"""

import os
import shutil
import json
import datetime
from pathlib import Path

# Diretórios (relativos ao diretório do projeto)
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TEST_DIR = PROJECT_ROOT / "test_files"
SIM_DIR = PROJECT_ROOT / "simulated_encrypted"

def ensure_dirs():
    TEST_DIR.mkdir(exist_ok=True)
    SIM_DIR.mkdir(exist_ok=True)

def create_sample_files():
    """Cria alguns arquivos de teste se a pasta estiver vazia."""
    if any(TEST_DIR.iterdir()):
        return
    samples = {
        "documento_exemplo.txt": "Este é um arquivo de exemplo para simulação.\n",
        "imagem_exemplo.jpg": "JPEG_SIMULADO_CONTENT\n",
        "planilha_exemplo.csv": "col1,col2\n1,2\n3,4\n"
    }
    for name, content in samples.items():
        with open(TEST_DIR / name, "w", encoding="utf-8") as f:
            f.write(content)

def simulate_encryption():
    manifest = {
        "simulated_at": datetime.datetime.utcnow().isoformat() + "Z",
        "files": []
    }

    for p in sorted(TEST_DIR.iterdir()):
        if p.is_file():
            target = SIM_DIR / (p.name + ".SIMLOCK")
            shutil.copy2(p, target)  # cópia: NÃO remove nem altera o original
            manifest["files"].append({
                "original": str(p.relative_to(PROJECT_ROOT)),
                "simulated": str(target.relative_to(PROJECT_ROOT)),
                "size": p.stat().st_size,
                "simulated_time": datetime.datetime.utcnow().isoformat() + "Z"
            })

    # Mensagem de resgate (educativa)
    with open(SIM_DIR / "README_RESCUE.txt", "w", encoding="utf-8") as f:
        f.write(
            "ATENÇÃO: Esta é uma mensagem de resgate SIMULADA com fins educativos.\n"
            "Nenhum arquivo foi encriptado de fato. Este experimento demonstra fluxo e logs.\n"
        )

    with open(SIM_DIR / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"Simulação completa. Conteúdo criado em: {SIM_DIR}")

if __name__ == "__main__":
    ensure_dirs()
    create_sample_files()
    simulate_encryption()
