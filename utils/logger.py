import os
import logging
import datetime

LOGS_FILE = 'logs'

os.makedirs(LOGS_FILE,exist_ok = True)


LOG_FILE = os.path.join(f'log_{datetime.datetime.now().strftime("%Y-%m-%D.%H-%M-%S")}.log')

logging.basicConfig(
    filename = LOG_FILE,
    level = logging.INFO,
    format ="%(asctime)s-%(level)s-%(message)s"
)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger