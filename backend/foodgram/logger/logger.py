import logging
from logging import StreamHandler


def add_logger(name):
    """создание логов."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = StreamHandler()
    handler.setFormatter(
        logging.Formatter(
            '%(asctime)s:: %(levelname)s:: %(name)s:: %(message)s %(lineno)d'
        )
    )
    logger.addHandler(handler)
    return logger


logger = add_logger(__name__)
