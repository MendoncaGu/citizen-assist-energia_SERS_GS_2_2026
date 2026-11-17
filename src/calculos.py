"""Calculos de energia do Citizen Assist AI (desafio de Energia e Sustentabilidade).

Todas as premissas vem de data/premissas.csv, para que o assistente e a
analise usem exatamente os mesmos numeros.
Formula base: E (kWh) = P (kW) x tempo (h) x fator de uso.
"""
import csv
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent


def carregar_premissas(caminho=None):
    caminho = Path(caminho) if caminho else RAIZ / "data" / "premissas.csv"
    with open(caminho, newline="", encoding="utf-8") as f:
        return {l["id"]: {"valor": float(l["valor"]), "tipo": l["tipo"],
                          "unidade": l["unidade"], "fonte": l["fonte_ou_justificativa"]}
                for l in csv.DictReader(f)}


def v(p, chave):
    return p[chave]["valor"]


def kwh_mes(potencia_w, horas_dia, dias=30, fator_uso=1.0):
    return potencia_w / 1000 * horas_dia * fator_uso * dias


def custo_rs(kwh, tarifa):
    return kwh * tarifa


def emissao_kg(kwh, fator):
    return kwh * fator


def consumo_equipamento(p, equipamento):

    dias = v(p, "dias_mes")
    if equipamento == "chuveiro":
        horas = v(p, "pessoas") * v(p, "banho_min") / 60
        return kwh_mes(v(p, "chuveiro_w"), horas, dias)
    if equipamento in ("geladeira", "ar"):
        return kwh_mes(v(p, f"{equipamento}_w"), v(p, f"{equipamento}_horas"),
                       dias, v(p, f"{equipamento}_fator"))
    raise ValueError(f"equipamento desconhecido: {equipamento}")


def comparar_banho(p, tarifa=None, fracao_solar=None, pessoas=None,
                   banho_min=None, potencia_w=None):
    tarifa = tarifa if tarifa is not None else v(p, "tarifa_kwh")
    fs = fracao_solar if fracao_solar is not None else v(p, "b_fracao_solar_base")
    pessoas = pessoas if pessoas is not None else v(p, "pessoas")
    banho_min = banho_min if banho_min is not None else v(p, "banho_min")
    potencia_w = potencia_w if potencia_w is not None else v(p, "chuveiro_w")
    dias, anos = v(p, "dias_mes"), v(p, "horizonte_anos")
    fator = v(p, "fator_emissao")

    base = kwh_mes(potencia_w, pessoas * banho_min / 60, dias)
    red = v(p, "a_reducao_tempo")
    opcoes = [
        ("Base: chuveiro eletrico (situacao atual)", base, 0.0, 0.0),
        ("A: eficiencia (banho mais curto / posicao morna)", base * (1 - red),
         v(p, "a_investimento"), 0.0),
        ("B: aquecedor solar (fonte renovavel)", base * (1 - fs),
         v(p, "b_investimento"), v(p, "b_manutencao_ano")),
        ("A+B: eficiencia + aquecedor solar", base * (1 - red) * (1 - fs),
         v(p, "b_investimento"), v(p, "b_manutencao_ano")),
    ]
    linhas = []
    for nome, kwh, invest, manut in opcoes:
        eco_kwh = base - kwh
        eco_mes = custo_rs(eco_kwh, tarifa) - manut / 12
        payback = (invest / eco_mes) if (invest > 0 and eco_mes > 0) else None
        linhas.append({
            "alternativa": nome,
            "kwh_mes": round(kwh, 1),
            "custo_energia_mes_rs": round(custo_rs(kwh, tarifa), 2),
            "economia_kwh_mes": round(eco_kwh, 1),
            "economia_liquida_mes_rs": round(eco_mes, 2),
            "investimento_rs": invest,
            "payback_meses": round(payback, 1) if payback else None,
            "custo_total_horizonte_rs": round(
                invest + manut * anos + custo_rs(kwh, tarifa) * 12 * anos, 2),
            "co2_evitado_kg_ano": round(emissao_kg(eco_kwh * 12, fator), 1),
        })
    return linhas


def cenarios_b(p):

    saida = []
    for rot, ch in (("conservador", "b_fracao_solar_cons"),
                    ("base", "b_fracao_solar_base"),
                    ("otimista", "b_fracao_solar_otim")):
        for l in comparar_banho(p, fracao_solar=v(p, ch)):
            saida.append({"cenario": rot, **l})
    return saida


def salvar_resultados():
    p = carregar_premissas()
    linhas = cenarios_b(p)
    destino = RAIZ / "results" / "comparacao_banho.csv"
    with open(destino, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=linhas[0].keys())
        w.writeheader()
        w.writerows(linhas)
    return destino


if __name__ == "__main__":
    print("Resultados salvos em", salvar_resultados())
