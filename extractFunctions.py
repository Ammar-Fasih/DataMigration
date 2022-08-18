import pandas as pd
from globalFunctions import logFunc

def extractUrlData(url, rawFile):

    logFunc(f'Extracting CSV data from\n {url}','info',True)
    # Will extract file from url and save it as a csv
    # url = enter the desired url
    # rawFile = enter the desired filename to be saved

    raw_df = pd.read_csv(url)
    raw_df.to_csv(rawFile,index = False)

    # print(rawFile +' has been created')
    logFunc(f'Extracted Rows: {len(raw_df)}','info')
    logFunc(f'File Generated: {rawFile}','info',False)

def refineRawData(rawFile,refineFile,coltoExtract=[]):

    # will extract the required columns from the rawfile and save it to new csv
    # rawFile = csv from where we need to extractUrlData
    # refineFile = csv where we need to save extract columns
    # coltoExtract = list of columns which we need to extract

    logFunc(f'Extracing required colums {coltoExtract}...','info')

    raw_df = pd.read_csv(rawFile)
    df = raw_df.filter(coltoExtract)
    df.to_csv(refineFile,index=False)

    print(refineFile + ' has been created')
    logFunc(f'Columns extracted: {str(len(coltoExtract))}','info')
    logFunc(f'File generated: {refineFile}','info',False)


