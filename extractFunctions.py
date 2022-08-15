import pandas as pd

def extractUrlData(url, rawFile):

    # Will extract file from url and save it as a csv
    # url = enter the desired url
    # rawFile = enter the desired filename to be saved

    raw_df = pd.read_csv(url)
    raw_df.to_csv(rawFile,index = False)

    print(rawFile +' has been created')

def refineRawData(rawFile,refineFile,coltoExtract=[]):

    # will extract the required columns from the rawfile and save it to new csv
    # rawFile = csv from where we need to extractUrlData
    # refineFile = csv where we need to save extract columns
    # coltoExtract = list of columns which we need to extract

    raw_df = pd.read_csv(rawFile)
    df = raw_df.filter(coltoExtract)
    df.to_csv(refineFile,index=False)

    print(refineFile +' has been created')


