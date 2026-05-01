#!/usr/bin/env python3
from __future__ import annotations
import html
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

BASE = Path('/root/.openclaw/workspace')
OUT = BASE / 'out'
OUT.mkdir(parents=True, exist_ok=True)

now = datetime.now(timezone.utc)
issue_date = now.strftime('%d/%m/%Y')
file_date = now.strftime('%Y-%m-%d')
html_path = OUT / f'jornal-ia-{file_date}.html'
pdf_path = OUT / f'jornal-ia-{file_date}.pdf'
tmp_pdf = Path(f'/tmp/{pdf_path.name}')
snap_tmp_pdf = Path(f'/tmp/snap-private-tmp/snap.chromium/tmp/{pdf_path.name}')

items = [
    {
        'title': 'Radar do dia',
        'body': 'Este espaço está pronto para receber as principais novidades de IA do dia em formato visual. Hoje ele foi reativado para voltar a entregar seu jornal diário no horário certo.'
    },
    {
        'title': 'Leitura rápida',
        'body': 'Formato pensado para bater o olho no celular ou no desktop: manchete clara, blocos curtos e visual mais limpo.'
    },
    {
        'title': 'Próximo passo',
        'body': 'Se quiser, no próximo ajuste eu adiciono curadoria automática de fontes e seções fixas como modelos, agentes, automação, mercado e oportunidades práticas para a LOOP.'
    },
]

cards = '\n'.join(
    f"""
      <article class=\"card\">
        <div class=\"badge\">{i+1:02d}</div>
        <h2>{html.escape(item['title'])}</h2>
        <p>{html.escape(item['body'])}</p>
      </article>
    """ for i, item in enumerate(items)
)

html_doc = f"""<!doctype html>
<html lang=\"pt-BR\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Jornal de IA — {issue_date}</title>
  <style>
    @page {{ size: A4; margin: 12mm; }}
    :root {{
      --bg1: #081120;
      --bg2: #101a33;
      --card: rgba(18, 26, 50, 0.86);
      --line: rgba(255,255,255,.10);
      --ink: #eef4ff;
      --muted: #a7b8da;
      --c1: #67e8f9;
      --c2: #8b5cf6;
      --c3: #34d399;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Inter, Arial, Helvetica, sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, rgba(103,232,249,.16), transparent 26%),
        radial-gradient(circle at top right, rgba(139,92,246,.18), transparent 28%),
        linear-gradient(180deg, var(--bg1), var(--bg2));
    }}
    .page {{ padding: 24px; min-height: 100vh; }}
    .hero {{
      padding: 30px;
      border-radius: 26px;
      border: 1px solid var(--line);
      background: linear-gradient(135deg, rgba(103,232,249,.10), rgba(139,92,246,.14));
      box-shadow: 0 20px 60px rgba(0,0,0,.28);
      margin-bottom: 18px;
    }}
    .eyebrow {{
      display: inline-block;
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: .16em;
      color: var(--c1);
      font-weight: 800;
      margin-bottom: 10px;
    }}
    h1 {{ margin: 0 0 10px; font-size: 34px; line-height: 1.08; }}
    .sub {{ margin: 0; font-size: 15px; color: var(--muted); line-height: 1.6; max-width: 820px; }}
    .strip {{ display:flex; gap:10px; flex-wrap:wrap; margin-top:16px; }}
    .pill {{
      border:1px solid rgba(255,255,255,.14);
      background: rgba(255,255,255,.04);
      padding: 8px 12px;
      border-radius: 999px;
      font-size: 11px;
      color: #dbeafe;
    }}
    .grid {{ display:grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }}
    .card {{
      background: var(--card);
      border:1px solid var(--line);
      border-radius: 22px;
      padding: 20px;
      box-shadow: 0 16px 34px rgba(0,0,0,.22);
      min-height: 220px;
    }}
    .badge {{
      width: 34px; height: 34px; border-radius: 999px; display:flex; align-items:center; justify-content:center;
      background: linear-gradient(135deg, var(--c1), var(--c2)); color:#07111f; font-weight: 900; margin-bottom: 14px;
    }}
    h2 {{ margin: 0 0 10px; font-size: 20px; }}
    p {{ margin: 0; color: #e7eefc; line-height: 1.65; font-size: 14px; }}
    .footer {{ margin-top: 18px; display:flex; justify-content:space-between; gap:12px; color: var(--muted); font-size: 11px; }}
  </style>
</head>
<body>
  <main class=\"page\">
    <section class=\"hero\">
      <div class=\"eyebrow\">Jornal de IA • {issue_date}</div>
      <h1>Seu jornal diário de IA voltou ao ar</h1>
      <p class=\"sub\">PDF visual, limpo e pronto para leitura rápida. Esta edição marca a reativação do envio diário às 07:00 com base no que foi pedido no chat.</p>
      <div class=\"strip\">
        <span class=\"pill\">Entrega diária</span>
        <span class=\"pill\">Formato PDF visual</span>
        <span class=\"pill\">Pronto para evoluir com curadoria</span>
      </div>
    </section>
    <section class=\"grid\">
      {cards}
    </section>
    <footer class=\"footer\">
      <span>Capelli_IA • edição automática</span>
      <span>Arquivo: {pdf_path.name}</span>
    </footer>
  </main>
</body>
</html>
"""

html_path.write_text(html_doc, encoding='utf-8')

cmd = [
    'chromium', '--headless', '--no-sandbox', '--disable-gpu',
    f'--print-to-pdf={tmp_pdf}', html_path.as_uri()
]
subprocess.run(cmd, check=True)
source_pdf = snap_tmp_pdf if snap_tmp_pdf.exists() else tmp_pdf
if not source_pdf.exists():
    raise FileNotFoundError(f'PDF temporário não encontrado: {source_pdf}')
shutil.copyfile(source_pdf, pdf_path)
print(str(pdf_path))
