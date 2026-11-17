# Justificativas das recomendações

**Público:** famílias de baixa renda com conta de luz alta. **Necessidade:** reduzir o gasto com banho quente (chuveiro elétrico costuma ser um dos maiores consumidores residenciais; validar com a conta do grupo/entrevistados).

**Período comum de comparação:** 10 anos, mesma necessidade (banho de 4 pessoas, 8 min cada), mesma tarifa.

## Resultados (cenário base, tarifa placeholder R$ 1,00/kWh)

| Alternativa | kWh/mês | Custo/mês | Investimento | Retorno | Custo total em 10 anos |
|---|---|---|---|---|---|
| Base: chuveiro elétrico | 88,0 | R$ 88,00 | — | — | R$ 10.560 |
| A: eficiência (banho mais curto/morno) | 66,0 | R$ 66,00 | R$ 0 | imediato | R$ 7.920 |
| B: aquecedor solar (renovável) | 26,4 | R$ 26,40 | R$ 3.500 | ~66 meses | R$ 7.668 |
| A+B | 19,8 | R$ 19,80 | R$ 3.500 | ~58 meses | R$ 6.876 |

Todos os números acima são **estimativas** e mudam com a tarifa real e as premissas. O arquivo `results/comparacao_banho.csv` traz também os cenários conservador (fração solar 50%) e otimista (85%).

## Leitura dos resultados

- **Custo:** A não exige investimento, então é a primeira recomendação. B exige capital inicial, que pode ser barreira para o público; vale pesquisar condições de financiamento ou programas locais.
- **Viabilidade:** B depende de telhado com insolação, espaço para reservatório e instalação adequada; em moradia alugada pode não ser viável.
- **Impacto ambiental:** a matriz elétrica brasileira já tem fator de emissão baixo, então o CO2 evitado é pequeno (dezenas de kg/ano). O argumento forte de B é financeiro e de redução de consumo, não climático. Não foram contabilizadas emissões de fabricação do equipamento.
- **Limitações:** não considera bandeiras tarifárias, impostos específicos, degradação do equipamento, nem o consumo de outros aparelhos.
