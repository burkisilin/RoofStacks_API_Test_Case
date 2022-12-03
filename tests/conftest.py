import pytest
import logging
from utils.client import Client


@pytest.fixture(autouse=True, scope="function")
def setup(request):
    BASE_URI = request.config.getoption("--BASE_URI")
    Client.set_url(BASE_URI)
    logger = logging.getLogger(request.node.name)
    logger.setLevel(logging.INFO)
    logger.propagate = True

    request.cls.logger = logger
    yield


def pytest_addoption(parser):
    parser.addoption("--BASE_URI", action="store", default="https://3e3d2990-3fca-4144-8b26-1538cf135a09.mock.pstmn.io",
                     help="Base URI for requests")

def pytest_exception_interact(report):
    logging.error(f'Test exception:\n{report.longreprtext}')