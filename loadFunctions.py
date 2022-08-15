import pandas as pd

def load_to(file):
    df = pd.read_csv(file)
    print(df.columns.values)
    for i in df.itertuples(index=False,name=None):
        print(i)

load_to('refineData.csv')
    

