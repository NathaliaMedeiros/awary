'''
Tratar as colunas sem informação adicionando o texto “Não informado”.
Formatar a coluna de total de inscritos multiplicando por 100 milhões.
Formatar coluna “AVG” para 2 casas decimais depois da vírgula.
Mostrar os top 10 usuários.
Mostrar primeiros 100 usuários por nome decrescente.
Salvar um novo CSV com a informação tratada.
'''
# Função para ler e processar o arquivo CSV
import pandas as pd

def trata_dados(arquivo):
    df = pd.read_csv(arquivo, sep=';')
    #
    df['100M'] = pd.to_numeric(df['100M'], errors='coerce')
    df['100M'] = df['100M'] * 100_000_000
    df['Avg'] = df['Avg'].round(2)
    df = df.fillna('Não informado')
    maiores_valores = df.nlargest(10, 'AVG')
    print(df)
    print(f'Os 10 maiores valores: {maiores_valores}')
    df.to_csv('top_youtubers_tratado.csv')

trata_dados('topyoutube.csv')
