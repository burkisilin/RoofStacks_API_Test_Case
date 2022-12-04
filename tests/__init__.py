import pytest
import logging
from utils.client import Client


# BaseTest class for all the tests
@pytest.mark.usefixtures("setup")
class BaseTest:  # Common classes

    client = Client()
    logger: logging.Logger
