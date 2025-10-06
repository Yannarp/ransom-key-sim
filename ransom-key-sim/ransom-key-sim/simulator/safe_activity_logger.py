#!/usr/bin/env python3
"""
safe_activity_logger.py
Aplicativo GUI (Tkinter) que coleta texto de forma consentida e salva em activity_logs/.
Alternativa segura a keyloggers.
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
from pathlib import Path
import datetime

PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "activity_logs"
LOG_DIR.mkdir(exist_ok=True)

def save_text():
    content = text_area.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Aviso", "Nenhum texto para salvar.")
        return
    ts = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    filename = LOG_DIR / f"activity_{ts}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Saved at (UTC): {ts}\n\n")
        f.write(content)
    messagebox.showinfo("Salvo", f"Texto salvo em:\n{filename}")

root = tk.Tk()
root.title("Logger de Atividade (consentido)")

label = tk.Label(root, text="Digite um texto (consentido). Este é um exemplo educativo:")
label.pack(padx=10, pady=(10, 0))

text_area = scrolledtext.ScrolledText(root, width=60, height=15)
text_area.pack(padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(padx=10, pady=(0, 10))

save_btn = tk.Button(btn_frame, text="Salvar", command=save_text)
save_btn.pack(side=tk.LEFT, padx=(0,5))

quit_btn = tk.Button(btn_frame, text="Sair", command=root.destroy)
quit_btn.pack(side=tk.LEFT)

root.mainloop()
