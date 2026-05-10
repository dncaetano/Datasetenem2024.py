# -*- coding: utf-8 -*-


#Aluno: Danilo Ferreira Caetano
#Turma: IA, ML e DP

import pandas as pd       #importação da biblioteca pandas
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração visual
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (10,6)

# Carregar arquivo CSV
df = pd.read_csv("/content/26d9bc031e001bac7ac5a1d579334576 (1).csv")

# Visualizar primeiras linhas
df.head()

# Quantidade de linhas e colunas
df.shape

# Informações gerais
df.info()

# Valores ausentes
df.isnull().sum()

#média das notas de matemática

media_matematica = df['NU_NOTA_MT'].mean()
print(f"A média das notas em Matemática é: {media_matematica:.2f}")

#mediana da redação

mediana_redacao = df['NU_NOTA_REDACAO'].median()
print(f"Mediana da Redação:{mediana_redacao}")

#A mediana indica o valor central das notas de redação, reduzindo o impacto de valores extremos.

#Desvio Padrão de Ciencias Humanas

desvio_ch = df['NU_NOTA_CH'].std()
print("Desvio padrão CH:", desvio_ch)

#O desvio padrão mede a dispersão das notas. Quanto maior o valor, maior a desigualdade de desempenho entre os candidatos.

#5. VISUALIZAÇÃO GÁFICA:

#Distribuição de notas matemáticas

plt.hist(df['NU_NOTA_MT'], bins=30)
plt.title('Distribuição das Notas de Matemática')
plt.xlabel('Nota')
plt.ylabel('Quantidade de alunos')
plt.show()

"""### Análise da Distribuição das Notas de Matemática

O histograma acima ilustra a distribuição das notas de matemática entre os participantes. Podemos observar a concentração das notas, identificar a faixa mais comum de desempenho e verificar a simetria ou assimetria da distribuição. Uma distribuição mais à direita indicaria um desempenho geral mais elevado, enquanto picos específicos podem sinalizar aglomerados de alunos com notas semelhantes.
"""

#Nota média por tipo de escola

# Mapear os valores numéricos para descrições de texto
tipo_escola_map = {
    1.0: 'Federal',
    2.0: 'Estadual',
    3.0: 'Municipal',
    4.0: 'Privada'
}
df['TP_DEPENDENCIA_ADM_ESC_LABEL'] = df['TP_DEPENDENCIA_ADM_ESC'].map(tipo_escola_map)

media_escola = df.groupby('TP_DEPENDENCIA_ADM_ESC_LABEL')['NU_NOTA_MT'].mean()

media_escola.plot(kind='bar')

plt.title('Média de Matemática por Tipo de Escola')
plt.xlabel('Tipo de Escola')
plt.ylabel('Média da Nota')
plt.xticks(rotation=45, ha='right') # Rotacionar rótulos para melhor visualização
plt.tight_layout() # Ajustar layout para evitar sobreposição
plt.show()

"""### Análise da Média de Matemática por Tipo de Escola

Este gráfico de barras mostra a média das notas de matemática para diferentes tipos de escolas. Podemos observar claramente que estudantes de escolas privadas e federais tendem a ter médias mais altas em comparação com estudantes de escolas estaduais e municipais.
"""

#Relação entre Tipo de Escola e as Notas de Redação
sns.boxplot(x='TP_DEPENDENCIA_ADM_ESC_LABEL', y='NU_NOTA_REDACAO', data=df)

plt.title('Relação entre Tipo de Escola e Nota da Redação')
plt.xlabel('Tipo de Escola')
plt.ylabel('Nota da redação')
plt.xticks(rotation=45, ha='right') # Rotacionar rótulos para melhor visualização
plt.tight_layout() # Ajustar layout para evitar sobreposição
plt.show()

"""### Análise da Relação entre Tipo de Escola e Nota da Redação

Este box plot visualiza a distribuição das notas de redação para cada tipo de escola. Podemos observar que, de forma geral, estudantes de escolas privadas e federais tendem a apresentar medianas e quartis mais elevados nas notas de redação, indicando um desempenho superior em comparação com os alunos de escolas estaduais e municipais. A amplitude dos boxes e os outliers também podem fornecer insights sobre a variabilidade e a presença de notas atípicas dentro de cada grupo.
"""

#comparação entre escola Pública e privada

desigualdade = df.groupby('TP_DEPENDENCIA_ADM_ESC_LABEL')['NU_NOTA_MT'].mean()

print(desigualdade)

"""A análise exploratória dos dados do ENEM 2024 permite observar como fatores estruturais influenciam diretamente o desempenho educacional dos participantes. As estatísticas mostram diferenças relevantes entre grupos sociais e tipos de escola, indicando que o desempenho acadêmico não depende apenas do esforço individual.

Os gráficos evidenciam uma tendência de maiores notas entre estudantes de renda mais alta e alunos da rede privada. Isso sugere que acesso a recursos educacionais, infraestrutura e apoio pedagógico impactam significativamente os resultados.

Além disso, a dispersão das notas demonstra que existe uma desigualdade importante no sistema educacional brasileiro. Alguns grupos possuem oportunidades muito superiores em comparação a outros.

Essa análise também se conecta diretamente ao debate sobre ética e vieses em inteligência artificial. Sistemas de IA treinados com dados históricos podem reproduzir desigualdades já existentes na sociedade caso essas diferenças não sejam analisadas criticamente.

Portanto, trabalhar com dados exige não apenas conhecimento técnico, mas também responsabilidade social. A interpretação correta dos dados é fundamental para evitar conclusões simplistas e decisões injustas baseadas apenas em números.
"""