import logging

logfile = "prgmdebug.log"
with open(logfile, 'w'):
    pass
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(logfile)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)
try:
    logger.info('logger has been initialized')
except Exception as e:
    print(f"Error during logging: {e}")