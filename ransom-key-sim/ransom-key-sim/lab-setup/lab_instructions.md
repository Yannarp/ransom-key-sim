# Instruções para Montar o Laboratório Seguro

**Objetivo:** garantir que todos os experimentos sejam realizados em ambiente controlado e reversível.

## Requisitos mínimos
- Máquina host com VirtualBox ou VMware.
- Imagem de máquina virtual (Ubuntu 22.04 LTS recomendado) ou Windows sandbox.
- Espaço em disco ≳ 10 GB livre.
- Contas locais (não utilize dados sensíveis nem redes corporativas).

## Passos (recomendado)
1. **Criar VM**
   - Alocar 2–4 GB RAM, 2 CPUs, disco 20 GB.
   - Desativar pastas compartilhadas com o host.
2. **Rede**
   - Defina a interface de rede da VM para **Host-only** ou **NAT** sem portas encaminhadas.
   - Melhor prática: desconectar totalmente a VM da internet (air-gapped) enquanto executa experimentos.
3. **Snapshots**
   - Antes de qualquer execução, **crie um snapshot** limpo da VM.
   - Crie snapshots adicionais antes de cada experimento significativo.
4. **Usuários e Permissões**
   - Use uma conta sem privilégios (não root/administrador) para executar scripts.
   - Se precisar de privilégios, use `sudo` apenas quando indispensável.
5. **Pastas**
   - Trabalhe apenas dentro da pasta do projeto (por exemplo `/home/user/ransom-key-sim`).
   - Não use pastas que contenham dados reais ou backups.
6. **Backups**
   - Faça backup do estado da VM (ou snapshot) antes/ depois dos experimentos.
7. **Monitoramento**
   - Habilite logs locais (syslog) e verifique consumo de CPU/disk.
8. **Reversão**
   - Para reverter o sistema, restaure o snapshot previamente salvo.
9. **Ética e Legalidade**
   - Não compartilhe scripts que possam ser usados maliciosamente fora de contexto educacional.
   - Não realize testes em redes alheias, computadores de terceiros ou sistemas de produção.

## Checklist antes de executar qualquer script
- [ ] Snapshot criado
- [ ] Rede isolada (ou desconectada)
- [ ] Pastas de teste criadas (`test_files/`)
- [ ] Usuário sem privilégios
- [ ] Registro de atividades habilitado

## Observações finais
Documente cada passo no relatório (`docs/report.md`) — data, hora, snapshot ID, comandos executados e resultado observado. Isso demonstra responsabilidade e reprodutibilidade.
