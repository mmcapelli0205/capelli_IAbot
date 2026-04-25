from pathlib import Path
text = Path('/root/.openclaw/workspace/out/resumao_prompt_guidance_gpt55.txt').read_text(encoding='utf-8')
out = Path('/root/.openclaw/workspace/out/resumao_prompt_guidance_gpt55.pdf')
lines = []
for raw in text.splitlines():
    if not raw:
        lines.append('')
        continue
    s = raw
    while len(s) > 95:
        cut = s.rfind(' ', 0, 95)
        if cut == -1:
            cut = 95
        lines.append(s[:cut])
        s = s[cut:].lstrip()
    lines.append(s)
pages = [lines[i:i+46] for i in range(0, len(lines), 46)]
objects = []
def add_obj(data: bytes):
    objects.append(data)
    return len(objects)
font_id = add_obj(b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>')
pages_root_id = add_obj(b'')
page_ids = []
content_ids = []
for page in pages:
    content = ['BT', '/F1 11 Tf', '50 790 Td', '14 TL']
    first = True
    for line in page:
        esc = line.replace('\\', r'\\').replace('(', r'\(').replace(')', r'\)')
        if first:
            content.append(f'({esc}) Tj')
            first = False
        else:
            content.append('T*')
            content.append(f'({esc}) Tj')
    content.append('ET')
    stream = '\n'.join(content).encode('latin-1', errors='replace')
    cid = add_obj(b'<< /Length ' + str(len(stream)).encode() + b' >>\nstream\n' + stream + b'\nendstream')
    content_ids.append(cid)
for cid in content_ids:
    pid = add_obj(f'<< /Type /Page /Parent {pages_root_id} 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {cid} 0 R >>'.encode())
    page_ids.append(pid)
objects[pages_root_id - 1] = (f'<< /Type /Pages /Count {len(page_ids)} /Kids [ ' + ' '.join(f'{p} 0 R' for p in page_ids) + ' ] >>').encode()
catalog_id = add_obj(f'<< /Type /Catalog /Pages {pages_root_id} 0 R >>'.encode())
pdf = bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
offsets = [0]
for i, obj in enumerate(objects, start=1):
    offsets.append(len(pdf))
    pdf.extend(f'{i} 0 obj\n'.encode())
    pdf.extend(obj)
    pdf.extend(b'\nendobj\n')
startxref = len(pdf)
pdf.extend(f'xref\n0 {len(objects)+1}\n'.encode())
pdf.extend(b'0000000000 65535 f \n')
for off in offsets[1:]:
    pdf.extend(f'{off:010d} 00000 n \n'.encode())
pdf.extend(f'trailer\n<< /Size {len(objects)+1} /Root {catalog_id} 0 R >>\nstartxref\n{startxref}\n%%EOF\n'.encode())
out.write_bytes(pdf)
print(out)
