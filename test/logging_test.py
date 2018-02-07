# 测试1
import logging
logging.basicConfig(filename='log.txt',filemode='w',level=logging.DEBUG)
logging.debug('This level is debug')
logging.info('This level is info')
logging.warning('This level is warning')