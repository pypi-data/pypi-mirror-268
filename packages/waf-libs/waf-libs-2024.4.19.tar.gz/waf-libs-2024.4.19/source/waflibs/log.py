"""
utils for logging
"""

import logging
import os
import random
import sys
import time

from waflibs.constants import PROGRAM_NAME

DEBUG = logging.DEBUG
VERBOSE = DEBUG

INFO = logging.INFO


def get_logger(name=PROGRAM_NAME):
    """get current logger"""

    return logging.getLogger(name)


def is_verbose(args):
    """check whether verbosity is set"""

    return "verbose" in args and args.verbose


has_verbose = is_verbose


def set_level(logger, level):
    logger.setLevel(level)


def create_logger(args={}, verbose=False, program_name=PROGRAM_NAME, log_format=None):
    """create logger"""

    logger = get_logger()

    divider = "#" * 55

    if log_format is None:
        log_format = f"""{divider}
timestamp: %(asctime)s | name: %(name)s
filename: %(filename)s | path name: %(pathname)s
module: %(module)s | function name: %(funcName)s() | line num: %(lineno)s
level name: %(levelname)s | level num: %(levelno)s

START LOG
%(message)s
END LOG
{divider}"""
    elif log_format == "simple":
        log_format = None
    formatter = logging.Formatter(log_format)

    if is_verbose(args) or verbose:
        set_level(logger, VERBOSE)

        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        logger.addHandler(sh)

        fh = logging.FileHandler(f"/tmp/{program_name}.{time.time()}.log", mode="a+")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    else:
        set_level(logger, INFO)

    return logger
