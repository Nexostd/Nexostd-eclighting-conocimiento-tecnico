import openpyxl, collections, sys
SRC, OUT = sys.argv[1], sys.argv[2]
src = openpyxl.load_workbook(SRC, data_only=True, read_only=True)
sheets = {'GR-SIST L50': 'Sistelectric-Genrod', 'NERA L50': 'Sistelectric NERA', 'TECLASTAR L51': 'Teclastar',
          'TECNOCOM L54': 'Tecnocom', 'EXULTT L51': 'Exultt', 'WAGO L4': 'Wago'}
out = openpyxl.Workbook(); out.remove(out.active)
summary = []
for sname, brand in sheets.items():
    rows = [r[:9] for r in src[sname].iter_rows(min_row=1, values_only=True)]
    hi = next(i for i, r in enumerate(rows) if r[0] == 'Referencia')
    hdr = rows[hi]
    fam_idx = hdr.index('Familia') if 'Familia' in hdr else hdr.index('Factura')
    data = [r for r in rows[hi+1:] if r[0] not in (None, '')]
    w = out.create_sheet(brand[:31])
    w.append(['codigo', 'marca_lista', 'descripcion', 'familia_proveedor', 'estado', 'qi_proveedor', 'sufijo_BF'])
    seen = collections.Counter()
    for r in data:
        code = str(r[0]).strip(); seen[code] += 1
        w.append([code, brand, (r[2] or '').strip(), (r[fam_idx] or '') if r[fam_idx] is not None else '',
                  (r[1] or '').strip(), r[3], 'SI' if code.upper().endswith('BF') else ''])
    dups = [c for c, n in seen.items() if n > 1]
    summary.append((brand, len(data), dups, sum(1 for r in data if str(r[0]).upper().endswith('BF'))))
out.save(OUT)
for s in summary: print(s)
