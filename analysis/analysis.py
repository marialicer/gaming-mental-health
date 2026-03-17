# %%
## importando bibliotecas necessárias 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %%

## carregando o df

df = pd.read_csv("C:/Users/alice/OneDrive/Documentos/gaming-mental-health/src/gaming_mental_health.csv")
# %%

## visualizando primeiras linhas do dataset

df.head()
# %%
df.describe()
# %%
df.info()
# %%
## 1.COMPORTAMENTO DO DATASET

## 1.1 quem joga mais? FAIXA ETÁRIA

df['faixa_idade'] = pd.cut( 
    df['age'], 
    bins=[0, 13, 15, 17, 20, 24, 30, 100],
    labels=['até 13 anos', '14-15 anos', '16-17 anos', '18-20 anos', '21-24 anos', '25-30 anos', 'acima de 30 anos'] 
)

media_por_idade = df.groupby('faixa_idade', as_index=False)['daily_gaming_hours'].mean() 

media_por_idade.head(7)

# %%
## plotar o gráfico horas jogadas x idade

plt.barh(
    media_por_idade['faixa_idade'],          # categorias no eixo Y
    media_por_idade['daily_gaming_hours'],   # valores no eixo X
    color='lightgreen'
)

plt.xlabel('Horas jogadas')
plt.ylabel('Faixa de idade')
plt.title('Quais faixas etárias mais jogam?')

for i, value in enumerate(media_por_idade['daily_gaming_hours']):
    plt.text(value + 0.1, i, f'{value:.1f}', va='center')

plt.xlim(0, max(media_por_idade['daily_gaming_hours']) + 1)
plt.tight_layout()

plt.savefig("../img/horas_jogadas_idade.png")

plt.show()

# %%

## 1.2 quem joga mais? GÊNERO




# %%

# 2. GAMING vs saúde mental

## 2.1 quem joga mais dorme menos?

df['faixa_jogo'] = pd.cut(
    df['daily_gaming_hours'],
    bins=[0, 1, 2, 3, 5, 10],
    labels=['0-1h', '1-2h', '2-3h', '3-5h', '5h+']
)

sono_horas_jogadas = df.groupby('faixa_jogo', as_index=False)['sleep_hours'].mean()

sono_horas_jogadas.head()
# %%

## plotar o gráfico horas jogadas x sono

plt.bar(
    sono_horas_jogadas['faixa_jogo'],
    sono_horas_jogadas['sleep_hours'],
    color='purple'
)

plt.xlabel('Faixa de horas de jogo')
plt.ylabel('Quantidade de horas de sono')
plt.title('Pessoas que jogam mais dormem menos?')

for i, value in enumerate(sono_horas_jogadas['sleep_hours']):
    plt.text(i, value + 0.1, f'{value:.1f}', ha='center')

plt.savefig("../img/sono_horas_jogadas.png")

plt.show()
# %%

