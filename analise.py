# Passo a passo
# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv('cancelamentos_sample.csv')

# Passo 2: Visualizar a base de dados (entender a base e identificar problemas)
# Deleter coluna CustomerID
tabela = tabela.drop(columns='CustomerID')

print(tabela)
# informações que não te ajudam, acabam te atrapalhando

# Passo 3: Corrigir os problemas da base de dados (tratamento de dados)
# valores vazios - deletar linhas que tem valores vazios
print(tabela.info())

tabela = tabela.dropna() # NaN -> not a number (valores vazios)

print(tabela.info())

# float -> numero com casa decimal
# object -> coluna com valores de texto

# Passo 4: Análise inicial -> quantos clientes cancelaram e qual o % de clientes
# contar na coluna cancelou os valores

print(tabela['cancelou'].value_counts())

# percentual
print(tabela['cancelou'].value_counts(normalize=True))

# Passo 5: Análise da causa de cancelamento dos clientes
# comparar as outras colunas da tabela coma a coluna de cancelamento
import plotly.express as px

for coluna in tabela.columns:
    # criar o gráfico
    grafico = px.histogram(tabela, x=coluna, color='cancelou', text_auto=True)

    # exibir o gráfico
    grafico.show()

# usuarios do contrato mensal sempre cancelam
    # evitar contrato mensal e incentivar as outras assinaturas

# todos os usuarios que ligaram mais de quatro vezes cancelaram
    # criar um processo que quando o usuario bater 3 ligações alerta vermelho

# usuarios que atarsaram o pagamento mais de 20 dias cancelaram
    # criar um alerta pra quando o atraso do pagamento bater 15 dias entrar em contato com o cliente

# duracao_contrato -> diferente de mensal
tabela = tabela[tabela['duracao_contrato'] != 'Monthly']

# ligacoes_callcenter >= a 4
tabela = tabela[tabela['ligacoes_callcenter']<=4]

# atraso_pagamento <= a 20 dias
tabela = tabela[tabela['dias_atraso']<=20]

# percentual
print(tabela['cancelou'].value_counts(normalize=True))