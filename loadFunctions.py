import pandas as pd
import logFunctions


def load_to(file):
    df = pd.read_csv(file)
    print(df.columns.values)
    for i in df.itertuples(index=False,name=None):
        print(i)
    logFunctions.logging.info(f' {file} file has been loaded succesfully')

load_to('refineData.csv')
    

