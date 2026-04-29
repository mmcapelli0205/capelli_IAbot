import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

HTML = Path('/root/.openclaw/workspace/out/jornal-ia-2026-04-29.html')
PDF = Path('/root/.openclaw/workspace/out/jornal-ia-2026-04-29.pdf')

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--no-sandbox'])
        page = await browser.new_page()
        await page.goto(HTML.as_uri(), wait_until='networkidle')
        await page.pdf(path=str(PDF), format='A4', print_background=True, margin={"top":"12mm","right":"12mm","bottom":"12mm","left":"12mm"})
        await browser.close()

asyncio.run(main())
