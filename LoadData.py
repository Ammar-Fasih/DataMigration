import pandas as pd
from functions import logfunc

def load(transData: str,destination=None) -> list:
    '''
    Function to load transformed data `transdata`.
 
    :param transData: The transformed data to be loaded.
    :param destination: The format of destination to be loaded to.
    :returns: Currently returns nothing. Just prints.

    '''

    df = pd.read_csv(transData)
    errors=[]
    print('\n Loading data initialized')
    print(df.columns.values)
    for rows in df.itertuples(index=False,name=None):
        try:
            print(rows)
        except Exception as e:
            logfunc(e,'error')
            errors.append(e)
            return errors
    
    print('\nThe loading process of transformed data has been completed')
    logfunc(f'The loading process of transformed data has been completed with the following exceptions {errors}','info')