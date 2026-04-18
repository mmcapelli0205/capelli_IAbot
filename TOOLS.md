# TOOLS.md — Configurações Técnicas do Bernardo

> Baixo nível: modelos, fallback, timeouts e tarefas especiais.
> Atualizado: Março 2026

---

## 1. MODELOS

### Modelo padrão
```
openai-codex/gpt-5.3-codex
```

### Modelo superior (escalada)
```
openai-codex/gpt-5.4
```
Usar quando: arquitetura complexa, estratégia de cliente, erro em produção.

### Fallback Anthropic
```
anthropic/claude-sonnet-4-6
```
Usar quando: modelo Codex indisponível ou falha de autenticação.

---

## 2. FALLBACK CHAIN POR SEVERIDADE

| Severidade | Modelo | Thinking | Quando usar |
|---|---|---|---|
| Normal | openai-codex/gpt-5.3-codex | OFF | Tarefas do dia a dia |
| Crítico | openai-codex/gpt-5.4 | OFF | Estratégia, arquitetura |
| Produção | openai-codex/gpt-5.4 | ON | Erro em produção ativo |
| Fallback | anthropic/claude-sonnet-4-6 | OFF | Codex indisponível |

---

## 3. THINKING ON — QUANDO ATIVAR

Ativar raciocínio profundo nas seguintes situações:

- Estratégia de negócio (ex: novo produto, precificação, posicionamento)
- Arquiteturas complexas de sistema (ex: multi-agente, integração entre plataformas)
- Erro crítico em produção com causa não óbvia
- Decisão com risco financeiro ou de acesso

**Como ativar:** via controle de sessão — usar `/reasoning` ou override por sessão no OpenClaw.
*(Comando via config não validado nesta versão — verificar na documentação antes de usar)*

---

## 4. TIMEOUT E RETRY PADRÃO

| Configuração | Valor |
|---|---|
| Timeout padrão | 60s |
| Timeout tarefas complexas | 120s |
| Retry automático | 2 tentativas |
| Após 2 falhas | Parar e escalar para Marcio |

---

## 5. ACESSO AO COFRE DO BERNARDO

Credenciais do agente ficam no cofre **"Bernardo - Capelli_IA"** no 1Password.

**Login:**
```bash
eval $(op signin)
```

**Listar itens do cofre:**
```bash
op item list --vault "Bernardo - Capelli_IA"
```

**Buscar item específico:**
```bash
op item get "NOME_DO_ITEM" --vault "Bernardo - Capelli_IA" --reveal
```

---

## 6. GATEWAY — COMANDOS OFICIAIS

**Status:**
```bash
openclaw gateway status
```

**Iniciar como serviço:**
```bash
openclaw gateway start
```

**Parar:**
```bash
openclaw gateway stop
```

**Reiniciar:**
```bash
openclaw gateway restart
```

**Rodar em foreground (debug):**
```bash
openclaw gateway run
```

**Forçar (mata processo existente):**
```bash
openclaw gateway run --force
```

**Verificar saúde:**
```bash
openclaw gateway health
```

**Tunnel SSH (acesso pelo navegador no Windows):**
```bash
ssh -N -L 18789:127.0.0.1:18789 root@69.62.89.29
```

Depois acessar: `http://localhost:18789`

---

## 7. BACKUP

**Script de backup diário:**
```bash
/root/.openclaw/workspace/scripts/daily-backup.sh
```

**Cron configurado:** Todo dia às 03:15 UTC
**Destino:** GitHub — mmcapelli0205/capelli_IAbot

---

## 8. STACK TÉCNICA

| Ferramenta | Uso | Onde |
|---|---|---|
| OpenClaw | Gateway do agente | Servidor Hostinger |
| N8N | Automações | papzinhio.app.n8n.cloud |
| Supabase | Banco de dados | Projetos ativos |
| Z-API | WhatsApp | Integração N8N |
| GPT Maker | Agente WilliAm | Cloud |
| Telegram | Canal do Bernardo | @Capelli_IAbot |
| GitHub | Backup workspace | mmcapelli0205/capelli_IAbot |
| 1Password CLI | Gestão de credenciais | Servidor |

---

*Atualizado: Março 2026*
*Dados sensíveis nunca neste arquivo — somente no .env e 1Password.*

---

## MCP PERMISSIONS

Permitido sem perguntar:

- read only tools
- supabase read
- memory search
- calendar read
- logs

Exige confirmação:

- writes
- automações
- inserts
- tarefas

Proibido sem aprovação:

- delete
- produção crítica
- credenciais
- mensagens externas
