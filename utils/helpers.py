import json
from tests import BaseTest


# Helping functions that used at some tests
class Helpers(BaseTest):

    def register(self):
        request_body = {
            "firstName": "burak",
            "lastName": "bayramoglu",
            "username": "burakb",
            "password": "123456Aa*"
        }
        response = self.client.post("/users", request_body)
        new_user_id = json.loads(response.content)["userId"]

        return request_body, new_user_id

    def get_user(self, id):
        response = self.client.get(f"/users/{id}")
        return json.loads(response.content)

    def get_users(self):
        response = self.client.get("/users")
        return json.loads(response.content)

    def check_user_is_deleted(self, users_after, user_id):
        matches = [sub for sub in users_after if sub['id'] == user_id]
        if len(matches) > 0:
            return False
        else:
            return True
