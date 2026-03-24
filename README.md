# 🎮 Gaming \& Mental Health Analysis



Análise exploratória de dados (EDA) sobre a relação entre tempo de jogo, saúde mental, sono e impactos na vida real, com foco em identificar padrões de comportamento e possíveis riscos associados ao uso excessivo de jogos.



---



## Objetivo do Projeto



Investigar como o tempo gasto em jogos pode influenciar:



- Saúde mental (humor, ansiedade, depressão)
- Qualidade e duração do sono
- Isolamento social
- Desempenho acadêmico e produtividade
- Risco de vício em jogos

---


## Este projeto busca responder:

- Mais horas de jogo estão associadas a pior saúde mental?
- Existe um “limite seguro” de horas jogadas por dia?
- O sono atua como variável mediadora da saúde mental?
- O comportamento de jogo impacta estudo e trabalho?
- Quais fatores estão mais associados ao risco de vício?

---

## Dataset

- Fonte: Kaggle
- Tema: Gaming and Mental Health
- Dados incluem:
- Tempo diário de jogo
- Qualidade e horas de sono
- Estado emocional
- Isolamento social
- Produtividade e desempenho acadêmico
- Indicadores de dependência em jogos

---

## Tecnologias Utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Tratamento de Dados

- Preenchimento de valores nulos com mediana:

grades_gpa
work_productivity_score

- Padronização e tradução de categorias (ex: humor, qualidade do sono)

- Criação de variáveis derivadas:

Faixas de horas jogadas (faixa_horas)
Tradução de variáveis booleanas

---

## Análises Realizadas

1. Distribuições

- Distribuição de tempo de jogo

![Distribuição de tempo de jogo](img/distribuicao_tempo_jogo.png)

📌 A maior parte dos jogadores, joga de 4 a 8 horas por dia, com uma média total de 6 horas diárias. Há jogadores que chegam a passar 15h+ jogando.

- Distribuição de tempo de sono

![Distribuição de tempo de sono](img/distribuicao_tempo_sono.png)

📌 A distribuição de sono mostra que a maior parte dos jogadores dorme menos de 7 horas por noite. O terceiro quartil (75%) está em aproximadamente 6,6 horas, indicando que apenas uma pequena parcela atinge níveis mais elevados de descanso.

- Distribuição de gênero

📌 A maior parte dos jogadores do conjunto de dados pertence ao sexo masculino, já pessoas do gênero feminino passam dos 30%.

2. 
