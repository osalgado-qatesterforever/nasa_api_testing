import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
import logging
import os
from os import path
import inspect


LOG_LEVEL = logging.INFO
root_path = path.dirname(path.dirname(path.dirname(path.realpath(__file__))))
common_formatter = logging.Formatter(
    "%(asctime)s [%(levelname)-7s][%(lineno)-3d]: %(message)s",
    datefmt="%Y-%m-%d %I:%M:%S",
)

def setup_logger(log_file, level=logging.INFO, name="", formatter=common_formatter):
    """ Set up a logger """
    handler = logging.FileHandler(log_file, mode="w")
    # Or use a rotating file handler
    # handler = RotatingFileHandler(log_file,maxBytes=1024, backupCount=5)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

# Create the logs directory
os.makedirs(path.join(root_path, "logs"), exist_ok=True)
debug_log_filename = path.join(root_path, "logs", "debug.log")
log = setup_logger(debug_log_filename, LOG_LEVEL, "log")

# logger for API outputs
api_formatter = logging.Formatter(
    "%(asctime)s: %(message)s", datefmt="%Y-%m-%d %I:%M:%S"
)
log = setup_logger(debug_log_filename, LOG_LEVEL, "log")


class TestNasa:
    def test_pic_of_the_day(self):
        apod_url = "https://api.nasa.gov/planetary/apod"
        params = {
            'api_key':"hH21kco9yqxWAEDKc2WoY7Pe6OdQw8EjjbjwgHCc"
            }
        response = requests.get(apod_url, params=params)
        pp = PrettyPrinter()
        print("Pretty response:")
        pp.pprint(response.json())
        response.raise_for_status()
        this_function_name = inspect.stack()[0].function
        log.info("Test %s passed." % this_function_name)
        log.info(f"Pretty response:\n {pp.pformat(response.json())}")
        

