import pandas as pd
from globalFunctions import logFunc

def loadData(transData: str,destination=None) -> list:
    '''
    Function to load transformed data `transdata`.
 
Parameters
----------
transData: The transformed data to be loaded.
destination: The format of destination to be loaded to.

Returns
----------
Currently returns nothing. Just prints.

    '''

    df = pd.read_csv(transData)
    errors=[]
    print('\n Loading data initialized')
    print(df.columns.values)
    for rows in df.itertuples(index=False,name=None):
        try:
            print(rows)
        except Exception as e:
            logFunc(e,'error')
            errors.append(e)
            return errors
    
    print('\nThe loading process of transformed data has been completed')
    logFunc(f'The loading process of transformed data has been completed with the following exceptions {errors}','info')