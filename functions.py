import pandas as pd

def extractUrlData(url, rawFile):
    raw_df = pd.read_csv(url)
    raw_df.to_csv(rawFile,index = False)

    print(rawFile +' has been created')


def refineRawData(rawFile,refineFile,coltoExtract=[]):
    raw_df = pd.read_csv(rawFile)
    df = raw_df.filter(coltoExtract)
    df.to_csv(refineFile,index=False)

    print(refineFile +' has been created')

def colsplit(file,maincol,delimiter,splitcols=[]):
    df = pd.read_csv(file)
    df[splitcols] = df[maincol].str.split(delimiter,expand=True)
    df['Categories'] = df['Categories'].str.strip()
    df.to_csv(file,index=False)

    print(maincol+' has been splitted to')

def idGeneration(file,maincol,idprefix,idheading,catidfile):
    cat_df = (pd.read_csv(file)).filter([maincol])
    cat_df.dropna(how='all', inplace=True)
    cat_df.drop_duplicates(inplace=True)
    ID = []
    for i in range(len(cat_df.index)):
        ID.append(idprefix +str(i+1))
    cat_df[idheading] = ID

    cat_df.to_csv(catidfile,index=False)
    print(maincol +' IDs have been generated')

def data_mapping(to_map,onto_map):
    pass

def id_mapping(onto_map):
    for a,b in (pd.read_csv(onto_map)).iterrows():
        pass

def catId_map(cat_map):
    CID =[]
    cat_df = pd.read_csv(cat_map)
    for c,d in cat_df.iterrows():
        if d['Categories'] == b['Categories']:
            CID.append(cat_df['CAT-ID'][c])
            break
        elif (isinstance(b['Categories'],float)):
            CID.append('NaN')
            break

url = 'https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv'

extractUrlData(url,'rawfile.csv')

refineRawData('rawfile.csv','refine.csv',['ID','Name','Categories','Images'])

colsplit('refine.csv','Categories','>',['Categories','Sub_Categories'])

idGeneration('refine.csv','Categories','CAT-','Category-ID','catID.csv')

idGeneration('refine.csv','Sub_Categories','SUB_C-','Sub_Category-ID','subCatID.csv')