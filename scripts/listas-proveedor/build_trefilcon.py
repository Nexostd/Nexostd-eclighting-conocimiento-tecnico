import openpyxl, re, collections, sys
SRC = sys.argv[1]; OUT = sys.argv[2]
wb = openpyxl.load_workbook(SRC, data_only=True)
ws = wb.worksheets[0]
head = re.compile(r'^\[(?P<code>.+?)/TREFI\]\s*(?P<name>.*)$')
name_re = re.compile(r'^CABLE\s+(?P<tipo>.*?)\s*(?P<cond>\d+)X(?P<sec>[\d.,]+(?:\s*\+\s*N?\s*[\d.,]+)?)\s*(?:MM)?\s*(?P<rest>.*)$')
out = []; problems = []
for i, (raw,) in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
    s = (raw or '').strip()
    m = head.match(s)
    if not m:
        problems.append((i, s)); continue
    # the code is everything before the first "/TREFI", which handles codes like LSOHST3X50/25
    code = m.group('code').strip(); name = m.group('name').strip()
    # codes like "LSOHST3X50/25" appear as [LSOHST3X50/25/TREFI]; rebuild
    if '/' in code: pass
    nm = name_re.match(name)
    if nm:
        tipo = nm.group('tipo').strip(); cond = nm.group('cond'); sec = nm.group('sec').replace(',', '.').strip()
        rest = nm.group('rest').replace('TREF', '').replace('MM','').strip()
        rest = re.sub(r'\s+', ' ', rest)
        color = rest.replace('V/', '').strip()
        otras = ''
    else:
        tipo = cond = sec = color = ''; otras = name; problems.append((i, s))
    out.append([code, s, tipo, cond, sec, color, otras])
codes = [r[0] for r in out]
dups = [c for c, n in collections.Counter(codes).items() if n > 1]
o = openpyxl.Workbook(); w = o.active; w.title = 'Trefilcon'
w.append(['codigo', 'nombre_odoo', 'tipo_cable', 'conductores', 'seccion_mm2', 'color', 'otras_especificaciones'])
for r in out: w.append(r)
o.save(OUT)
print('filas de datos:', len(out), '| codigos duplicados:', dups, '| no parseados:', len(problems))
for p in problems[:10]: print('  revisar:', p)
