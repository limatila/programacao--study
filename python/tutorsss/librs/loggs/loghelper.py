import logging
import datetime
#set a name for initl, counts in file everytime its used
from logging import DEBUG, WARNING, FileHandler, StreamHandler

#init count
initl = logging.getLogger(f"{__name__} init")
initl.level= DEBUG
initl_file_h = FileHandler('loghelperDEBUG_init.txt', 'a')#set to file

#counting in file
with open('loghelperDEBUG_init.txt', 'r') as f:
    fil = f.read()
n= 0

for i in fil:
    if i == ('\n'):
        n+=1 
n+=1
#dates
t = datetime.datetime.now(tz= None).strftime('%d-%m-%Y - %H:%M:%S')

formatter = logging.Formatter(f'{t} -- %(message)s -- {n} times used')#formatting message to file handler
initl_file_h.setFormatter(formatter)
initl.addHandler(initl_file_h)#setting handler

initl.info('loghelper is being used!')#should be infoed in file import
#fim do init

def logHelper_countUses(): 
    print(f'loghelper used a total of {n} times by now.')

#setando logger normal
logger = logging.getLogger(__name__)
logger_file_h = FileHandler("loghelperDEBUG.txt", 'a')

logger_stream_h = StreamHandler()
t = datetime.datetime.now(tz= None).strftime('%d-%m-%Y - %H:%M:%S')
formatter1 = logging.Formatter(f'{t} -- %(name)s -- %(levelname)s -- %(message)s')

logger_file_h.setFormatter(formatter1)
logger_stream_h.setFormatter(formatter1)
logger_file_h.setLevel(logging.ERROR)
#logger.addHandler(logger_stream_h) stream handler ja é incluso no console do outro arquivo
logger.addHandler(logger_file_h)

