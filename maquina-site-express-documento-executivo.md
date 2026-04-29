# Máquina Site Express — Documento Executivo

## 1. Visão do Projeto

**Máquina Site Express** é uma frente comercial automatizada para venda de sites a empresas locais.

A proposta do projeto é construir uma máquina digital capaz de:
- pesquisar empresas por cidade e setor;
- identificar empresas sem site ou com presença digital fraca;
- gerar automaticamente uma prévia visual de site;
- abordar empresas via WhatsApp;
- conduzir a conversa inicial;
- enviar checkout;
- coletar onboarding;
- organizar a produção e a entrega final.

O objetivo não é apenas automatizar mensagens, mas estruturar um sistema comercial previsível, auditável e escalável para aquisição de clientes.

---

## 2. Objetivo Estratégico

Criar um canal de aquisição semi-autônomo para vender sites de entrada com processo padronizado, baixo custo operacional e capacidade de expansão por cidade, nicho e oferta.

### Resultado esperado
- gerar leads com rastreabilidade;
- qualificar oportunidades automaticamente;
- reduzir tempo entre descoberta do lead e proposta comercial;
- aumentar volume de abordagens com controle;
- organizar conversão, pagamento e entrega dentro de um fluxo único.

---

## 3. Escopo Inicial

### Incluído no projeto
- pesquisa e cadastro de leads;
- classificação de oportunidade;
- geração de briefing comercial;
- criação de preview visual inicial;
- copy comercial de abordagem;
- conversa inicial via WhatsApp;
- envio de checkout;
- coleta de onboarding;
- organização da produção final;
- monitoramento operacional;
- auditoria de eventos críticos.

### Fora do escopo neste momento
- disparos massivos sem governança;
- expansão multi-cidade simultânea no MVP;
- venda da oferta “Presença Inteligente”;
- automações sem trilha de auditoria;
- produção final fora de fluxo aprovado.

---

## 4. Estrutura de Responsabilidade

### Bernardo
Responsável por:
- orquestração estratégica;
- desenho operacional;
- protocolos de decisão;
- regras de risco;
- monitoramento;
- definição de fluxo;
- coordenação entre agentes.

### Claude Code
Responsável por:
- construção da base técnica inicial;
- estrutura do banco;
- workflows centrais;
- serviços de integração;
- interfaces internas;
- motor de templates;
- trilha técnica de execução.

**Regra central:** Bernardo pensa e organiza a operação. Claude Code constrói a fundação técnica.

---

## 5. Stack Prevista

- **Supabase** — banco central e persistência operacional
- **n8n** — orquestração de workflows
- **Evolution API** — canal inicial de WhatsApp
- **React / Next.js** — camada de frontend
- **Tailwind + shadcn/ui + Framer Motion** — interface e componentes visuais
- **Templates de site em JSON** — geração semiautomática de previews e entregas
- **Stripe ou Mercado Pago** — pagamento (pendente de decisão)

---

## 6. Planos Comerciais

### 1. Site Express
- **Preço:** R$ 497
- foco em entrada rápida;
- oferta padronizada;
- menor atrito comercial;
- alta velocidade operacional.

### 2. Site Pro
- **Preço:** R$ 1.497
- proposta mais robusta;
- maior personalização;
- potencial de maior margem;
- operação com mais coleta de contexto.

### 3. Presença Inteligente
- previsto para fase futura;
- não vender no início;
- manter fora do fluxo MVP.

---

## 7. Princípios Operacionais

1. Nenhum agente age fora do fluxo aprovado.
2. Nenhum envio em massa sem limite diário.
3. Nenhum contato para leads com `opt_out = true`.
4. Nenhum link deve ser enviado no primeiro contato.
5. Toda origem de lead deve ser registrada.
6. Toda mensagem enviada deve ser registrada.
7. Toda resposta recebida deve ser classificada.
8. Alto risco ou risco financeiro deve ser escalado.
9. Falhou duas vezes, parar e revisar.
10. Produção sem backup, bloquear.

---

## 8. Mapa dos Agentes Internos

### 8.1 Agente Pesquisador de Leads
**Missão:** encontrar empresas por cidade e setor e registrar origem com rastreabilidade.

**Entradas:** cidade, setor, palavras-chave, fontes aprovadas, limite diário.

**Saídas:** lead bruto, origem registrada, evidência mínima, status inicial.

**Regras de segurança:**
- não inventar dados;
- não coletar sem origem;
- não marcar “sem site” sem evidência;
- respeitar o limite diário.

**Parar e pedir revisão quando:**
- fonte for instável;
- houver duplicidade alta;
- dados essenciais estiverem faltando.

**Consulta:** `leads`, `lead_sources`, `lead_search_runs`.

**Erros a reportar:** fonte indisponível, dados incompletos, duplicidade, risco de origem.

---

### 8.2 Agente Classificador de Oportunidade
**Missão:** atribuir score e classificar potencial de conversão.

**Entradas:** lead bruto, sinais de presença digital, critérios de score.

**Saídas:** score, categoria de prioridade, justificativa, status classificado.

**Regras de segurança:**
- não aprovar lead com `opt_out = true`;
- não classificar sem evidência;
- não usar critérios subjetivos sem log.

**Parar e pedir revisão quando:**
- faltar evidência;
- score estiver contraditório;
- lead for sensível ou regulado.

**Consulta:** `leads`, `lead_profiles`, `lead_scores`, `opt_out_registry`.

**Erros a reportar:** ausência de dados, score inconsistente, contato recente, opt-out.

---

### 8.3 Agente Gerador de Briefing
**Missão:** transformar lead qualificado em briefing claro para oferta e preview.

**Entradas:** lead, score, presença digital, plano comercial.

**Saídas:** briefing estruturado, dores prováveis, posicionamento sugerido, lacunas.

**Regras de segurança:**
- separar hipótese de fato;
- não exagerar dor comercial;
- não afirmar o que não foi verificado.

**Parar e pedir revisão quando:**
- houver lacunas críticas;
- marca estiver confusa;
- segmento exigir abordagem especial.

**Consulta:** `leads`, `lead_scores`, `briefings`, `offer_plans`.

**Erros a reportar:** briefing inconsistente, falta de dados, ICP fraco.

---

### 8.4 Agente Criador de Preview
**Missão:** gerar prévia visual com base em template e briefing.

**Entradas:** briefing, template, tokens visuais, assets disponíveis.

**Saídas:** preview, JSON do site, observações de completude.

**Regras de segurança:**
- não publicar em produção;
- não usar assets sem autorização;
- não sair do template aprovado.

**Parar e pedir revisão quando:**
- faltar asset essencial;
- briefing estiver incompleto;
- preview quebrar ou perder consistência.

**Consulta:** `briefings`, `site_templates`, `site_previews`, storage.

**Erros a reportar:** JSON inválido, renderização falha, asset ausente, incompatibilidade de template.

---

### 8.5 Agente Copywriter Comercial
**Missão:** gerar copy de abordagem, follow-up e tratamento de objeções.

**Entradas:** briefing, score, plano, estágio da conversa.

**Saídas:** mensagens de abordagem, follow-ups, respostas por objeção, CTA por etapa.

**Regras de segurança:**
- sem link no primeiro contato;
- sem promessas enganosas;
- sem pressão abusiva;
- sem fugir das políticas de compliance.

**Parar e pedir revisão quando:**
- surgir objeção fora do roteiro;
- a copy ficar agressiva;
- o segmento exigir cuidado adicional.

**Consulta:** `conversation_templates`, `briefings`, `lead_scores`, `campaign_rules`.

**Erros a reportar:** template ausente, CTA errado, copy fora da política.

---

### 8.6 Agente SDR WhatsApp
**Missão:** executar contato inicial e conduzir a conversa comercial dentro do roteiro.

**Entradas:** lead aprovado, copy aprovada, janela de envio, limite diário.

**Saídas:** mensagem registrada, resposta classificada, próximo passo sugerido.

**Regras de segurança:**
- nunca enviar para `opt_out = true`;
- não enviar primeiro contato com link;
- registrar toda mensagem;
- classificar toda resposta;
- respeitar limite diário.

**Parar e pedir revisão quando:**
- houver ameaça, reclamação séria ou pedido jurídico;
- surgir dúvida fora do roteiro;
- houver bloqueio de número ou canal.

**Consulta:** `leads`, `conversations`, `messages`, `campaign_limits`, `opt_out_registry`, Evolution API.

**Erros a reportar:** falha de envio, duplicidade de contato, rate limit, inconsistência de webhook.

---

### 8.7 Agente de Compliance e Opt-out
**Missão:** autorizar ou bloquear ações conforme regras de contato, rastreabilidade e histórico.

**Entradas:** lead, histórico, regras, origem, estado da campanha.

**Saídas:** autorização ou bloqueio, justificativa e trilha de auditoria.

**Regras de segurança:**
- bloqueio absoluto para `opt_out = true`;
- bloquear origem sem rastreabilidade;
- bloquear contato fora da política.

**Parar e pedir revisão quando:**
- houver dúvida jurídica;
- histórico estiver contraditório;
- surgir pedido de exclusão.

**Consulta:** `opt_out_registry`, `messages`, `leads`, `audit_logs`, `campaign_rules`.

**Erros a reportar:** lead sem origem, conflito de histórico, auditoria incompleta.

---

### 8.8 Agente de Pagamento e Onboarding
**Missão:** conduzir pagamento e coleta organizada de onboarding.

**Entradas:** lead pronto, plano escolhido, checkout ativo, formulário de onboarding.

**Saídas:** checkout enviado na etapa certa, pagamento registrado, onboarding iniciado ou concluído.

**Regras de segurança:**
- risco financeiro sempre escala;
- não liberar produção sem confirmação válida;
- não considerar onboarding incompleto como finalizado.

**Parar e pedir revisão quando:**
- houver divergência de valor;
- pagamento estiver pendente ou duplicado;
- surgir disputa ou reembolso.

**Consulta:** `orders`, `payments`, `checkout_sessions`, `onboarding_forms`, `clients`.

**Erros a reportar:** checkout falho, webhook inconsistente, lead sem associação, divergência de plano.

---

### 8.9 Agente de Produção Final
**Missão:** transformar preview e onboarding em entrega final organizada.

**Entradas:** pagamento confirmado, onboarding completo, template, assets finais.

**Saídas:** site final montado, checklist técnico, status de entrega, pendências.

**Regras de segurança:**
- produção sem backup bloqueia;
- não publicar sem validação mínima;
- não inventar conteúdo faltante;
- não expandir escopo sem aprovação.

**Parar e pedir revisão quando:**
- onboarding estiver incompleto;
- assets faltarem;
- houver risco na publicação.

**Consulta:** `projects`, `production_jobs`, `site_templates`, `assets`, repositório frontend, pipeline de deploy.

**Erros a reportar:** build falhou, deploy falhou, layout quebrou, backup inexistente.

---

### 8.10 Agente Supervisor de Campanhas
**Missão:** monitorar volume, risco, desempenho e saúde operacional.

**Entradas:** métricas, histórico de envio, respostas, alertas e estados de campanha.

**Saídas:** painel resumido, alertas, recomendações, pausas automáticas quando necessário.

**Regras de segurança:**
- pausar campanha com sinal de risco;
- respeitar limite diário;
- escalar risco reputacional e financeiro.

**Parar e pedir revisão quando:**
- taxa de bloqueio subir;
- houver falha sistêmica;
- erro repetir duas vezes.

**Consulta:** `campaigns`, `messages`, `conversations`, `payments`, `audit_logs`, `error_logs`.

**Erros a reportar:** queda de entrega, aumento de rejeição, volume anormal, falhas recorrentes.

---

## 9. Fluxo Operacional Completo

### Fase 0 — Governança
1. definir ICP por cidade e setor;
2. definir limite diário;
3. definir janela de envio;
4. aprovar política de opt-out;
5. aprovar templates de mensagem e preview;
6. aprovar trilha de auditoria.

### Fase 1 — Pesquisa
1. pesquisar empresas por cidade e setor;
2. registrar origem e evidência;
3. evitar duplicidade;
4. salvar lead bruto.

### Fase 2 — Classificação
1. analisar presença digital;
2. calcular score;
3. classificar prioridade;
4. bloquear leads fora da regra.

### Fase 3 — Estruturação comercial
1. gerar briefing;
2. criar preview;
3. gerar copy;
4. validar compliance.

### Fase 4 — Abordagem
1. enviar primeira mensagem sem link;
2. registrar envio;
3. classificar resposta;
4. conduzir o próximo passo.

### Fase 5 — Conversão
1. apresentar oferta adequada;
2. enviar checkout na etapa correta;
3. confirmar pagamento;
4. abrir onboarding.

### Fase 6 — Produção e entrega
1. validar onboarding;
2. produzir site final;
3. executar checklist técnico;
4. publicar com segurança.

### Fase 7 — Supervisão
1. monitorar saúde da campanha;
2. acompanhar métricas;
3. detectar riscos;
4. pausar ou ajustar quando necessário.

---

## 10. Matriz de Riscos

### 10.1 Riscos operacionais
- duplicidade de leads;
- erro de classificação;
- preview inconsistente;
- webhook instável;
- falha de rastreabilidade.

**Mitigação:**
- chaves únicas;
- logs obrigatórios;
- revisão por amostra;
- retries controlados;
- trilha de auditoria.

### 10.2 Riscos comerciais
- abordagem fraca;
- timing ruim;
- oferta errada;
- copy desalinhada.

**Mitigação:**
- playbook por etapa;
- revisão de copy;
- testes controlados;
- ICP mais restrito no MVP.

### 10.3 Riscos jurídicos e reputacionais
- contato após opt-out;
- origem obscura de lead;
- excesso de mensagens;
- promessa enganosa.

**Mitigação:**
- compliance obrigatório;
- rastreabilidade da origem;
- limite diário;
- auditoria de mensagens.

### 10.4 Riscos financeiros
- cobrança errada;
- pagamento sem conciliação;
- produção liberada sem pagamento.

**Mitigação:**
- dupla confirmação;
- reconciliação diária;
- estados de pedido obrigatórios;
- escalação em caso de divergência.

### 10.5 Riscos técnicos
- falha no n8n;
- falha na Evolution API;
- falha no Supabase;
- deploy quebrado;
- ausência de backup.

**Mitigação:**
- retries com limite;
- filas mortas;
- alertas;
- backup e rollback.

---

## 11. Checklist de Prontidão

### Estratégia
- [ ] ICP definido
- [ ] cidade piloto definida
- [ ] setor piloto definido
- [ ] oferta inicial validada
- [ ] diferenciação entre Site Express e Site Pro clara

### Compliance
- [ ] política de opt-out definida
- [ ] texto de remoção definido
- [ ] janela de envio definida
- [ ] limite diário definido
- [ ] auditoria mínima aprovada

### Dados e rastreabilidade
- [ ] origem do lead obrigatória
- [ ] log de mensagens obrigatório
- [ ] classificação de resposta obrigatória
- [ ] anti-duplicidade definido
- [ ] status do lead definido

### Comercial
- [ ] mensagem inicial sem link aprovada
- [ ] follow-ups aprovados
- [ ] objeções principais mapeadas
- [ ] CTA por etapa definido

### Técnica
- [ ] arquitetura inicial desenhada
- [ ] schema base definido
- [ ] templates JSON definidos
- [ ] preview pipeline definido
- [ ] checkout decidido
- [ ] backup definido

### Operação
- [ ] responsáveis por etapa definidos
- [ ] critérios de pausa definidos
- [ ] métricas mínimas definidas
- [ ] modelo de relatório diário definido

---

## 12. Regras de Decisão

### Pode seguir automaticamente
- pesquisa dentro da regra;
- classificação com evidência suficiente;
- briefing operacional;
- preview dentro de template;
- abordagem aprovada por compliance.

### Deve escalar
- risco financeiro;
- ambiguidade jurídica;
- bloqueio de canal;
- reclamação séria;
- mudança de preço, oferta ou escopo.

### Deve bloquear
- `opt_out = true`;
- origem não registrada;
- primeiro contato com link;
- limite diário excedido;
- duas falhas consecutivas;
- produção sem backup;
- pagamento inconsistente.

---

## 13. Plano de Monitoramento

### Métricas principais
- leads pesquisados por dia;
- leads qualificados por dia;
- contatos iniciados;
- taxa de resposta;
- taxa de interesse;
- taxa de checkout;
- taxa de pagamento;
- taxa de onboarding concluído;
- taxa de entrega concluída;
- taxa de opt-out;
- taxa de falha de envio.

### Alertas prioritários
- opt-out acima do limite;
- erro recorrente de envio;
- queda brusca de resposta;
- aumento de rejeição;
- webhook de pagamento inconsistente;
- produção parada;
- falta de backup.

### Cadência
- monitoramento por evento;
- resumo operacional duas vezes ao dia;
- relatório diário consolidado;
- revisão semanal de performance.

---

## 14. Modelo de Relatório Diário

# Relatório Diário — Máquina Site Express

**Data:**  
**Cidade/segmento:**  
**Status geral:** saudável / atenção / bloqueado

## 1. Volume
- leads captados:
- leads qualificados:
- leads bloqueados:
- contatos iniciados:
- respostas recebidas:

## 2. Comercial
- interessados:
- checkouts enviados:
- pagamentos confirmados:
- onboardings iniciados:
- onboardings concluídos:

## 3. Operação
- previews gerados:
- produções iniciadas:
- entregas concluídas:
- falhas técnicas:
- falhas de compliance:

## 4. Alertas
- principais erros:
- principais riscos:
- casos para revisão:

## 5. Recomendações
- continuar;
- pausar;
- ajustar copy;
- ajustar ICP;
- revisar limite diário;
- revisar integração.

---

## 15. Dependências do Claude Code

### Construções técnicas necessárias
- schema inicial do Supabase;
- modelagem de estados do lead;
- workflows do n8n;
- integração base com Evolution API;
- frontend interno de preview e operação;
- motor de templates JSON;
- fluxo de checkout e onboarding;
- painel operacional;
- camada de auditoria e logs;
- retries, filas e tratamento de falhas.

### Componentes críticos
1. modelo de dados;
2. máquina de estados do lead;
3. pipeline de preview;
4. motor de mensagens;
5. camada de compliance;
6. conciliação de pagamento;
7. checklist de produção;
8. dashboard operacional.

---

## 16. Decisões Pendentes

Antes da construção técnica, ainda precisam ser definidas:
- Stripe ou Mercado Pago;
- cidade piloto;
- setor piloto;
- limite diário inicial;
- janela de envio;
- critério objetivo de “presença digital fraca”;
- quantidade de templates do MVP;
- se Site Express inclui domínio e hospedagem;
- SLA de entrega por plano.

---

## 17. Recomendação Estratégica de Lançamento

A recomendação é iniciar de forma controlada.

### MVP recomendado
- 1 cidade;
- 1 segmento;
- 1 oferta principal;
- 1 template campeão;
- 1 fluxo de abordagem;
- 1 limite diário conservador.

### Motivo
O maior risco do projeto no início não é técnico. É operacional, reputacional e comercial. Se a máquina nascer sem controle, vira spam. Se nascer com estrutura, vira canal previsível de aquisição.

---

## 18. Conclusão Executiva

Máquina Site Express tem potencial real de se tornar um canal de aquisição escalável para a LOOP, desde que seja construída com:
- governança;
- rastreabilidade;
- controle de risco;
- disciplina operacional;
- separação clara entre automação e decisão.

A prioridade correta agora não é campanha. É fundação.

Primeiro: estrutura.  
Depois: piloto controlado.  
Só então: escala.
