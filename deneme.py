import random
import string


class TestData:
    def __init__(self):
        first_name_char_range = (2, 50)  # FirstName Char Ranges
        last_name_char_range = (2, 50)  # LastName Char Ranges
        user_name_char_range = (4, 12)  # UserName Char Ranges

        self.registerTestCases = [
            {
                "Case": "Create user - Minimum Values",
                "Test Type": "Positive",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Mid Values",
                "Test Type": "Positive",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Max Values",
                "Test Type": "Positive",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Max",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Empty Firstname Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (0, 0),  # Leaves the firstname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Empty Lastname Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (0, 0),  # Leaves the lastname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Empty Username Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": (0, 0),  # Leaves the username field empty
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Empty Password Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (0, 0),  # Leaves the password field empty
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Firstname & Lastname Fields Empty",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (0, 0),  # Leaves the firstname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (0, 0),  # Leaves the lastname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Firstname & Lastname & Username Fields Empty",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (0, 0),  # Leaves the firstname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (0, 0),  # Leaves the lastname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": (0, 0), # Leaves the username field empty
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - All Fields Empty",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (0, 0),  # Leaves the firstname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (0, 0),  # Leaves the lastname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": (0, 0),  # Leaves the username field empty
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (0, 0),
                        "length": "Min",  # Leaves the password field empty
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Empty Lastname & Username Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (0, 0),  # Leaves the lastname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": (0, 0),  # Leaves the username field empty
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Empty Lastname Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (0, 0),  # Leaves the lastname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Empty Lastname & Username Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (0, 0),  # Leaves the lastname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": (0, 0),  # Leaves the username field empty
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Empty Lastname & Username & Password Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (0, 0),  # Leaves the lastname field empty
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": (0, 0),  # Leaves the username field empty
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (0, 0),  # Leaves the username field empty
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Empty Username & Password Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": (0, 0),  # Leaves the username field empty
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (0, 0),  # Leaves the password field empty
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Firstname Alphanumeric",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Firstname Numeric",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Numeric"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Firstname Symbolic",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Symbolic"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Firstname Alphanumeric & Symbolic",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "All"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Lastname Alphanumeric",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Lastname Numeric",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Numeric"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Lastname Symbolic",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Symbolic"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Lastname Alphanumeric & Symbolic",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "All"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Username Alpha",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Username Numeric",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Username Symbolic",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Username AlphaNumeric & Symbolic",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "userName": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "All"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            }

        ]

    def generate_string(self, len_type="Random", char_range=(4, 8), chars_type="All"):

        if len_type.lower() == "min":
            string_len = char_range[0]
        elif len_type.lower() == "max":
            string_len = char_range[1]
        elif len_type.lower() == "mid":
            string_len = round((char_range[1] - char_range[0]) / 2)
        elif len_type.lower() == "random":
            string_len = random.randint(char_range[0], char_range[1])
        else:
            raise ValueError('Unexpected Length Type', len_type, "Expected Types: Min, Max, Mid, Random")

        if chars_type.lower() == "alpha":  # Alphabetic characters only
            characters = string.ascii_letters

        elif chars_type.lower() == "numeric":  # Numeric Characters only
            characters = string.digits

        elif chars_type.lower() == "alphanumeric":  # Alphabetic and Numeric Characters only
            characters = string.ascii_letters + string.digits

        elif chars_type.lower() == "symbolic":  # Symbolic Characters only
            characters = string.ascii_letters + string.digits + string.punctuation

        elif chars_type.lower() == "all":  # Alphanumeric, Numeric & Symbolic Characters
            characters = string.ascii_letters + string.digits + string.punctuation

        else:
            raise ValueError('Unexpected Type', chars_type, "Expected Types: Alpha, Numeric, AlphaNumeric, Symbolic, All")

        generated_string = ''.join(random.choice(characters) for _ in range(string_len))

        return generated_string

    def generate_request_body(self, dict_keys=None, default=False):
        if dict_keys is None:
            dict_keys = {}
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


