import logging

logging.basicConfig(filename='text.log',level=logging.INFO, format='{asctime}  {levelname}  {message}',style= '{')
with open('text.log','a',newline='',encoding='utf-8') as f:
    print('\n\n',file=f)
logging.info('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx NEW INTERVAL xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')