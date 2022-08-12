from ast import main
from lib2to3.pgen2.pgen import DFAState
from types import NoneType
from unicodedata import name
import pandas as pd
import time
import urllib.request


st = time.time()


###################################### Functions #####################################
def extractRawData(url): # APPROACH 1  
    output = pd.read_csv(url)
    print('Raw data extracted')
    return output


# def extractRawData(url,output_csv): # APPROACH 2
#     df = pd.read_csv(url)
#     df.to_csv(output_csv)
#     print('Raw data extracted')

def refineRawData(rawData,colNames,colSplit):
    refData = rawData.filter(colNames)
    refData[[colSplit,f'Sub_{colSplit}']] = refData[colSplit].str.split('>',expand=True)
    refData[colSplit] = refData[colSplit].str.strip()
    return refData

# ###################################### Extracting and Refine to 3 columns #####################################
# url = 'https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv'
# # raw_refData = pd.read_csv(url)
# df = raw_df.filter(['ID','Name','Categories','Images'])
# df[['Categories','Sub_Categories']] = df['Categories'].str.split('>',expand=True)
# df['Categories'] = df['Categories'].str.strip()

# raw_df = extractRawData(url)

def extractCategory(refData):
    cat_df = refData.filter(['Categories'])
    cat_df.dropna(how='all', inplace=True)
    cat_df['Categories'] = cat_df['Categories'].str.strip()
    cat_df.drop_duplicates(inplace=True)
    C_ID = []
    for i in range(len(cat_df.index)):
            C_ID.append('C-' +str(i+1))
    cat_df['CAT-ID'] = C_ID
    print('Categories have been extracted')
    return cat_df


# ###################################### Extracting Categories and CAT_ID #######################################
# cat_df = df.filter(['Categories'])
# cat_df.dropna(how='all', inplace=True)
# cat_df['Categories'] = cat_df['Categories'].str.strip()
# cat_df.drop_duplicates(inplace=True)
# C_ID = []
# for i in range(len(cat_df.index)):
#         C_ID.append('C-' +str(i+1))
# cat_df['CAT-ID'] = C_ID
# print('Categories have been extracted')


def extractSubCategory(refData,ID):
    sub_cat_df = refData.filter(['Sub_Categories'])
    sub_cat_df.dropna(how='all', inplace=True)
    sub_cat_df.drop_duplicates(inplace=True)
    SC_ID = []
    for i in range(len(sub_cat_df.index)):
            SC_ID.append('SC-' +str(i+1))
    sub_cat_df[ID] = SC_ID
    print('Sub_Categories have been extracted')
    return sub_cat_df

def mapping(ID):
    newdf.loc[(newdf[ID]=)]
# ################################ Extracting Sub_Categories and SUBCAT_ID #####################################
# sub_cat_df = df.filter(['Sub_Categories'])
# sub_cat_df.dropna(how='all', inplace=True)
# sub_cat_df.drop_duplicates(inplace=True)
# SC_ID = []
# for i in range(len(sub_cat_df.index)):
#         SC_ID.append('SC-' +str(i+1))
# sub_cat_df['SUBCAT-ID'] = SC_ID
# print('Sub_Categories have been extracted')
if 'SUBCAT-ID':
    pass
if 'CAT-ID':
    pass


# ################################## Formation of Relational DF ###############################################
# CID =[]
# SCID = []
# filepath = 'images/'
# path = []
# # df = df.append({'CID':[4]})
# ############################ Category ID generation ######################################################
# for a,b in df.iterrows():
#     for c,d in cat_df.iterrows():
#         if d['Categories'] == b['Categories']:
#             # df.loc[(df['Categories'] == cat_df['Categories']), 'CID'] = cat_df['CAT-ID']
#             CID.append(cat_df['CAT-ID'][c])
#             break
#         elif (isinstance(b['Categories'],float)):
#             CID.append('NaN')
#             break

# ################################## Sub_Category ID generation #################################################
#     for e,f in sub_cat_df.iterrows():
#         if f['Sub_Categories'] == b['Sub_Categories']:
#             # df.loc[(df['Categories'] == cat_df['Categories']), 'CID'] = cat_df['CAT-ID']
#             SCID.append(sub_cat_df['SUBCAT-ID'][e])
#             break
#         elif (isinstance(b['Sub_Categories'],float)) | (isinstance(b['Sub_Categories'],NoneType)):
#             SCID.append('NaN')
#             break
#  ############################## Extracting & Downloading Images ########################################       
#     rowpath = []
#     if ',' in b['Images']:
#         b['Images'] = b['Images'].split()
#         print(type(b['Images']))
#     if (isinstance(b['Images'],list)):
#         for x,y in enumerate(b['Images']):
#             filename = 'Image_'+str(a+1)+'-'+str(x+1)
#             full_path = filepath + filename + '.jpg'
#             urllib.request.urlretrieve(y,full_path)
#             rowpath.append(full_path)
#     else:
#         filename = 'Image_'+str(a+1)
#         full_path = filepath + filename + '.jpg'
#         urllib.request.urlretrieve(b['Images'],full_path)
#         rowpath.append(full_path)
#     path.append(rowpath)
# print('Category IDs have been generated')
# print('Sub_Category IDs have been generated')
# print('All images have been downloaded')
    
# df.insert(3,'CID',CID)
# df.insert(5,'SCID',SCID)
# df.insert(6,'Path',path)
# # print(CID, len(CID))
# # print(SCID, len(SCID))
# # print(df)
# # print(cat_df)

# df_final = df.drop(['Categories','Images','Sub_Categories'], axis=1)
# ###################################### Creating CSV ######################################################
# df_final.to_csv('refineProducts.csv',index=False)
# cat_df.to_csv('categoryId.csv',index=False)
# sub_cat_df.to_csv('subCategoryId.csv',index=False)

# print('Requested CSVs have been created successfully')

# et = time.time()


# ######################### Execution Time #########################################
# print(et - st)

########################## DRIVER CODE ############################################

if __name__=="__main__":
    url = 'https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv'
    colNames =['ID','Name','Categories','Images']
    raw_df = extractRawData(url)
    refData = refineRawData(raw_df,colNames,'Categories')
    # cat_df = extractCategory(refData)
    # sub_cat_df=extractSubCategory(refData)
    print(refData)
    