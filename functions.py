import pandas as pd
from types import NoneType
import urllib.request
import os

# Extraction Phase

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

# Transformation Phase

def colsplit(file,maincol,delimiter,splitcols=[]):

    # will split any column into required columns with a defined deilmiter
    # file = original data file
    # maincol = column that we need to extractUrlData
    # delimiter = define the seperator HeaderRegistry
    # splitcols = enter the list of new generated columns

    df = pd.read_csv(file)
    df[splitcols] = df[maincol].str.split(delimiter,expand=True)
    df['Categories'] = df['Categories'].str.strip()  #this has to be generalized
    df.to_csv(file,index=False)

    print(maincol+' has been splitted')

def df_strip(file,stripcols=[]):

    # will strip the required columns, removing the whitespaces and save it to existing csv
    # file = original file name
    # stripcols = list of columns we need to strips

    df = pd.read_csv(file)
    for col in stripcols:
        df[col] = df[col].str.strip()
    df.to_csv(file,index=False)
    print('strip function completed')

def idGeneration(file,maincol,idprefix,idheading,catidfile):

    # will generate unique ids for the required columns elements and save it to new csv
    # file = original file name
    # maincol = column for which ID need generation Required
    # idprefix = enter the unique prefix for ID
    # idheading = enter 'category' or 'subcategory' for which id generation reuqired
    # catidfile = new csv filename

    id_df = (pd.read_csv(file)).filter([maincol])
    id_df.dropna(how='all', inplace=True)
    id_df.drop_duplicates(inplace=True)
    ID = []
    for i in range(len(id_df.index)):
        ID.append(idprefix +str(i+1))
    if idheading == 'category':
        id_df['CAT-ID'] = ID
    elif idheading == 'subcategory':
        id_df['SUBCAT-ID'] = ID

    id_df.to_csv(catidfile,index=False)
    print(maincol +' IDs have been generated')

def id_mapping(onto_map,cat,scat,img):

    # will map IDs on original file
    # onto_map = original file on which mapping Required
    # cat = enter 'y' to map it
    # scat = enter 'y' to map it
    # img = enter 'y' to map it

    # x = input("Do you wan't to map Category IDs? (y/n)")
    # y = input("Do you wan't to map Sub_Category IDs? (y/n)")

    cat_input = input('Input filename of categories: ')
    subcat_input = input('Input filename of sub_categories: ')
    global a,b
    CID=[]
    SCID=[]
    imgPath = []
    df = pd.read_csv(onto_map)
    for a,b in df.iterrows():
        if cat == 'y':
            CID.append(catId_map(cat_input))
        if scat == 'y':
            SCID.append(subCatId_map(subcat_input))
        if img == 'y':
            imgPath.append(img_map())
  
    if cat == 'y':
        df = df.assign(CAT_ID=CID)
    if scat == 'y':
        df = df.assign(SUBCAT_ID=SCID)
    if img == 'y':
        df = df.assign(Img_Path=imgPath)
        
    print('Mapping has been completed')
    # print(df)
    df.to_csv(onto_map,index=False)

def catId_map(catidfile):

    # will execute mapping of catId
    # catidfile = enter the catid csv file name

    cat_df = pd.read_csv(catidfile)
    for c,d in cat_df.iterrows():
        if d['Categories'] == b['Categories']:
            x =(cat_df['CAT-ID'][c])
            break
        elif (isinstance(b['Categories'],float)):
            x =('NaN')
            break
    return x

def subCatId_map(subCatIdFile):

    # will exexute mapping of subCatId
    # subCatIdFile = enter the subcatID csv file name

    sub_cat_df = pd.read_csv(subCatIdFile)
    for e,f in sub_cat_df.iterrows():
        if f['Sub_Categories'] == b['Sub_Categories']:
            # df.loc[(df['Categories'] == cat_df['Categories']), 'CID'] = cat_df['CAT-ID']
            x=(sub_cat_df['SUBCAT-ID'][e])
            break
        elif (isinstance(b['Sub_Categories'],float)) | (isinstance(b['Sub_Categories'],NoneType)):
            x=('NaN')
            break
    return x

def img_map(filepath='images/'):

    # will execute the mapping of image
    # filepath = enter the path to put downloded files

    # Limitations:
    # It will only takes images data from current file onto which mapping is done
    rowpath = []
    if not os.path.isdir(filepath):
            os.makedirs(filepath)
    if ',' in b['Images']:
        b['Images'] = b['Images'].split()
        print(type(b['Images']))
    if (isinstance(b['Images'],list)):
        for x,y in enumerate(b['Images']):
            filename = 'Image_'+str(a+1)+'-'+str(x+1)
            full_path = filepath + filename + '.jpg'
            urllib.request.urlretrieve(y,full_path)
            rowpath.append(full_path)
    else:
        filename = 'Image_'+str(a+1)
        full_path = filepath + filename + '.jpg'
        urllib.request.urlretrieve(b['Images'],full_path)
        rowpath.append(full_path)
    return rowpath

def df_drop(file,dropcol=[]):

    # will drop the unwanted columns from a csv and update iter
    # file = enter the file name for modification
    # dropcol = enter list of columns to be dropped

    df = pd.read_csv(file)
    df_new = df.drop(dropcol,axis=1)
    df_new.to_csv(file,index=False)

    print('Requested columns dropped')


if __name__ == '__main__':

    url = 'https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv'

    # extractUrlData(url,'rawfile.csv')

    # refineRawData('rawfile.csv','refine.csv',['ID','Name','Categories','Images'])

    # colsplit('refine.csv','Categories','>',['Categories','Sub_Categories'])

    # idGeneration('refine.csv','Categories','CAT-','category','catID.csv')

    # idGeneration('refine.csv','Sub_Categories','SUB_C-','subcategory','subCatID.csv')

    # id_mapping('refine.csv','y','y','y')

    # df_strip('trystrip.csv',['Categories','CAT-ID'])

    # df_drop('refine.csv',['Images'])

