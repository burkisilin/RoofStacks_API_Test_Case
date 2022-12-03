import pytest
import logging
from utils.client import Client


@pytest.mark.usefixtures("setup")
class BaseTest:  # Common classes

    client = Client()
    logger: logging.Logger
