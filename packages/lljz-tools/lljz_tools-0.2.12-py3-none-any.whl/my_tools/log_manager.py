import sys

from loguru import logger


def init_logger():
    import os
    if "PYTHONPATH" in os.environ and os.path.exists(os.environ['PYTHONPATH']):
        path = os.environ['PYTHONPATH']
    else:
        path = '/pythonlogs'
        if not os.path.exists(path):
            os.mkdir(path)

    logger.remove()
    logger.add(sys.stdout, level="DEBUG")
    logger.add(os.path.join(path, 'trace.log'), level="TRACE", rotation="5 MB", compression="zip")
    logger.add(os.path.join(path, 'info.log'), level="INFO", rotation="5 MB", compression="zip")
    logger.add(os.path.join(path, 'error.log'), level="ERROR", rotation="5 MB", compression="zip")
    return logger