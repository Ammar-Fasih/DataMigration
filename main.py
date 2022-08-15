import extractFunctions
import transformFunctions

url = 'https://raw.githubusercontent.com/woocommerce/woocommerce/master/sample-data/sample_products.csv'

extractFunctions.extractUrlData(url,'rawData.csv')

extractFunctions.refineRawData('rawData.csv','refineData.csv',['ID','Name','Categories','Images'])

transformFunctions.colsplit('refineData.csv','Categories','>',['Categories','Sub_Categories'])

transformFunctions.df_strip('refineData.csv',['Categories'])

transformFunctions.idGeneration('refineData.csv','Categories','CAT-','category','catID.csv')

transformFunctions.idGeneration('refineData.csv','Sub_Categories','SUBCAT-','subcategory','subcatID.csv')

# transformFunctions.id_mapping('refineData.csv','y','y','y')

transformFunctions.df_drop('refineData.csv',['Categories','Sub_Categories','Images'])

