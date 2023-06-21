import logging
from logging import DEBUG, INFO, WARNING, StreamHandler, FileHandler, Formatter
import datetime as date

fileh = FileHandler("FileHandlerFromDefaultLog.txt","a")
streamh = StreamHandler()

file_format = Formatter('%(asctime)s ... %(levelname)s -- %(message)s', datefmt='%d/%m/%Y %H:%M')
stream_format = Formatter('[%(levelname)s] -- %(message)s')

fileh.setFormatter(file_format)
streamh.setFormatter(stream_format)

logging.basicConfig(encoding='UTF-8', datefmt = '%d/%m/%Y %H:%M',
                    handlers=[fileh, streamh], level=DEBUG
                    )

logging.debug("Default Logger by Atila: Imported and Started...")