import pytest
import logging
from utils.client import Client

logger = None


# Configurations for PyTest
@pytest.fixture(autouse=True, scope="function")
def setup(request):
    global logger
    BASE_URI = request.config.getoption("--BASE_URI")
    save_log = request.config.getoption("--SAVE_LOG")

    Client.set_url(BASE_URI)
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)
    if save_log:
        save_log = save_log.replace(".log", "")
        fh = logging.FileHandler(f'{save_log}.log')
        fh.setLevel(logging.INFO)
        logger.addHandler(fh)

    request.cls.logger = logger
    yield


def pytest_addoption(parser):
    parser.addoption("--BASE_URI", action="store", default="https://3e3d2990-3fca-4144-8b26-1538cf135a09.mock.pstmn.io",
                     help="Base URI for requests")  # Allows BASE URI to be set from command prompt

    parser.addoption("--SAVE_LOG", action="store", default=False,
                     help="Save Log on given path")  # Enables the log saving


def pytest_exception_interact(report):  # Log the assertion fails
    logger.error(f'Test exception:\n{report.longreprtext}')
