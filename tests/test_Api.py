from tests import BaseTest
import pytest
import json
from deneme import RegisterTestData, GetUserTestData



class TestApi(BaseTest):
    BASE_URL = "https://3e3d2990-3fca-4144-8b26-1538cf135a09.mock.pstmn.io"

    @pytest.mark.parametrize('case', RegisterTestData().registerTestCases, ids=[i["Case"] for i in RegisterTestData().registerTestCases])
    def test_register(self, case):
        print(f"\nRunning -> {case['Case']}")
        request_dict = case["Request_Body"]
        print("Request Body:", request_dict)

        endpoint = "/users"
        response = self.Wrappers.post_wrapper(self.BASE_URL + endpoint, request_dict)

        if case['Test Type'].lower() == "positive":
            response_json = json.loads(response.content)
            self.EnsureThat.is_same(response.status_code, 201)  # Status code is expected as 201 when the request has succeeded and has led to the creation of a resource.
            self.EnsureThat.is_true(response_json["userId"] is not None)  # When the user created a User ID must be returned from the server. Checking if a User ID has returned.
            self.EnsureThat.is_true(type(response_json["userId"]) == str)  # When the user created a User ID must be returned from the server. Checking if the returned value is a string.

            self.EnsureThat.is_true((case["Request_Body"]["firstName"]).isalpha())  # Expect firstName to contain only Alpha chars
            self.EnsureThat.is_true((case["Request_Body"]["lastName"]).isalpha())  # Expect lastName to contain only Alpha chars
            self.EnsureThat.is_true((case["Request_Body"]["username"]).isalnum())   # Expect userName to contain only AlphaNumeric chars


        else:
            self.EnsureThat.is_same(response.status_code, 400)  # Status code is expected as 400 when the request cannot be processed due to something perceived to be a client error.

        self.EnsureThat.lower_than(response.elapsed.total_seconds(), 5)  # Expect the request to be responded within 5 seconds.

        #print(f"\n{responseJson}")


    def test_get_user_list(self):
        endpoint = "/users"
        response = self.Wrappers.get_wrapper(self.BASE_URL + endpoint)
        response_json = json.loads(response.content)
        self.EnsureThat.is_same(response.status_code, 200)  # Status code is expected as 200 when the request has succeeded.
        self.EnsureThat.lower_than(response.elapsed.total_seconds(), 5)  # Expect the request to be responded within 5 seconds.

        for user_data in response_json:  # Check the returned data for each user.
            if "id" in user_data and "username" in user_data and "firstName" in user_data and "lastName" in user_data and "isActive" in user_data:  # Expect the given keys to be in the returned user dictionary.
                self.EnsureThat.is_same(type(user_data["id"]), str)  # Expect ID to be String type
                self.EnsureThat.is_same(type(user_data["username"]), str)  # Expect Username to be String type
                self.EnsureThat.is_same(type(user_data["firstName"]), str)  # Expect First Name to be String type
                self.EnsureThat.is_same(type(user_data["lastName"]), str)  # Expect Last Name to be String type
                self.EnsureThat.is_same(type(user_data["isActive"]), bool)  # Expect Is Active key to be Boolean type
            else:
                self.EnsureThat.is_true(False)  # Fail the test

    @pytest.mark.parametrize('case', GetUserTestData.test_data)
    def test_get_user_by_id(self, case):
        print(case["Case"])
        endpoint = "/users"
        user_id = case["user_id"]
        response = self.Wrappers.get_wrapper(self.BASE_URL + endpoint + "/" + user_id)
        response_json = json.loads(response.content)

        if case["is_valid"]:
            self.EnsureThat.is_same(response.status_code, 200)  # Status code is expected as 200 when the request has succeeded.

            if "id" in response_json and "username" in response_json and "firstName" in response_json and "lastName" in response_json and "isActive" in response_json:  # Expect the given keys to be in the returned user dictionary.
                self.EnsureThat.is_same(type(response_json["id"]), str)  # Expect ID to be String type
                self.EnsureThat.is_same(type(response_json["username"]), str)  # Expect Username to be String type
                self.EnsureThat.is_same(type(response_json["firstName"]), str)  # Expect First Name to be String type
                self.EnsureThat.is_same(type(response_json["lastName"]), str)  # Expect Last Name to be String type
                self.EnsureThat.is_same(type(response_json["isActive"]), bool)  # Expect Is Active key to be Boolean type
            else:
                self.EnsureThat.is_true(False)  # Fail the test

        else:
            self.EnsureThat.is_same(response.status_code, 404)  # Status code is expected as 404 when that the server cannot find the requested resource.


