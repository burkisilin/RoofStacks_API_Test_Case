from config.Config import TestData
from tests import BaseTest
import pytest
import requests
import json
from utils import generateRequestBody
from config.Config import TestData
from deneme import TestData


class TestApi(BaseTest):
    BASE_URL = "https://3e3d2990-3fca-4144-8b26-1538cf135a09.mock.pstmn.io"

    @pytest.mark.parametrize('case', TestData().registerTestCases)
    def test_register(self, case):
        print(f"\nRunning -> {case['Case']}")
        request_dict = case["Request_Body"]
        print("Request Body:" ,request_dict)
        endpoint = "/users"
        response = self.Wrappers.post_wrapper(self.BASE_URL + endpoint, request_dict)

        if case['Test Type'].lower() == "positive":
            response_json = json.loads(response.content)
            self.EnsureThat.is_same(response.status_code, 201)  # Status code is expected as 201 when the request has succeeded and has led to the creation of a resource.
            self.EnsureThat.is_same(response_json["userId"] is not None, True)  # When the user created a User ID must be returned from the server. Checking if a User ID has returned.
            self.EnsureThat.is_same(type(response_json["userId"]) == str, True)  # When the user created a User ID must be returned from the server. Checking if the returned value is a string.
        else:
            self.EnsureThat.is_same(response.status_code, 400)  # Status code is expected as 400 when the request cannot be processed due to something perceived to be a client error.

        self.EnsureThat.lower_than(response.elapsed.total_seconds(), 5)  # Expect the request to be responded within 5 seconds.

        #print(f"\n{responseJson}")
