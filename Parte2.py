# -*- coding: utf-8 -*-

# Carregar o dataset
import pandas as pd

url = 'https://raw.githubusercontent.com/BrennoPaiva2310/python-dataset/main/cursos-prouni.csv'
df = pd.read_csv(url)
df

# a. Limpar as colunas de notas substituindo NaN por 0.0
df[['nota_integral_ampla', 'nota_integral_cotas', 'nota_parcial_ampla', 'nota_parcial_cotas']] = df[['nota_integral_ampla', 'nota_integral_cotas', 'nota_parcial_ampla', 'nota_parcial_cotas']].fillna(0.0)
df

# b. Agrupar os dados pelo grau

grupo_grau = df.groupby('grau')
pd.DataFrame(grupo_grau)

# c. Agrupar os dados pelos cursos de Matemática, Medicina e Pedagogia

grupo_cursos = df[df['curso_busca'].isin(['Matemática', 'Medicina', 'Pedagogia'])].groupby('curso_busca')

pd.DataFrame(grupo_cursos)

# d. Agrupar os dados por Estado e obter a média de notas de corte por Estado\

grupo_nota_integral_ampla = df.groupby('uf_busca')['nota_integral_ampla','nota_integral_cotas','nota_parcial_ampla','nota_parcial_cotas'].mean()

pd.DataFrame(grupo_nota_integral_ampla)

# e. Agrupar os dados pelos cursos Tecnológicos

grupo_tecnologico = df[df['grau'] == 'Tecnológico'].groupby('curso_busca')
pd.DataFrame(grupo_tecnologico)

# f. Eliminar a coluna "cidade_filtro" do dataframe

df = df.drop('cidade_filtro', axis=1)
df

# g. Apresentar a média das mensalidades dos cursos de Medicina

media_mensalidades_medicina = df[df['curso_busca'] == 'Medicina']['mensalidade'].mean()

media_mensalidades_medicina

# h. Média das notas de corte dos cursos de tempo integral

cursos_integral = df[df['turno'] == 'Integral']

media_nota_integral_ampla = cursos_integral['nota_integral_ampla'].mean()
media_nota_integral_cotas = cursos_integral['nota_integral_cotas'].mean()
media_nota_parcial_ampla = cursos_integral['nota_parcial_ampla'].mean()
media_nota_parcial_cotas = cursos_integral['nota_parcial_cotas'].mean()

print('Média da nota_integral_ampla:', media_nota_integral_ampla)
print('Média da nota_integral_cotas:', media_nota_integral_cotas)
print('Média da nota_parcial_ampla:', media_nota_parcial_ampla)
print('Média da nota_parcial_cotas:', media_nota_parcial_cotas)

# i. Estatística Descritiva das Notas Integral Ampla dos cursos de Bacharelado

desc_notas_bacharelado = df[(df['grau'] == 'Bacharelado') & (df['turno'] == 'Integral')]['nota_integral_ampla'].describe()
desc_notas_bacharelado

# j. Gráfico comparativo entre o grau dos cursos pelas Notas Integral de Cotas

import matplotlib.pyplot as plt

grau_notas_cotas = df.groupby('grau')['nota_integral_cotas'].mean()

plt.bar(grau_notas_cotas.index, grau_notas_cotas)
plt.xlabel('Grau')
plt.ylabel('Média Nota Integral de Cotas')
plt.title('Comparação de Notas Integral de Cotas por Grau')
plt.show()