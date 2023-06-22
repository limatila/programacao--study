import logging #use it for better error handling, and registering events
import sentry_sdk as sy
from logging import DEBUG, INFO
from logging import FileHandler, StreamHandler
from logging import Formatter

from loghelper import n
fileh_formatter = Formatter(fmt= f'%(asctime)s - %(name)s - %(levelname)s - %(message)s; {n} times used')
fileh_handler= FileHandler('debugfile.txt', 'a')
fileh_handler.setFormatter(fileh_formatter)
#set a config: 
logging.basicConfig(level = DEBUG, encoding='UTF-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt = '%d/%m/%Y %H:%M:%S',
                    handlers= [fileh_handler,
                               StreamHandler(),
                               #RotatingFileHandler('debugfile.txt', 'a', 5)
                               ]
                    )

#FileHandler.setLevel(INFO)
#RotatingFileHandler.setlevel(INFO)

#logging.: .debug, < .info, < .warning, < .error, < .critical in levels of error
#default %(name)s: root is the logger


logging.debug("debug msg")
logging.debug('OK DEBUGGED')
logging.warning("input not ideal: see documentationa")

import loghelper
loghelper.logger.info('info message')
loghelper.logger.error('code failed')


""" #formatter
formate_ENdate = Formatter(datefmt= '%Y/%m/%d')#your config here

logging.basicConfig(level= INFO, datefmt= formate_ENdate)


logging.debug("debug msg")
logging.debug('OK DEBUGGED')
logging.warning("input not ideal: see documentationa")
"""




""" #loguro:
from loguru import logger

logger.debug("debug msg") #colorful
logger.info('FUK YU')
logger.warning("input not ideal: see dcumentationa")

#printo pro txt:
logger.add(
    'debugloguro.txt'
)
logger.warning('printed here')
"""

