import requests
import json
import pytest_check as check  # Soft assertion in order to keep the tests running in case of any case fails.


class BaseTest:  # Common classes


    class Wrappers(object):

        @staticmethod
        def get_wrapper(url):
            resp = requests.get(url)
            return resp

        @staticmethod
        def post_wrapper(url, dict):
            resp = requests.post(url, json=dict)
            return resp


    class EnsureThat(object):
        @staticmethod
        def is_same(value1, value2):
            check.equal(value1, value2)


        @staticmethod
        def is_true(value):
            check.equal(value, True)

        @staticmethod
        def greater_than(value1, value2):
            check.greater(value1, value2)


        @staticmethod
        def lower_than(value1, value2):
            check.less(value1, value2)
