from src.utils.tools import setup_logger
import pytest
import json
import os
from datetime import datetime
from os import path
import logging


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSetting up resources...")
    yield
    print("\nTearing down resources...")


@pytest.fixture(scope="session", autouse=True)
def log():
    log_level = logging.INFO
    root_path = path.dirname(path.dirname(path.dirname(path.realpath(__file__))))
    os.makedirs(path.join(root_path, "logs"), exist_ok=True)
    debug_log_filename = path.join(root_path, "logs", "debug.log")
    log = setup_logger(debug_log_filename, log_level, "log")
    return log



