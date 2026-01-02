# 1. INSTALAÇÃO E IMPORTAÇÃO DE BIBLIOTECAS

# Instala bibliotecas no Google Colab
# !pip install pandas matplotlib numpy seaborn
# !pip install polars

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Permite mostrar até 100 colunas no DataFrame
#pd.set_option('display.max_columns', 100)

# 2. LEITURA E INSPEÇÃO INICIAL DOS DADOS

# Lê o arquivo CSV
df = pd.read_csv('./dados_enem_2021_BA.csv')

# Retorna (linhas, colunas)
df.shape

# Mostra as 5 primeiras linhas
df.head()

# Mostra as 10 primeiras linhas
df.head(n=10)

# Mostra as 5 últimas linhas
df.tail()

# Mostra as 10 últimas linhas
df.tail(n=10)

# Informações gerais do dataset:
# - tipos das colunas
# - valores não nulos
# - uso de memória
df.info()

# Lista os nomes das colunas
df.columns

# Estatísticas descritivas:
# média, mediana, quartis, mínimo e máximo
df.describe()
df.describe().transpose()

# Quantidade de valores únicos por coluna
df.nunique()


# ============================================================
# 3. SELEÇÃO DE COLUNAS
# ============================================================

# Seleção de uma coluna (duas formas)
df['TP_ESCOLA']
df.TP_ESCOLA

# Seleção de múltiplas colunas
df[['TP_SEXO', 'TP_ESCOLA']]

# Seleção por nome usando .loc
df.loc[:, 'TP_SEXO']
df.loc[:, ['TP_SEXO', 'TP_ESCOLA']]

# Seleção por posição usando .iloc
df.iloc[:, 0]
df.iloc[0:5, 0]

# Seleciona colunas numéricas
df.select_dtypes(include=[int, float])

# Seleciona colunas categóricas (object / string)
df.select_dtypes(include=object)


# 4. FILTRO DE DADOS

# Filtro usando query (condição em string)
df.query('TP_SEXO == "M"')

# AND (&)
df.query('(TP_SEXO == "M") & (IN_TREINEIRO == 1)')

# OR (|)
df.query('(TP_SEXO == "M") | (IN_TREINEIRO == 1)')

# Filtro usando máscara booleana
df[df.TP_SEXO == "M"]

# Filtro com mais de uma condição
df[(df.TP_SEXO == "M") & (df.IN_TREINEIRO == 1)]

# Detecta valores ausentes
df.isna()
df.notna()

# Verifica pertencimento
df.NO_MUNICIPIO_PROVA.isin(['Salvador', 'Itabuna'])

# Negação com ~
df[~df.NO_MUNICIPIO_PROVA.isin(['Salvador'])]


# 5. AGREGAÇÕES ESTATÍSTICAS

# Média
df.NU_NOTA_MT.mean()

# Mediana
df.NU_NOTA_MT.median()

# Mínimo
df.NU_NOTA_MT.min()

# Máximo
df.NU_NOTA_MT.max()

# Desvio padrão
df.NU_NOTA_MT.std()

# Variância
df.NU_NOTA_MT.var()

# Aplica várias agregações ao mesmo tempo
df.NU_NOTA_MT.agg([np.min, np.mean, np.median, np.max])

# Retorna índice do maior valor
df.NU_NOTA_MT.idxmax()

# Retorna índice do menor valor
df.NU_NOTA_MT.idxmin()

# Recupera a linha do aluno com maior nota
df.iloc[df.NU_NOTA_MT.idxmax()]

# Axis:
# axis=0 → colunas
# axis=1 → linhas

# 6. TRATAMENTO DE VALORES AUSENTES (MISSING)

# Cria uma cópia do DataFrame
df_copy = df.copy()

# Seleciona colunas de provas
provas = df.columns[
    (df.columns.str.contains('NOTA')) &
    (~df.columns.str.contains('COMP'))
].tolist()

# Calcula média das provas por aluno
df_copy['MEDIA_GERAL'] = df[provas].mean(axis=1)

# Imputação de missing com valor simbólico
df_copy['MEDIA_GERAL'].fillna(-1)

# Imputação pela média
df_copy['MEDIA_GERAL'].fillna(df_copy['MEDIA_GERAL'].mean())

# Imputação pela mediana
df_copy['MEDIA_GERAL'].fillna(df_copy['MEDIA_GERAL'].median())

# 7. AGRUPAMENTO (GROUPBY)

# Distribuição de frequência por gênero
df.TP_SEXO.value_counts()

# Contagem por grupo
df.groupby('TP_SEXO')['NU_INSCRICAO'].count()

# Média por tipo de escola
df.groupby('TP_ESCOLA')['NU_NOTA_MT'].mean()

# Média de múltiplas provas por tipo de escola
df.groupby('TP_ESCOLA')[['NU_NOTA_MT', 'NU_NOTA_CN']].mean()

# Frequência percentual
df.TP_SEXO.value_counts(normalize=True)

# 8. ORDENAÇÃO E RANKING

# Ordenação simples
df.sort_values(by='NU_NOTA_MT')

# Top maiores notas
df.nlargest(10, 'NU_NOTA_MT')

# Top menores notas
df.nsmallest(10, 'NU_NOTA_MT')

# Ordenação pelo índice
df.sort_index()

# 9. CRIAÇÃO E TRANSFORMAÇÃO DE COLUNAS

# Criação direta de coluna
df['MEDIA_OBJETIVAS'] = (
    df['NU_NOTA_CN'] +
    df['NU_NOTA_CH'] +
    df['NU_NOTA_LC'] +
    df['NU_NOTA_MT']
) / 4

# Criação usando assign
df = df.assign(LOG_MT=np.log(df.NU_NOTA_MT))

# Uso de eval
df.eval('(NU_NOTA_CN + NU_NOTA_MT) / 2')

# map para transformar valores
df.TP_SEXO.map({'M': 'Masculino', 'F': 'Feminino'})

# replace
df.TP_SEXO.replace({'M': 'Masculino', 'F': 'Feminino'})

# apply com função
def resultado(nota):
    if nota < 600:
        return 'Reprovado'
    else:
        return 'Aprovado'

df.NU_NOTA_MT.apply(resultado)

# 10. VISUALIZAÇÃO DE DADOS

# Gráfico de barras
df.TP_SEXO.value_counts().plot(kind='bar')
plt.title('Distribuição por gênero')
plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.show()

# Histograma
df.NU_NOTA_MT.plot(kind='hist')
plt.show()

# Boxplot
df.NU_NOTA_MT.plot(kind='box')
plt.show()

# Dispersão
df.plot(kind='scatter', x='NU_NOTA_MT', y='NU_NOTA_CN')
plt.show()

# Densidade
df.NU_NOTA_MT.plot(kind='kde')
plt.show()

# 11. MERGE / JOIN

# Leitura da base socioeconômica
economic_data = pd.read_csv('./dados_enem_2021_BA_questoes_socieconomicas.csv')

# Merge usando chave comum
df_merged = pd.merge(
    df,
    economic_data,
    on='NU_INSCRICAO',
    how='inner'
)
