"""Calcula indicadores dos testes: taxa de acerto, tempo medio e facilidade media."""
import csv
from pathlib import Path

ARQ = Path(__file__).resolve().parent.parent / "testes" / "registros_testes.csv"

linhas = list(csv.DictReader(open(ARQ, encoding="utf-8")))
if not linhas:
    print("Sem registros ainda. Preencha testes/registros_testes.csv.")
else:
    n = len(linhas)
    acertos = sum(l["acertou_interpretacao"].strip().lower() in ("sim", "s", "1", "true") for l in linhas)
    tempo = sum(float(l["tempo_segundos"]) for l in linhas) / n
    fac = sum(float(l["facilidade_1a5"]) for l in linhas) / n
    print(f"Registros: {n}\nTaxa de acerto: {acertos / n:.0%}\nTempo medio: {tempo:.0f} s\nFacilidade media: {fac:.1f}/5")
