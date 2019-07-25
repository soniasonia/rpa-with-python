import logging
import os
import sys
from dotenv import load_dotenv
load_dotenv(verbose=True)

LOG_FILE = os.getenv('LOG_FILE')

logger = logging.getLogger("logger")
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handlers = [logging.StreamHandler(stream=sys.stdout), logging.FileHandler(LOG_FILE)]
for handler in handlers:
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel('INFO')


def info(s):
    logger.info(s)


def error(s):
    logger.error(s)
    # TODO: Add Sending email


def debug(s):
    logger.debug(s)
