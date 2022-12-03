import json
import pytest
from tests import BaseTest
from utils.client import Client
import pytest_check as check  # Soft assertion in order to keep the tests running in case of any case fails.
from config.test_datas import RegisterTestData, GetUserTestData, RemoveUserTestData, SwitchActivityTestData
from utils.helpers import Helpers


class TestApi(BaseTest):
    client = Client()
    helpers = Helpers()

    @pytest.mark.parametrize('case', RegisterTestData().registerTestCases,
                             ids=[i["Case"] for i in RegisterTestData().registerTestCases])
    def test_register(self, case):
        request_dict = case["Request_Body"]

        self.logger.info(f"\nRunning -> {case['Case']}\nRequest Body: {request_dict}")

        response = self.client.post("/users", request_dict)

        if case['Test Type'].lower() == "positive":
            response_json = json.loads(response.content)

            check.equal(response.status_code,
                        201)  # Status code is expected as 201 when the request has succeeded and has led to the creation of a resource.
            check.is_true(response_json[
                              "userId"] is not None)  # When the user created a User ID must be returned from the server. Checking if a User ID has returned.
            check.is_true(type(response_json[
                                   "userId"]) == str)  # When the user created a User ID must be returned from the server. Checking if the returned value is a string.

            check.is_true((case["Request_Body"]["firstName"]).isalpha())  # Expect firstName to contain only Alpha chars
            check.is_true((case["Request_Body"]["lastName"]).isalpha())  # Expect lastName to contain only Alpha chars
            check.is_true(
                (case["Request_Body"]["username"]).isalnum())  # Expect userName to contain only AlphaNumeric chars

        else:
            check.equal(response.status_code,
                        400)  # Status code is expected as 400 when the request cannot be processed due to something perceived to be a client error.

        check.less(response.elapsed.total_seconds(), 5)  # Expect the request to be responded within 5 seconds.

    def test_register_integration(self):  # Testing of if the registration works.
        new_user_json, new_user_id = self.helpers.register()
        users = self.helpers.get_users()

        user_found = False
        for user in users:
            if user["id"] == new_user_id:
                user_found = True
                check.equal(user["username"], new_user_json[
                    "username"])  # Check if the found user id data matches with the register body.
                check.equal(user["firstName"], new_user_json[
                    "firstName"])  # Check if the found user id data matches with the register body.
                check.equal(user["lastName"], new_user_json[
                    "lastName"])  # Check if the found user id data matches with the register body.
                break  # Stop checking when the user found by ID.
        if not user_found:
            assert False  # Registered user could not be found.

    def test_get_user_list(self):
        response = self.client.get("/users")
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
                self.logger.error("Test has failed because response has unexpected type of json data")
                check.is_true(False)  # Fail the test because the response has unexpected json data

    @pytest.mark.parametrize('case', GetUserTestData.test_data, ids=[i["Case"] for i in GetUserTestData.test_data])
    def test_get_user_by_id(self, case):
        user_id = case["user_id"]

        self.logger.info(f"| Case: {case['Case']} | User ID: {user_id}")

        response = self.client.get(f"/users/{user_id}")
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
                self.logger.error("Test has failed because response has unexpected type of json data")
                check.is_true(False)  # Fail the test because the response has unexpected json data

        else:
            check.equal(response.status_code,
                        404)  # Status code is expected as 404 when that the server cannot find the requested resource.

        check.less(response.elapsed.total_seconds(), 5)  # Expect the request to be responded within 5 seconds.

    @pytest.mark.parametrize('case', RemoveUserTestData.test_data,
                             ids=[i["Case"] for i in RemoveUserTestData.test_data])
    def test_remove_user(self, case):
        user_id = case["user_id"]
        self.logger.info(f"| Case: {case['Case']} | User ID: {user_id}")

        response = self.client.delete(f"/users/{user_id}")
        users_after = self.helpers.get_users()
        if case["Positive Case"]:
            check.equal(response.status_code,
                        204)  # Status code is expected as 204 when the server successfully processed the request, but is not returning any content.
            check.is_true(
                self.helpers.check_user_is_deleted(users_after, user_id))  # Check if the user has deleted successfully.

        else:
            check.equal(response.status_code,
                        404)  # Status code is expected as 404 when that the server cannot find the requested resource.

        check.less(response.elapsed.total_seconds(), 5)  # Expect the request to be responded within 5 seconds.

    @pytest.mark.parametrize('case', SwitchActivityTestData.test_data,
                             ids=[i["Case"] for i in SwitchActivityTestData.test_data])
    def test_switch_user_activity(self, case):
        user_id = case["user_id"]

        self.logger.info(f"| Case: {case['Case']} | User ID: {user_id} | New isActive: {case['new_isActive']}")

        request_body = {"isActive": case['new_isActive']}
        response = self.client.patch(f"/users/{user_id}/activity", request_body)
        if case["Positive Case"]:
            response_json = json.loads(response.content)
            check.is_true(response_json["userId"] == user_id and response_json["isActive"] == case[
                'new_isActive'])  # Check if the returned user is correct and "isActive" value is updated successfully.
            check.equal(response.status_code, 200)  # Status code is expected as 200 when the request has succeeded.
        else:
            check.equal(response.status_code,
                        400)  # Status code is expected as 400 when the request cannot be processed due to something perceived to be a client error.

        check.less(response.elapsed.total_seconds(), 5)  # Expect the request to be responded within 5 seconds.

