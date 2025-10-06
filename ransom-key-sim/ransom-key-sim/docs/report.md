# Relatório do Projeto — Simulação Segura de Ransomware e Keylogger

## 1. Introdução
Este projeto tem objetivo pedagógico: compreender o comportamento e os vetores de ataque de ransomware e keyloggers, sem desenvolvimento de malware real. Foram implementadas simulações não-destrutivas e ferramentas defensivas básicas, além de reflexões sobre mitigação.

## 2. Objetivos
- Demonstrar o fluxo operacional observado em ransomware e keyloggers.
- Implementar simulações seguras em Python.
- Desenvolver ferramentas educativas de defesa (monitor de integridade, backups).
- Documentar práticas e recomendações de defesa.

## 3. Ambiente de teste
- VM: Ubuntu 22.04 LTS (recomendada).
- Isolamento: rede host-only / desconectada.
- Snapshot: criado antes de cada execução.

## 4. Implementações realizadas
### 4.1 Simulador de Ransomware (safe_ransom_simulator.py)
- Cria cópias de arquivos de `test_files/` para `simulated_encrypted/` com extensão `.SIMLOCK`.
- Gera `manifest.json` com lista de arquivos afetados.
- Gera `README_RESCUE.txt` com mensagem educativa.
- **Importante:** arquivos originais **não** são alterados nem removidos.

### 4.2 Alternativa segura ao Keylogger (safe_activity_logger.py)
- GUI (Tkinter) que solicita entrada do usuário e salva o texto em arquivo `.txt`.
- Demonstra fluxo de captura de entrada **consentida** (ex.: formulário de feedback).

### 4.3 Ferramentas de defesa
- **file_integrity_monitor.py:** calcula e salva hashes SHA-256 dos arquivos em `test_files/`.
- **backup_script.py:** copia `test_files/` para `backups/` com timestamp.

## 5. Análise conceitual (alto nível)
### 5.1 Ransomware real (como funciona)
- Vetores comuns: phishing, RDP mal protegido, vulnerabilidades em serviços expostos.
- Etapas: entrada, escalada de privilégios, criptografia dos arquivos, potencial exfiltração, nota de resgate.
- Mitigações: backups isolados, EDR, aplicação de patches, segmentação de rede.

### 5.2 Keylogger real (como funciona)
- Pode utilizar APIs de sistema para interceptar eventos de teclado, hooks globais, ou drivers.
- Riscos: captura contínua de credenciais, exfiltração.
- Mitigações: controle de privilégio, EDR, políticas de execução, educação de usuário.

## 6. Medidas de Defesa e Boas Práticas
- Backups regulares e testados (3-2-1 rule).
- Soluções EDR/antivírus com heurísticas e análise comportamental.
- Monitor de integridade (hashing), detectando alterações não autorizadas.
- Least privilege e segmentação de rede.
- Treinamento de usuários para reconhecer phishing.
- Sandboxing para executar software desconhecido em isolamento.
- Resposta a incidentes e playbooks bem definidos.

## 7. Ética e Legalidade
Desenvolver, testar ou distribuir malware pode ser ilegal e causar danos. Por isso este projeto prioriza simulações inofensivas e a educação para defesa.

## 8. Resultados observados
- Simulação permitiu demonstrar geração de notas de resgate, manifestos e impacto aparente sem perda de dados.
- Ferramentas de defesa detectaram alterações simples (hash changed) quando arquivos de teste foram modificados manualmente.

## 9. Conclusão e aprendizados
O projeto mostra como fluxos e sinais de ataques podem ser replicated... (adicione suas observações pessoais ao relatório antes de submeter ao professor)

## 10. Referências (exemplos)
- NIST Special Publication 800-83 (malware) — para leitura conceitual.
- OWASP — boas práticas de segurança de aplicações.
- Artigos e whitepapers de fornecedores de EDR (ex.: Microsoft Defender for Endpoint).
- Livros: "Practical Malware Analysis" (leitura conceitual).
