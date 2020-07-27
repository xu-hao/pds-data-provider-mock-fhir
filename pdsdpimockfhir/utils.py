import os
import logging

def getLogger(name):
    logger = logging.getLogger(name)
    logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger
