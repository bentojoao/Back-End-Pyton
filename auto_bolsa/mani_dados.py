import pandas as pd
import glob


def tabela():
    cam = '../../../../Downloads/*.csv'
    arq = glob.glob(cam)
    for a in arq:
        df = pd.read_csv(a)
        pr = df['Adj Close']
        return pr


from mouseinfo import mouseInfo
mouseInfo()