import logging
import sys

def basic_debug(level=logging.DEBUG):
    logging.basicConfig(level=level, stream=sys.stdout)