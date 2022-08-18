import extractFunctions
import transformFunctions
import loadFunctions
import globalFunctions

url = 'https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv'

rawDataPath = 'rawData/rawData.csv'
refineDataPath = 'data/refineData.csv'

def main():
    extractFunctions.extractUrlData(url,'rawData/rawData.csv')

    extractFunctions.refineRawData(rawDataPath,refineDataPath,['ID','Name','Categories','Images'])

    transformFunctions.colSplit(refineDataPath,'Categories','>',['Categories','Sub_Categories'])

    transformFunctions.dfStrip(refineDataPath,['Categories'])

    transformFunctions.idGeneration(refineDataPath,'Categories','CAT-','category','data/catID.csv')

    transformFunctions.idGeneration(refineDataPath,'Sub_Categories','SUBCAT-','subcategory','data/subcatID.csv')

    transformFunctions.idMapping(refineDataPath,'y','y','y')

    transformFunctions.dfDrop(refineDataPath,['Categories','Sub_Categories','Images'])

    loadFunctions.loadData(refineDataPath)

if __name__=="__main__":
    main()