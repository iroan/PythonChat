import logging

# create logger_client
logger_client = logging.getLogger('cli')
logger_client.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch_client = logging.FileHandler(filename='log.txt', mode='a')
ch_client.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch_client
ch_client.setFormatter(formatter)

# add ch_client to logger_client
logger_client.addHandler(ch_client)

logger_server = logging.getLogger('ser')
logger_server.setLevel(logging.DEBUG)
# add ch_client to logger_client
logger_server.addHandler(ch_client)