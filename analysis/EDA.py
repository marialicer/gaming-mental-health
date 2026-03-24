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

#%%

## tratando nulos no dataframe

mediana_gpa = df['grades_gpa'].median()

df['grades_gpa'] = df['grades_gpa'].fillna(mediana_gpa)

# %%

median_productivity = df['work_productivity_score'].median()

df['work_productivity_score'] = df['work_productivity_score'].fillna(median_productivity)

# %%

## Análise do Dataset

## Distribuição de tempo de jogo

plt.figure(figsize=(8,5))

sns.histplot(
    df["daily_gaming_hours"],
    kde=True,
    color="#9E219E", 
    edgecolor="black"
)

plt.title("Distribuição de horas diárias de jogo")
plt.xlabel("Tempo diário de jogo")
plt.ylabel("Frequência")

plt.savefig("../img/distribuicao_tempo_jogo.png")

plt.show()

# %%

## Distribuição de tempo de sono

plt.figure(figsize=(8,5))

sns.histplot(
    df["sleep_hours"],
    kde=True,
    color="#ED8726", 
    edgecolor="black"
)

plt.title("Distribuição de horas de sono")
plt.xlabel("Horas de sono")
plt.ylabel("Frequência")

plt.savefig("../img/distribuicao_tempo_sono.png")

plt.show()

# %%

## Distribuição de gênero

plt.figure(figsize=(6,4))
sns.countplot(
    x=df["gender"].map({
        "Male": "Masculino",
        "Female": "Feminino",
        "Other": "Outros"
    }),
    data=df
)

plt.title("Distribuição de Gênero")
plt.xlabel("Gênero")
plt.ylabel("Frequência")

plt.savefig("../img/distribuicao_genero.png")

plt.show()

# %%

## 1. Tempo de jogo x saúde mental

## Mais horas de jogo por dia estão associadas a pior saúde mental e bem-estar?

## 🎭 daily_gaming_hours x mood_state

paleta_de_cores = sns.color_palette("flare", 9)

plt.figure(figsize=(12, 6))

sns.boxplot(
    x=df['mood_state'].map({
        "Withdrawn": "Introspectivo",
        "Restless": "Inquieto",
        "Normal": "Normal",
        "Irritable": "Irritado",
        "Excited": "Animado",
        "Euphoric": "Eufórico",
        "Depressed": "Depressivo",
        "Anxious": "Ansioso",
        "Angry": "Nervoso"
    }),
    y='daily_gaming_hours',
    data=df,
    showfliers=False, 
    order=["Eufórico", "Animado","Normal","Inquieto", 
           "Nervoso", "Irritado", "Ansioso", "Introspectivo", "Depressivo"],
    palette=paleta_de_cores
)

plt.title("Humor x Horas diárias de jogo")
plt.xlabel("Humor")
plt.ylabel("Horas de jogo")

plt.savefig("../img/tempo_jogo_humor.png")

plt.show()


# %%

## 🔁 daily_gaming_hours x mood_swing_frequency

paleta_de_cores = sns.color_palette("Blues", 5)

plt.figure(figsize=(12, 6))

sns.boxplot(
    x=df['mood_swing_frequency'].map({
        "Daily": "Diariamente",
        "Never": "Nunca",
        "Rarely": "Raramente",
        "Sometimes": "Às vezes",
        "Often": "Frequentemente"
    }),
    y='daily_gaming_hours',
    data=df,
    showfliers=False, 
    order=["Nunca", "Raramente", "Às vezes", "Frequentemente", "Diariamente"],
    palette=paleta_de_cores
)

plt.title("Mudança de humor x Horas diárias de jogo")
plt.xlabel("Mudança de humor")
plt.ylabel("Horas de jogo")

plt.savefig("../img/tempo_jogo_mudanca_humor.png")

plt.show()
# %%

## 🧍 daily_gaming_hours x social_isolation_score

plt.scatter(
    df['social_isolation_score'],
    df['daily_gaming_hours'],
    c=df['social_isolation_score'],   # variável que define a cor
    cmap='viridis_r'                    # paleta de cores
)

plt.colorbar(label='Escala de isolamento')

plt.title("Escala de isolamento x Horas diárias de jogo")
plt.xlabel("Escala de isolamento")
plt.ylabel("Horas de jogo")

plt.savefig("../img/tempo_jogo_isolamento.png")

plt.show()
# %%

## 🚫 daily_gaming_hours x withdrawal_symptoms

media = df.groupby('withdrawal_symptoms')['daily_gaming_hours'].mean()

labels = ['Sem sintomas', 'Com sintomas']

cores = ['indianred', 'brown']

plt.bar(labels, media.values, color=cores)

plt.xlabel('Sintomas de abstinência')
plt.ylabel('Horas diárias de jogo (média)')
plt.title('Abstinência x Média de horas diárias de jogo')

for i, value in enumerate(media.values):
    plt.text(i, value + 0.1, f'{value:.1f}', ha='center')

plt.savefig("../img/tempo_jogo_abstinencia.png")

plt.show()
# %%

## 2. Existe um limite “seguro” de horas jogadas?

## A partir de quantas horas por dia os indicadores negativos começam a piorar?

df['faixa_horas'] = pd.cut(
    df['daily_gaming_hours'],
    bins=[0, 2, 4, 6, 8, float('inf')],
    labels=['0-2h', '2-4h', '4-6h', '6-8h', '8h+'],
    include_lowest=True
)

## daily_gaming_hours x social_isolation_score

horas_isolamento = df.groupby('faixa_horas', as_index=False)['social_isolation_score'].mean()

horas_isolamento.head()
# %%

plt.bar(horas_isolamento['faixa_horas'],
        horas_isolamento['social_isolation_score'],
        color=plt.cm.viridis_r(
            horas_isolamento['social_isolation_score'] / horas_isolamento['social_isolation_score'].max()
    )
)

plt.title("Média de isolamento social por faixa de horas jogadas")
plt.xlabel("Faixa de horas jogadas")
plt.ylabel("Score de isolamento social")

for i, value in enumerate(horas_isolamento['social_isolation_score']):
    plt.text(i, value + 0.1, f'{value:.1f}', ha='center')

plt.savefig("../img/limite_tempo_jogo_isolamento.png")

plt.show()
# %%

## daily_gaming_hours x sleep_quality

paleta_de_cores = sns.color_palette("Spectral_r", 5)

sns.violinplot(
    x=df['sleep_quality'].map({
        "Good": "Boa",
        "Fair": "Regular",
        "Poor": "Ruim",
        "Very Poor": "Muito ruim",
        "Insomnia": "Insônia"
    }),
    y='daily_gaming_hours',
    data=df,
    cut=0, 
    order=['Boa', "Regular", "Ruim","Muito ruim", "Insônia"],
    palette=paleta_de_cores
)

plt.title("Horas de jogo x Qualidade do sono")
plt.xlabel("Qualidade do sono")
plt.ylabel("Horas de jogo")

plt.savefig("../img/limite_tempo_jogo_qualidade_sono.png")

plt.show()
# %%

## 3. Sono como variável mediadora

## Jogadores que dormem pior também apresentam piores indicadores de saúde mental?

## sleep_hours x mood_state

paleta_de_cores = sns.color_palette("YlOrBr", 9)

plt.figure(figsize=(12, 6))

sns.boxplot(
    x=df['mood_state'].map({
        "Withdrawn": "Introspectivo",
        "Restless": "Inquieto",
        "Normal": "Normal",
        "Irritable": "Irritado",
        "Excited": "Animado",
        "Euphoric": "Eufórico",
        "Depressed": "Depressivo",
        "Anxious": "Ansioso",
        "Angry": "Nervoso"
    }),
    y='sleep_hours',
    data=df,
    showfliers=False, 
    order=["Eufórico", "Animado","Normal","Inquieto", 
           "Nervoso", "Irritado", "Ansioso", "Introspectivo", "Depressivo"],
    palette=paleta_de_cores
)

plt.title("Humor x Horas de sono")
plt.xlabel("Humor")
plt.ylabel("Horas de sono")

plt.savefig("../img/horas_sono_humor.png")

plt.show()

# %%

## sleep_quality x social_isolation_score

paleta_de_cores = sns.diverging_palette(145, 300, s=60, n=5)

plt.figure(figsize=(12, 6))

sns.boxplot(
    x=df['sleep_quality'].map({
        "Good": "Boa",
        "Fair": "Regular",
        "Poor": "Ruim",
        "Very Poor": "Muito ruim",
        "Insomnia": "Insônia"
    }),
    y='social_isolation_score',
    data=df,
    showfliers=False, 
    order=['Boa', "Regular", "Ruim","Muito ruim", "Insônia"],
    palette=paleta_de_cores
)

plt.title("Qualidade de sono x Score de isolamento social")
plt.xlabel("Qualidade do sono")
plt.ylabel("Score de isolamento social")

plt.savefig("../img/qualidade_sono_isolamento.png")

plt.show()
# %%

## 4. Impacto na vida real
## O comportamento de jogo afeta desempenho acadêmico e produtividade?

## daily_gaming_hours x academic_work_performance

paleta_de_cores = sns.color_palette("vlag", 9)

plt.figure(figsize=(12, 6))

sns.boxplot(
    x=df['academic_work_performance'].map({
        "Good": "Boa",
        "Average": "Mediano",
        "Below Average": "Abaixo da média",
        "Poor": "Ruim",
        "Excellent": "Excelente",
        "Failing": "Reprovado"
    }),
    y='daily_gaming_hours',
    data=df,
    showfliers=False, 
    order=['Excelente','Boa', "Mediano", "Abaixo da média","Ruim", "Reprovado"],
    palette=paleta_de_cores
)

plt.title("Performance acadêmica x Horas de jogo")
plt.xlabel("Performance acadêmica")
plt.ylabel("Horas de jogo")

plt.savefig("../img/performance_academica_tempo_jogo.png")

plt.show()
# %%

## 5. Quem tem maior risco de vício?

## Quais fatores estão mais associados ao risco de dependência em jogos?

df['gaming_addiction_risk_level'].value_counts()

# %%

paleta_de_cores = sns.color_palette("coolwarm", 4)

df['risco_vicio'] = df['gaming_addiction_risk_level'].map({
    "Low": "Baixo",
    "Moderate": "Moderado",
    "High": "Alto",
    "Severe": "Severo"
})

sns.boxplot(
    x= 'risco_vicio',
    y='daily_gaming_hours',
    data=df,
    showfliers=False, 
    order=['Baixo', 'Moderado', 'Alto', "Severo"],
    palette=paleta_de_cores
)

plt.ylabel("Horas de jogo")
plt.xlabel("Risco de vício")
plt.title('Horas jogadas vs risco de vício')

plt.savefig("../img/risco_vicio_tempo_jogo.png")

plt.show()
# %%

df['continued_despite_problems_pt'] = df['continued_despite_problems'].map({
    True: 'Sim',
    False: 'Não'
})

paleta_de_cores_hue = sns.color_palette("YlOrBr_r", 2)

sns.countplot(
    x = 'risco_vicio',
    hue='continued_despite_problems_pt',
    data=df,
    order=['Baixo', 'Moderado', 'Alto', "Severo"],
    palette= paleta_de_cores_hue
)

plt.legend(title='Continua apesar de problemas', labels=['Não', 'Sim'])
plt.ylabel("Continua jogando apesar dos problemas")
plt.xlabel("Risco de vício")
plt.title('Risco de vício x comportamento de continuidade')

plt.savefig("../img/risco_vicio_jogo_continuo.png")

plt.show()

# %%

## comparar médias

df.groupby('risco_vicio')[
    ['daily_gaming_hours',
     'years_gaming',
     'monthly_game_spending_usd',
     'social_isolation_score']
].mean()
#%%

## heatmap de correlação
numeric_df = df.select_dtypes(include=["int64","float64"])

plt.figure(figsize=(12,8))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Heatmap de correlação")

plt.tight_layout()

plt.savefig("../img/heatmap_correlacao.png")

plt.show()
# %%