# -*- coding: utf-8 -*-

# Carregar o dataset

import pandas as pd

url = "https://raw.githubusercontent.com/BrennoPaiva2310/python_csv/main/world_alcohol.csv"
df = pd.read_csv(url)
df

# a. Agrupar os dados por tipo de bebidas

grupo_bebidas = df.groupby('Beverage Types')
pd.DataFrame(grupo_bebidas)

# b. Agrupar os dados por Região e por Ano

grupo_regiao_ano = df.groupby(['WHO region', 'Year'])
pd.DataFrame(grupo_regiao_ano)

# c. Seção de Contagens: Contar a ocorrência de Regiões, de Países e a soma da coluna de valores por Bebida

contagem_regiao = df['WHO region'].nunique()
contagem_pais = df['Country'].nunique()
valor_bebida = df.groupby('Beverage Types')['Display Value'].sum()
print('Contagem por região: '+str(contagem_regiao))
print('Contagem por pais: '+str(contagem_pais))
pd.DataFrame(valor_bebida)

# d. Realize análises estatísticas da coluna dos valores: Média, Moda, Mediana, Estatística Descritiva e Gráfico de comparação dos valores agrupados por tipo de bebida.


import seaborn as sns
import matplotlib.pyplot as plt

media = df['Display Value'].mean()

moda = df['Display Value'].mode().values[0]

mediana = df['Display Value'].median()

print('Média:', media)
print('Moda:', moda)
print('Mediana:', mediana)

estatisticas_descritivas = df['Display Value'].describe()
print(pd.DataFrame(estatisticas_descritivas))

agrupado = df.groupby('Beverage Types')['Display Value'].mean().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='Beverage Types', y='Display Value', data=agrupado)
plt.xlabel('Tipo de Bebida')
plt.ylabel('Média dos Valores')
plt.title('Comparação dos Valores por Tipo de Bebida')
plt.show()

# e. Mostre resultados de acordo com alguns critérios

# i. Mostrar a coluna de bebidas do ano de 1985
bebidas_1985 = df[df['Year'] == 1985]['Beverage Types']
print(bebidas_1985)

# ii. Mostrar a coluna de Região com valores acima de 4
regiao_4 = df[df['Display Value'] > 4]['WHO region'].unique()
pd.DataFrame(regiao_4)