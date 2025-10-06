# 🧠 Ransom-Key-Sim — Simulação Segura de Ransomware e Keylogger

Este projeto foi desenvolvido como parte de um desafio educacional sobre **Segurança da Informação**, com o objetivo de **compreender o funcionamento prático de malwares (Ransomware e Keylogger)** e **refletir sobre medidas de defesa e prevenção**.

⚠️ **Atenção:**
Este projeto é **totalmente seguro** e **não causa nenhum dano real**.
Todas as implementações simulam o comportamento de malware **em ambiente controlado**, apenas para **fins educacionais e de pesquisa**.

---

## 🎯 Objetivos de Aprendizagem

* Entender o funcionamento básico de Ransomware e Keylogger simulados em Python.
* Reconhecer como esses malwares exploram vulnerabilidades técnicas e humanas.
* Programar scripts de simulação em ambiente seguro.
* Documentar e refletir sobre medidas de defesa e boas práticas de segurança.
* Utilizar o **GitHub como portfólio técnico**, com versionamento e documentação.

---

## 📂 Estrutura do Projeto

```
ransom-key-sim/
├── README.md
├── LICENSE
├── .gitignore
├── lab-setup/
│   └── lab_instructions.md        → Instruções para criar o ambiente seguro
├── docs/
│   └── report.md                  → Relatório e reflexões sobre segurança
├── simulator/
│   ├── safe_ransom_simulator.py   → Simula criptografia e descriptografia de arquivos
│   └── safe_activity_logger.py    → Simula captura e registro de teclas (keylogger seguro)
├── defense/
│   ├── file_integrity_monitor.py  → Monitora integridade de arquivos
│   └── backup_script.py           → Automatiza backups e prevenção de perdas
└── test_files/
    ├── exemplo1.txt
    └── exemplo2.txt
```

---

## 🧩 Funcionalidades Simuladas

### 🔒 Ransomware Simulado

* Cria arquivos de teste e os **criptografa** usando uma chave local.
* Permite **descriptografar** os arquivos com a chave correta.
* Exibe uma **mensagem educativa de “resgate”** simulada.

### ⌨️ Keylogger Simulado

* Captura e registra teclas digitadas (simulação controlada).
* Armazena logs em um arquivo `.txt`.
* Pode simular envio por e-mail (sem enviar de fato).

### 🛡️ Reflexão sobre Defesa

* Estratégias de prevenção e mitigação:

  * Uso de antivírus e firewall;
  * Execução em sandbox;
  * Backup frequente;
  * Conscientização dos usuários.

---

## 🧠 Requisitos

* **Python 3.9+**
* Bibliotecas:

  * `cryptography`
  * `pynput` (para simulação de keylogger)
  * `smtplib` (para envio simulado de e-mails)

---

## 🚀 Como Executar

1. Crie um ambiente virtual e ative:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
2. Instale dependências:

   ```bash
   pip install cryptography pynput
   ```
3. Execute os scripts em `/simulator` para testar as simulações:

   ```bash
   python simulator/safe_ransom_simulator.py
   python simulator/safe_activity_logger.py
   ```

---

## 🧩 Reflexão Final

A criação desses simuladores reforça a importância de compreender **como ataques reais ocorrem**, para poder **defendê-los de forma eficaz**.
Educar usuários e aplicar boas práticas são as melhores armas contra ameaças digitais.

---

## 👩‍💻 Autora

**Yanna R. Peçanha**
Pós-graduanda em Engenharia de software
GitHub: [@Yannarp](https://github.com/yannap)
