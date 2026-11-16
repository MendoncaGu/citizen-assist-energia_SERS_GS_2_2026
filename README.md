# citizen-assist-energia_SERS_GS_2_2026

**Integrantes:** 

Ângelo Malta Reina - rm 570769

Gustavo Mendonça Duarte - rm 570561

Matheus Carpinheiro Moreno - rm 571770

## Público e problema
Famílias de baixa renda com conta de luz alta. O foco é o **banho quente**: o chuveiro elétrico pesa muito no consumo residencial. O assistente ajuda a estimar o consumo de equipamentos (chuveiro, geladeira, ar-condicionado) e a comparar alternativas.

## Alternativas comparadas (mesma necessidade, mesmo período de 10 anos)
- **Base:** chuveiro elétrico.
- **A — Eficiência:** banhos mais curtos / posição morna (sem custo).
- **B — Aquecedor solar de água (fonte renovável).**
- **A+B.**

## Funcionalidades de energia no assistente
1. Quanto gasta meu equipamento? (kWh, R$ e CO2 por mês)
2. Comparar opções para o banho, incluindo solar (custo, retorno, custo total, CO2 evitado)
3. Dicas de economia
4. Tarifa Social (orientação e onde confirmar)
5. Fontes e limitações


## Como executar
```bash
python3 src/calculos.py        # gera results/comparacao_banho.csv (3 cenários)
python3 src/assistente.py      # assistente de terminal
python3 tests/test_calculos.py # testes unitários
python3 src/indicadores.py     # indicadores dos testes com usuários
```


## Estrutura
- `data/premissas.csv` — todos os dados, com tipo (PUBLICO / ESTIMADO), unidade e fonte
- `src/` — cálculos, assistente, indicadores
- `results/` — comparação gerada
- `docs/justificativas.md` e `docs/referencias.md`
- `testes/` — roteiro, registros e ajustes dos testes com usuários

## Limitações
Valores são **estimativas**, não garantias. A tarifa padrão é um placeholder
