# 1. INSPEÇÃO INICIAL DO DATASET

# Objetivo:
# Entender a estrutura geral dos dados antes de qualquer análise

# Foi verificado:
# - O tamanho do dataset (quantidade de linhas e colunas)
# - Os nomes das colunas
# - Os tipos de dados de cada coluna
# - A presença de valores ausentes (NaN)



# 2. COMPARAÇÃO DE NOTAS POR GÊNERO

# Pergunta de análise:
# Existe diferença de desempenho em Matemática entre homens e mulheres?

# Exemplo trabalhado:
# Encontre a média, a mediana, o valor mínimo e o valor máximo
# das notas de Matemática para alunos do sexo masculino e feminino.


# 3. IDENTIFICAR ALUNO COM MAIOR E MENOR NOTA

# Objetivo:
# Descobrir qual aluno obteve a maior e a menor nota em Matemática

# Ferramentas utilizadas:
# - max()     → para obter o maior valor
# - idxmax() → para descobrir o índice onde ocorreu a maior nota
# - iloc     → para acessar a linha completa do aluno


# 4. ANÁLISE DA REDAÇÃO

# Questões analisadas:
# - O que representa um valor NaN na prova?
# - Qual a diferença entre nota zero e nota ausente?

# Etapas realizadas:
# - Identificação de valores NaN na nota da redação
# - Remoção de notas iguais a zero
# - Análise da distribuição das notas utilizando:
#   * Histograma
#   * Boxplot



# 5. CÁLCULO DA MÉDIA GERAL DO ALUNO

# Objetivo:
# Calcular a média das cinco provas para cada aluno

# Observação:
# - A média foi calculada por linha (por aluno)
# - Cada aluno passou a ter uma nota média geral



# 6. TRATAMENTO DE DADOS AUSENTES (MISSING)

# Problema:
# A média geral pode conter valores ausentes (NaN)

# Estratégias apresentadas:
# - Imputação com valor simbólico (-1)
# - Imputação utilizando a média da amostra
# - Imputação utilizando a mediana da amostra

# Objetivo:
# Demonstrar diferentes abordagens e seus impactos


# 7. DISTRIBUIÇÃO POR GÊNERO E TIPO DE ESCOLA

# Análises realizadas:
# - Quantidade absoluta de alunos por gênero
# - Quantidade absoluta de alunos por tipo de escola
# - Proporção percentual (%) de cada grupo



# 8. DESEMPENHO POR TIPO DE ESCOLA

# Pergunta de análise:
# Alunos de escolas públicas e privadas apresentam desempenho diferente?

# Métricas analisadas:
# - Média das notas de Matemática
# - Média das notas de Ciências da Natureza

# Comparação:
# - Escola Pública × Escola Privada


# 9. RANKING POR MUNICÍPIO

# Perguntas respondidas:
# - Quais municípios possuem as maiores notas médias?
# - Quais municípios possuem a maior quantidade de inscritos?

# Estratégia:
# - Agrupamento por município
# - Ordenação dos resultados
# - Criação de rankings


# 10. CRIAÇÃO DE TABELAS RESUMO

# Tabelas construídas:
# - Métricas estatísticas por município
# - Quantidade de inscritos por município
# - Percentual de inscritos em relação ao total

# Técnica utilizada:
# - Junção de tabelas utilizando merge


# 11. VISUALIZAÇÕES

# Tipos de gráficos utilizados:
# - Gráfico de barras
# - Gráfico de pizza
# - Histograma
# - Boxplot
# - Gráfico de dispersão
# - Gráfico de linhas (ranking de municípios)

# Objetivo:
# Facilitar a interpretação visual dos dados


# 12. TRANSFORMAÇÃO DE VARIÁVEIS

# Transformações realizadas:
# - Aplicação de logaritmo nas notas
# - Mapeamento de códigos numéricos para categorias textuais
# - Criação de colunas mais interpretáveis para análise


# 13. JOIN COM DADOS SOCIOECONÔMICOS

# Objetivo:
# Unir a base principal do ENEM com o questionário socioeconômico

# Resultado:
# - Dataset enriquecido com informações adicionais
# - Possibilidade de análises mais complexas e explicativas
