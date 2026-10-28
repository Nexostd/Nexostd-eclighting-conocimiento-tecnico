#!/usr/bin/env python3
"""Buscador textual local, sin dependencias externas."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
query = " ".join(sys.argv[1:]).strip().casefold()
if not query:
    print('Uso: python scripts/buscar.py "diferencial selectivo"')
    sys.exit(1)

results = []
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        continue
    for number, line in enumerate(text.splitlines(), 1):
        if query in line.casefold():
            results.append((str(path.relative_to(ROOT)), number, line.strip()[:220]))
for path, line, text in results[:30]:
    print(f"{path}:{line}: {text}")
print(f"Coincidencias: {len(results)} (se muestran hasta 30).")
