from calculos import (carregar_premissas, v, kwh_mes, custo_rs, emissao_kg,
                      consumo_equipamento, comparar_banho)

AVISO = ("AVISO: este assistente NAO e um canal oficial. Os valores sao "
         "ESTIMATIVAS baseadas em premissas (data/premissas.csv), nao garantias "
         "de economia. Confira sua conta de luz e orcamentos reais.")

REFERENCIAS = [
    "Fator de emissao do SIN: MCTI (media 2023 = 38,5 kgCO2/MWh).",
    "Tarifas e Tarifa Social: ANEEL (aneel.gov.br) e sua distribuidora.",
    "Potencias de equipamentos: etiqueta ENCE/Procel e manual do fabricante.",
    "Detalhes completos: docs/referencias.md",
]


def pedir_numero(texto, minimo, maximo, padrao=None, tentativas=3):

    for _ in range(tentativas):
        dica = f" [Enter = {padrao}]" if padrao is not None else ""
        bruto = input(f"{texto}{dica}: ").strip().replace(",", ".")
        if bruto == "" and padrao is not None:
            return float(padrao)
        try:
            valor = float(bruto)
        except ValueError:
            print("  Entrada invalida: digite apenas numeros (ex.: 5500 ou 0,5).")
            continue
        if not (minimo <= valor <= maximo):
            print(f"  Valor fora do intervalo esperado ({minimo} a {maximo}).")
            continue
        return valor
    print("  Nao consegui entender. Voltando ao menu.")
    return None


def _fmt(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def opcao_equipamento(p):
    print("\nQual equipamento? 1) Chuveiro  2) Geladeira  3) Ar-condicionado  4) Outro")
    esc = input("Escolha: ").strip()
    tarifa = pedir_numero("Tarifa em R$/kWh (veja na sua conta)", 0.1, 5, v(p, "tarifa_kwh"))
    if tarifa is None:
        return
    if esc in ("1", "2", "3"):
        nome = {"1": "chuveiro", "2": "geladeira", "3": "ar"}[esc]
        kwh = consumo_equipamento(p, nome)
        premissa = "dados padrao (estimados) do arquivo de premissas"
    elif esc == "4":
        w = pedir_numero("Potencia em watts (etiqueta do aparelho)", 1, 10000)
        h = pedir_numero("Horas de uso por dia", 0, 24)
        if w is None or h is None:
            return
        kwh, premissa = kwh_mes(w, h, v(p, "dias_mes")), "valores informados por voce"
    else:
        print("  Opcao invalida.")
        return
    print(f"\nConsumo estimado: {_fmt(kwh)} kWh/mes  |  Custo: R$ {_fmt(custo_rs(kwh, tarifa))}/mes")
    print(f"CO2 associado: {_fmt(emissao_kg(kwh, v(p, 'fator_emissao')))} kg/mes")
    print(f"Base: {premissa}. Calculo: P(kW) x horas x dias x fator de uso.")


def opcao_comparar(p):
    print("\nComparar opcoes para o BANHO QUENTE (mesmo periodo de "
          f"{int(v(p, 'horizonte_anos'))} anos).")
    pessoas = pedir_numero("Quantas pessoas tomam banho por dia", 1, 15, v(p, "pessoas"))
    minutos = pedir_numero("Minutos por banho", 1, 60, v(p, "banho_min"))
    tarifa = pedir_numero("Tarifa em R$/kWh", 0.1, 5, v(p, "tarifa_kwh"))
    if None in (pessoas, minutos, tarifa):
        return
    linhas = comparar_banho(p, tarifa=tarifa, pessoas=pessoas, banho_min=minutos)
    print()
    for l in linhas:
        pb = f"{l['payback_meses']:.0f} meses" if l["payback_meses"] else "sem investimento"
        print(f"- {l['alternativa']}\n    {_fmt(l['kwh_mes'])} kWh/mes | R$ {_fmt(l['custo_energia_mes_rs'])}/mes"
              f" | investimento R$ {_fmt(l['investimento_rs'])} | retorno: {pb}"
              f" | custo total em {int(v(p, 'horizonte_anos'))} anos: R$ {_fmt(l['custo_total_horizonte_rs'])}")
    print("\nLimitacoes: a fracao solar assumida e "
          f"{int(v(p, 'b_fracao_solar_base') * 100)}% (pode variar de "
          f"{int(v(p, 'b_fracao_solar_cons') * 100)}% a {int(v(p, 'b_fracao_solar_otim') * 100)}% "
          "conforme regiao, estacao e dimensionamento). Custo do aquecedor e estimado: "
          "peca orcamentos. O CO2 evitado e pequeno porque a matriz eletrica brasileira ja e "
          "majoritariamente renovavel; o principal ganho e financeiro.")


def opcao_dicas():
    print("\nDicas de uso consciente (valem para qualquer residencia):")
    print("- Chuveiro: banhos mais curtos e posicao 'verao/morna' sempre que possivel.")
    print("- Geladeira: borrachas de vedacao em bom estado e longe de fontes de calor.")
    print("- Ar-condicionado: filtro limpo e temperatura moderada; prefira modelos com etiqueta A.")
    print("- Procure o selo Procel/etiqueta ENCE ao trocar eletrodomesticos.")
    print("O quanto isso economiza depende do seu caso: use as opcoes 1 e 2 para estimar.")


def opcao_tarifa_social():
    print("\nTarifa Social de Energia Eletrica: familias de baixa renda inscritas no CadUnico "
          "podem ter desconto na conta.")
    print("As regras mudam: confirme condicoes e como solicitar na sua distribuidora ou em "
          "aneel.gov.br. Este assistente nao e canal oficial.")


def menu():
    print("=== Citizen Assist AI - Energia para sua casa ===")
    print(AVISO)
    p = carregar_premissas()
    while True:
        print("\n1) Quanto gasta meu equipamento?\n2) Comparar opcoes para o banho (inclui solar)"
              "\n3) Dicas de economia\n4) Tarifa Social\n5) Fontes e limitacoes\n0) Sair")
        esc = input("Escolha: ").strip()
        if esc == "1":
            opcao_equipamento(p)
        elif esc == "2":
            opcao_comparar(p)
        elif esc == "3":
            opcao_dicas()
        elif esc == "4":
            opcao_tarifa_social()
        elif esc == "5":
            print("\n" + AVISO + "\nFontes:")
            for r in REFERENCIAS:
                print(" -", r)
        elif esc == "0":
            print("Ate logo!")
            break
        else:
            print("Opcao invalida. Digite um numero de 0 a 5.")


if __name__ == "__main__":
    try:
        menu()
    except (EOFError, KeyboardInterrupt):
        print("\nEncerrado.")
