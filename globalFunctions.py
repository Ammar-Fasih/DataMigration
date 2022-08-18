import pandas as pd
import logging
import textwrap
import datetime


def logFunc(msg,level,log_start='inprocess'):

    #FileNaming
    filedirectory='logs/'
    currentDT = datetime.datetime.now()
    fileName = filedirectory + currentDT.strftime("%d_%m_%Y__%H_%M_%S") + "__test.log"

    #Root config
    logging.basicConfig(
        level=logging.DEBUG,
        format="{asctime} {levelname:<8} {message}",
        style='{',
        filename=fileName, 
        filemode='w'
    )
    #Setting UP logger with handler
    logger = logging.getLogger()
    # logger.setLevel(logging.INFO)
    # formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # handler = logging.FileHandler(fileName,mode='w', encoding='utf-8')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)

    #Text Formatting
    if len(msg) > 60:
        ftext = textwrap.TextWrapper(width=70,initial_indent='',subsequent_indent=' '*33,#break_long_words= False,
        break_on_hyphens= False).fill(text=msg)
    else:
        ftext=msg

    #Log execution
    if  log_start==True:
        logger.info('='*70)
    if level == 'debug':
        logger.debug(ftext)
    elif level == 'info':
        logger.info(ftext)
    elif level == 'warning':
        logger.warning(ftext)
    elif level == 'error':
        logger.error(ftext)
    elif level == 'critical':
        logger.critical(ftext)
    if log_start == False:
        logger.info('*'*70)




