import extractFunctions
import transformFunctions
import loadFunctions
import globalFunctions

url = 'https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv'

def main():
    extractFunctions.extractUrlData(url,'rawData/rawData.csv')

    extractFunctions.refineRawData('rawData/rawData.csv','data/refineData.csv',['ID','Name','Categories','Images'])

    transformFunctions.colSplit('data/refineData.csv','Categories','>',['Categories','Sub_Categories'])

    transformFunctions.df_strip('data/refineData.csv',['Categories'])

    transformFunctions.idGeneration('data/refineData.csv','Categories','CAT-','category','data/catID.csv')

    transformFunctions.idGeneration('data/refineData.csv','Sub_Categories','SUBCAT-','subcategory','data/subcatID.csv')

    transformFunctions.id_mapping('data/refineData.csv','y','y','y')

    transformFunctions.df_drop('data/refineData.csv',['Categories','Sub_Categories','Images'])

    loadFunctions.load('data/refineData.csv')

if __name__=="__main__":
    main()