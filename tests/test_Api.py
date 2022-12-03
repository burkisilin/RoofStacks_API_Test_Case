from tests import BaseTest
import pytest
import json
from deneme import RegisterTestData, GetUserTestData
from utils.client import Client
import pytest_check as check  # Soft assertion in order to keep the tests running in case of any case fails.


class TestApi(BaseTest):
    BASE_URL = "https://3e3d2990-3fca-4144-8b26-1538cf135a09.mock.pstmn.io"

    @pytest.mark.parametrize('case', RegisterTestData().registerTestCases, ids=[i["Case"] for i in RegisterTestData().registerTestCases])
    def test_register(self, case):
        client = Client()
        self.logger.info(f"\nRunning -> {case['Case']}")
        request_dict = case["Request_Body"]
        self.logger.info(f"Request Body: {request_dict}")

        endpoint = "/users"
        response = client.post(endpoint, request_dict)

        if case['Test Type'].lower() == "positive":
            response_json = json.loads(response.content)

            check.equal(response.status_code, 201)  # Status code is expected as 201 when the request has succeeded and has led to the creation of a resource.
            check.is_true(response_json["userId"] is not None)  # When the user created a User ID must be returned from the server. Checking if a User ID has returned.
            check.is_true(type(response_json["userId"]) == str)  # When the user created a User ID must be returned from the server. Checking if the returned value is a string.

            check.is_true((case["Request_Body"]["firstName"]).isalpha())  # Expect firstName to contain only Alpha chars
            check.is_true((case["Request_Body"]["lastName"]).isalpha())  # Expect lastName to contain only Alpha chars
            check.is_true((case["Request_Body"]["username"]).isalnum())   # Expect userName to contain only AlphaNumeric chars


        else:
            check.equal(response.status_code, 400)  # Status code is expected as 400 when the request cannot be processed due to something perceived to be a client error.

        check.less(response.elapsed.total_seconds(), 5)  # Expect the request to be responded within 5 seconds.

        #print(f"\n{responseJson}")


    def test_get_user_list(self):
        client = Client()

        endpoint = "/users"
        response = client.get(endpoint)
        response_json = json.loads(response.content)
        check.equal(response.status_code, 200)  # Status code is expected as 200 when the request has succeeded.
        check.less(response.elapsed.total_seconds(), 5)  # Expect the request to be responded within 5 seconds.

        for user_data in response_json:  # Check the returned data for each user.
            if "id" in user_data and "username" in user_data and "firstName" in user_data and "lastName" in user_data and "isActive" in user_data:  # Expect the given keys to be in the returned user dictionary.
                check.equal(type(user_data["id"]), str)  # Expect ID to be String type
                check.equal(type(user_data["username"]), str)  # Expect Username to be String type
                check.equal(type(user_data["firstName"]), str)  # Expect First Name to be String type
                check.equal(type(user_data["lastName"]), str)  # Expect Last Name to be String type
                check.equal(type(user_data["isActive"]), bool)  # Expect Is Active key to be Boolean type
            else:
                check.is_true(False)  # Fail the test because the response has unexpected json data

    @pytest.mark.parametrize('case', GetUserTestData.test_data, ids=[i["Case"] for i in GetUserTestData.test_data])
    def test_get_user_by_id(self, case):
        client = Client()
        self.logger.info(case["Case"])
        self.logger.info(f"User ID: {case['user_id']}")
        endpoint = "/users"
        user_id = case["user_id"]
        response = client.get(f"{endpoint}/{user_id}")
        response_json = json.loads(response.content)

        if case["is_valid"]:
            check.equal(response.status_code, 200)  # Status code is expected as 200 when the request has succeeded.

            if "id" in response_json and "username" in response_json and "firstName" in response_json and "lastName" in response_json and "isActive" in response_json:  # Expect the given keys to be in the returned user dictionary.
                check.equal(type(response_json["id"]), str)  # Expect ID to be String type
                check.equal(type(response_json["username"]), str)  # Expect Username to be String type
                check.equal(type(response_json["firstName"]), str)  # Expect First Name to be String type
                check.equal(type(response_json["lastName"]), str)  # Expect Last Name to be String type
                check.equal(type(response_json["isActive"]), bool)  # Expect Is Active key to be Boolean type
            else:
                check.is_true(False)  # Fail the test because the response has unexpected json data

        else:
            check.equal(response.status_code, 404)  # Status code is expected as 404 when that the server cannot find the requested resource.


