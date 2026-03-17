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
## descobrir a média de horas jogadas por idade

media_por_idade = df.groupby('age', as_index=False)['daily_gaming_hours'].mean()

media_por_idade.set_index('age', inplace=True)
media_por_idade.head()

# %% 

## definindo a média global

media_global = df['daily_gaming_hours'].mean()
print(media_global)
# %%
## plotar o gráfico horas jogadas x idade

plt.plot(media_por_idade.index, media_por_idade.values, marker='o', color = 'green')

plt.xlabel('Idade')
plt.axhline(media_global, color='sienna', linestyle='--', label=f'Média global: {media_global:.2f}')
plt.ylabel('Média de horas jogadas')
plt.title('Média de horas jogadas por idade')
plt.legend()

## plt.savefig("../img/horas_jogadas_idade.png")

plt.show()
# %%
