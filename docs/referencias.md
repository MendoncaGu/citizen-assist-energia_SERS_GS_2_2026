# Referências

Fontes consultadas até 16/11/2026. **Confirmem cada link/valor antes de entregar** e atualizem a data de acesso.

| Dado | Fonte | Observação |
|---|---|---|
| Fator de emissão do SIN (2023): 38,5 kgCO2/MWh (0,0385 tCO2/MWh) | MCTI — "Fator de emissão de CO2 na geração de energia elétrica no Brasil em 2023 é o menor em 12 anos" (gov.br/mcti, notícia de fev/2024) | Usado em `data/premissas.csv`. Atualizar para o ano mais recente. Em abril/2025 o fator mensal foi 28,9 kgCO2/MWh (MCTI, via Canal Solar). |
| Reajustes tarifários 2026 (ex.: Enel SP, +10,18% médio, vigência 4/7/2026) | ANEEL, via imprensa (Cenário Energia, Gazeta SP) | Mostra que a tarifa muda todo ano; **a tarifa por kWh do grupo deve vir da conta de luz / aneel.gov.br**. |
| Tarifa Social (CadÚnico: até 80 kWh/mês com desconto de 100%, segundo reportagem sobre a Enel Ceará, abr/2026) | O POVO (mais.opovo.com.br) | Regras mudam; confirmar na ANEEL/distribuidora antes de afirmar no assistente. |
| Potência de equipamentos | Etiqueta ENCE/Procel (Inmetro/Eletrobras) e manual do fabricante | **A consultar pelo grupo**: anexar prints das etiquetas usadas. |
| Custo/desempenho de aquecedor solar | Orçamentos locais (mín. 3) e ABRAVA/Procel | **A consultar pelo grupo**: os valores atuais em `premissas.csv` são ESTIMADOS. |

## O que ainda é estimativa (não é dado público verificado)

Tarifa (placeholder R$ 1,00/kWh), hábitos de banho, potências padrão, fração solar, investimento e manutenção do aquecedor. Todos aparecem como `ESTIMADO` em `data/premissas.csv`.
