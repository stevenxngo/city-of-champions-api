import logging
import sys
from typing import Optional


LOGGING_FORMATTER = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

DEBUG_LEVELS = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR]
DebugLevelType = int


def get_logger(
    name: Optional[str] = None, level: DebugLevelType = logging.DEBUG
):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(LOGGING_FORMATTER)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(level)

    return logger
