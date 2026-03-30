# OpenClaw Workspace Backup

## Restore em nova máquina/VPS

1. Instale OpenClaw e Git
2. Clone o repo:
```bash
git clone https://github.com/mmcapelli0205/capelli_IAbot.git /root/.openclaw/workspace
```
3. Ajuste permissões:
```bash
chmod +x /root/.openclaw/workspace/scripts/*.sh
```
4. Reconfigure segredos (não versionados):
   - arquivos `.env`
   - chaves/token locais
5. Reinstale cron:
```bash
crontab -e
```
Adicione:
```
15 3 * * * /root/.openclaw/workspace/scripts/daily-backup.sh >> /root/.openclaw/workspace/logs/daily-backup.log 2>&1
```

## Validação
- `openclaw status`
- confirmar logs do backup
- testar comando manual do script
