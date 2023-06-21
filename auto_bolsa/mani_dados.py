import pandas as pd


def tabela():
    df = pd.read_csv('PETR4.SA.csv')
    pr = df['Adj Close']
    return pr
