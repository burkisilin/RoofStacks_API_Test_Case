import random
import string

class TestData:
    firstNameCharRange = (2, 50)  # FirstName Char Ranges
    lastNameCharRange = (2, 50)  # LastName Char Ranges
    userNameCharRange = (4, 12)  # UserName Char Ranges

    def generate_string(self, len_type="Random", char_range=(4, 8), chars_type="All"):

        if len_type.lower() == "min":
            string_len = char_range[0]
        elif len_type.lower() == "max":
            string_len = char_range[1]
        elif len_type.lower() == "mid":
            string_len = (char_range[1] - char_range[0]) / 2
        elif len_type.lower() == "random":
            string_len = random.randint(char_range[0], char_range[1])
        else:
            raise ValueError('Unexpected Length Type', len, "Expected Types: Min, Max, Mid, Random")

        if chars_type.lower() == "alpha":  # Alphabetic characters only
            characters = string.ascii_letters

        elif chars_type.lower() == "alphanumeric":  # Alphabetic and Numeric Characters only
            characters = string.ascii_letters + string.digits

        elif chars_type.lower() == "all":  # Alphanumeric, Numeric & Symbolic Characters
            characters = string.ascii_letters + string.digits + string.punctuation

        else:
            raise ValueError('Unexpected Type', type, "Expected Types: Alpha, AlphaNumeric, All")

        generated_string = ''.join(random.choice(characters) for _ in range(string_len))

        return generated_string


    def generate_request_body(self, dict_keys={}, default=False):
        if default:
            request_body = {
                    "firstName": "jan1e",
                    "lastName": "doe",
                    "username": "doejj",
                    "password": "123456Aa*"
            }
            return request_body

        else:
            request_body = {}
            for key, value in zip(dict_keys.keys(), dict_keys.values()):
                request_body[key] = self.generate_string(value["length"], value["range"], value["chars_type"])
            return request_body


    request_body = {}
    dict_keys = {
        "firstName": {
            "range": firstNameCharRange,
            "length": "Min",
            "chars_type": "Alpha"
        },
        "lastName": {
            "range": lastNameCharRange,
            "length": "Min",
            "chars_type": "Alpha"
        },
        "userName": {
            "range": userNameCharRange,
            "length": "Min",
            "chars_type": "Alpha"
        },
        "password":{
            "range": (2,8),
            "length": "Random",
            "chars_type": "AlphaNumeric"
        }
    }

    requestBodies = []


    registerTestCases = [

        {
            "Case": "Create User - Username Symbol",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Firstname is Below Minimum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Lastname is Below Minimum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Username is Below Minimum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},        {
            "Case": "Create User - Firstname and Lastname are Below Minimum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Lastname and Username are Below Minimum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Firstname,Lastname and Username are Below Minimum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Firstname is Below Maximum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Lastname is Below Maximum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Username is Below Maximum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Firstname and Lastname are Below Maximum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Firstname and Username are Below Maximum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Lastname and Username are Below Maximum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Firstname,Lastname and Username are Below Maximum Value",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }},
        {
            "Case": "Create User - Password Field Not Entered",
            "Request_Body": {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }}
    ]