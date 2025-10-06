# Simulação Segura de Ransomware e Keylogger (Projeto Educativo)

**Resumo**
Repositório educativo que implementa simulações **não-destrutivas** de comportamento observado em malwares (ransomware e keylogger) e ferramentas defensivas básicas. O objetivo é didático: entender fluxos, logs e estratégias de defesa sem produzir código malicioso.

**Aviso de segurança (LEIA ANTES DE USAR)**
- **Não** execute estes scripts em sua máquina principal. Use uma **VM isolada** ou ambiente de laboratório conforme `lab-setup/lab_instructions.md`.
- Os scripts são projetados para **não** encriptar, não exfiltrar dados e não capturar teclas globalmente. Eles apenas simulam comportamentos por meio de cópias, manifestos e interfaces consentidas.
- Não compartilhe código fora de contextos educacionais controlados.

## Estrutura do repositório
```
ransom-key-sim/
├─ README.md
├─ LICENSE
├─ lab-setup/
│  └─ lab_instructions.md
├─ simulator/
│  ├─ safe_ransom_simulator.py
│  └─ safe_activity_logger.py
├─ defense/
│  ├─ file_integrity_monitor.py
│  └─ backup_script.py
├─ docs/
│  └─ report.md
├─ test_files/
│  └─ (arquivos de exemplo gerados automaticamente)
└─ .gitignore
```

## Como usar (fluxo rápido)
1. Clone o repositório na VM de testes.
2. Abra um terminal dentro da VM (diretório do projeto).
3. Gere arquivos de teste (ex.: crie alguns `.txt` em `test_files/` ou execute o script do simulador que já gera amostras).
4. Execute `python3 simulator/safe_ransom_simulator.py` para ver a simulação. Verifique `simulated_encrypted/`.
5. Execute `python3 defense/file_integrity_monitor.py` para gerar `defense/hashes.json`.
6. Faça um backup com `python3 defense/backup_script.py`.
7. Teste a interface consentida: `python3 simulator/safe_activity_logger.py`.

## Recomendação de apresentação ao professor
- Inclua o arquivo `docs/report.md` (PDF opcional).
- Demonstre a simulação em vídeo curto (screen recording) na VM isolada.
- Explique a razão ética por trás de não criar malware real e as medidas defensivas implementadas.

## Licença
Use a LICENSE (ex.: MIT) para código educativo. Veja `LICENSE`.
