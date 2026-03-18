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

plt.xlabel('Média de horas jogadas')
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

media_por_sexo = df.groupby('gender', as_index=False)['daily_gaming_hours'].mean() 

media_por_sexo.head()

# %%
plt.bar(
    media_por_sexo['gender'],
    media_por_sexo['daily_gaming_hours'],
    color='blue'
)

plt.xlabel('Gênero')
plt.ylabel('Média de horas jogadas')
plt.title('Qual gênero joga mais?')

for i, value in enumerate(media_por_sexo['daily_gaming_hours']):
    plt.text(i, value + 0.1, f'{value:.1f}', ha='center')

plt.savefig("../img/horas_jogadas_genero.png")

plt.show()
#%%

media_jogo_dia = df['daily_gaming_hours'].mean()

print (media_jogo_dia)

# %%
## 1.3 Quantas horas por dia as pessoas jogam?

plt.title('Quantas horas por dia as pessoas jogam?')
plt.xlabel('Horas de jogo')
plt.ylabel('Frequência Absoluta')
plt.hist(df['daily_gaming_hours'], rwidth=0.9, color= 'indianred', edgecolor = 'black')


plt.savefig("../img/horas_jogo_dia.png")

plt.show()


# %%

# 2. GAMING vs estilo de vida

## 2.1 quem joga mais dorme menos?

df['faixa_jogo'] = pd.cut(
    df['daily_gaming_hours'],
    bins=[0, 1, 2, 3, 5, 10, float('inf')],
    labels=['0-1h', '1-2h', '2-3h', '3-5h', '5-10h', '10h+'],
    include_lowest=True
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

## 2.2 Jogar mais afeta a qualidade de sono?

paleta_de_cores = ['#2ecc71', '#a3e635', '#facc15', '#fb923c', '#ef4444']

sns.boxplot(
    x=df['sleep_quality'].map({
        "Good": "Boa",
        "Fair": "Regular",
        "Poor": "Ruim",
        "Very Poor": "Muito ruim",
        "Insomnia": "Insônia"
    }),
    y='daily_gaming_hours',
    data=df,
    showfliers=False, 
    order=['Boa', "Regular", "Ruim","Muito ruim", "Insônia"],
    palette=paleta_de_cores
)

plt.title("Jogar mais afeta a qualidade do sono?")
plt.xlabel("Qualidade do sono")
plt.ylabel("Horas de jogo")

plt.savefig("../img/qualidade_sono.png")

plt.show()

# %%

## 2.3 Pessoas com mais tempo offline são mais felizes?

## Transformando o humor em uma escala de felicidade

df['happiness_score'] = df['mood_state'].map({
    "Depressed": 'Baixo',
    "Withdrawn": 'Baixo',
    "Anxious": 'Baixo',
    "Irritable": 'Baixo',
    "Angry": "Baixo",
    "Restless": 'Médio',
    "Normal": 'Médio',
    "Excited": 'Alto',
    "Euphoric": 'Alto'
})

#%%

tempo_off = df.groupby('happiness_score', as_index=False)['face_to_face_social_hours_weekly'].mean()
tempo_off.head()

# %%

tempo_off = df.groupby('happiness_score')['face_to_face_social_hours_weekly'].mean()

plt.bar(tempo_off.index, tempo_off.values, color='orange')

plt.xlabel('Nível de felicidade')
plt.ylabel('Tempo offline (média)')
plt.title('Mais tempo offline está associado à felicidade?')

for i, value in enumerate(tempo_off.values):
    plt.text(i, value + 0.1, f'{value:.1f}', ha='center')

plt.savefig("../img/tempo_off_felicidade.png")

plt.show()

# %%
