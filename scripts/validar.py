#!/usr/bin/env python3
"""Control básico del repositorio de conocimiento ECLIGHTING."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md", "AGENTS.md", "agente/INSTRUCCIONES_TUQUI.md",
    "agente/skill-actual/SKILL.md", "aprendizajes/registro.md",
    "conocimiento/protecciones.md", "pruebas/casos.md",
]
missing = [name for name in required if not (ROOT / name).is_file()]
if missing:
    print("Faltan archivos:", ", ".join(missing))
    sys.exit(1)

prompt = (ROOT / "agente/INSTRUCCIONES_TUQUI.md").read_text(encoding="utf-8")
for term in ("qty_available", "con explicación", "default_code"):
    if term not in prompt:
        print("Falta regla en las instrucciones:", term)
        sys.exit(1)
print("OK: documentos mínimos e instrucciones presentes.")
