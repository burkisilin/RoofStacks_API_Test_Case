import random
import string


# This file contains test cases and required test datas for the cases with the functions to build the data sets.

class RegisterTestData:
    def __init__(self):
        first_name_char_range = (2, 50)  # FirstName Char Ranges
        last_name_char_range = (2, 50)  # LastName Char Ranges
        user_name_char_range = (4, 12)  # username Char Ranges

        self.registerTestCases = [
            {
                "Case": "Create user - Register Success",
                "Test Type": "Positive",
                "Request_Body": self.generate_request_body(default=True)
            },
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                "Case": "Create user - Empty username Field",
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                "Case": "Create user - Firstname & Lastname & username Fields Empty",
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
                    "username": {
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
                    "username": {
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
                "Case": "Create user - Empty Lastname & username Field",
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
                    "username": {
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
                "Case": "Create user - Empty Lastname & username & Password Field",
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
                    "username": {
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
                "Case": "Create user - Empty username & Password Field",
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
                    "username": {
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
                "Case": "Create user - Empty Password Field",
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                    "username": {
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
                "Case": "Create user - username Alpha",
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
                    "username": {
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
                "Case": "Create user - username Numeric",
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
                    "username": {
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
                "Case": "Create user - username Symbolic",
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
                    "username": {
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
                "Case": "Create user - username AlphaNumeric & Symbolic",
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
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "All"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "AlphaNumeric"
                    }})
            },
            {
                "Case": "Create user - Password Alpha",
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
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Create user - Password AlphaNumeric",
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
                    "username": {
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
                "Case": "Create user - Password Numeric",
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
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "Numeric"
                    }})
            },
            {
                "Case": "Create user - Password Symbolic",
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
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "Symbolic"
                    }})
            },
            {
                "Case": "Create user - Password AlphaNumeric & Symbolic",
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
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "All"
                    }})
            },
            {
                "Case": "Create user - Firstname Is Below Min Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (1, 1),
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "All"
                    }})
            },
            {
                "Case": "Create user - Firstname & Lastname Are Below Min Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (1, 1),  # Firstname field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (1, 1),  # Firstname field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "All"
                    }})
            },
            {
                "Case": "Create user - Firstname & username Are Below Min Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (1, 1),  # Firstname field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": (1, 1),  # username field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "All"
                    }})
            },
            {
                "Case": "Create user - Firstname & Lastname & username Are Below Min Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (1, 1),  # Firstname field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (1, 1),  # Lastname field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": (1, 1),  # username field will be generated with 1 Char only
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "All"
                    }})
            },
            {
                "Case": "Create user - LastName Is Below Min Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (1, 1),  # Lastname field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "Symbolic"
                    }})
            },
            {
                "Case": "Create user - LastName & username Are Below Min Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (1, 1),  # Lastname field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": (1, 1),  # username field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "Symbolic"
                    }})
            },
            {
                "Case": "Create user - username Is Below Min Value",
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
                    "username": {
                        "range": (1, 1),  # username field will be generated with 1 Char only
                        "length": "Min",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "Symbolic"
                    }})
            },
            {
                "Case": "Create user - Firstname Is Above Max Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (51, 51),  # username field will be generated with 51 Char
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "All"
                    }})
            },
            {
                "Case": "Create user - Firstname & Lastname Are Above Max Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (51, 51),  # Firstname field will be generated with 51 Char
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (51, 51),  # Lastname field will be generated with 51 Char
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "All"
                    }})
            },
            {
                "Case": "Create user - Firstname & username Are Above Max Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (51, 51),  # Firstname field will be generated with 51 Char
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": (13, 13),  # username field will be generated with 13 Char
                        "length": "Max",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "All"
                    }})
            },
            {
                "Case": "Create user - Firstname & Lastname & username Are Above Max Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": (51, 51),  # Firstname field will be generated with 51 Char
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (51, 51),  # Lastname field will be generated with 51 Char
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": (13, 13),  # username field will be generated with 51 Char
                        "length": "Max",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "All"
                    }})
            },
            {
                "Case": "Create user - LastName Is Above Max Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (51, 51),  # Lastname field will be generated with 51 Char
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": user_name_char_range,
                        "length": "Mid",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "Symbolic"
                    }})
            },
            {
                "Case": "Create user - LastName & username Are Above Max Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": (51, 51),  # Lastname field will be generated with 51 Char
                        "length": "Max",
                        "chars_type": "Alpha"
                    },
                    "username": {
                        "range": (13, 13),  # username field will be generated with 13 Char
                        "length": "Max",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "Symbolic"
                    }})
            },
            {
                "Case": "Create user - username Is Above Max Value",
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
                    "username": {
                        "range": (13, 13),  # username field will be generated with 13 Char
                        "length": "Max",
                        "chars_type": "AlphaNumeric"
                    },
                    "password": {
                        "range": (4, 8),
                        "length": "Random",
                        "chars_type": "Symbolic"
                    }})
            }

        ]

    def generate_string(self, len_type="Random", char_range=(4, 8), chars_type="All"):

        if len_type.lower() == "min":
            string_len = char_range[0]
        elif len_type.lower() == "max":
            string_len = char_range[1]
        elif len_type.lower() == "mid":
            string_len = round((char_range[1] + char_range[
                0]) / 2)  # Rounded to the integer so the range function does not throw an error.
        elif len_type.lower() == "random":
            string_len = random.randint(char_range[0], char_range[1])
        else:
            raise ValueError('Unexpected Length Type', len_type, "Expected Types: Min, Max, Mid, Random")

        if chars_type.lower() == "alpha":  # Alphabetic characters only
            characters = string.ascii_letters

        elif chars_type.lower() == "numeric":  # Numeric Characters only
            characters = string.digits

        elif chars_type.lower() == "alphanumeric":  # Alphabetic and Numeric Characters only

            # Making sure the generated string contains both Ascii letters & digits. Random generation can cause issue that the string not containing one of those.
            string1 = ''.join(random.choice(string.ascii_letters) for _ in range(round(string_len / 2)))
            string2 = ''.join(random.choice(string.digits) for _ in range(string_len - len(string1)))

            generated_string = string1 + string2

        elif chars_type.lower() == "symbolic":  # Symbolic Characters only
            characters = string.punctuation

        elif chars_type.lower() == "all":  # Alphanumeric, Numeric & Symbolic Characters

            # Making sure the generated string contains both Ascii letters & digits & symbols. Random generation can cause issue that the string not containing one of those.
            string1 = ''.join(random.choice(string.ascii_letters) for _ in range(round(string_len / 3)))
            string2 = ''.join(random.choice(string.digits) for _ in range(round(string_len / 2) - len(string1)))
            string3 = ''.join(random.choice(string.punctuation) for _ in range(string_len - len(string1 + string2)))
            generated_string = string1 + string2 + string3

        else:
            raise ValueError('Unexpected Type', chars_type,
                             "Expected Types: Alpha, Numeric, AlphaNumeric, Symbolic, All")

        if chars_type.lower() == "symbolic" or chars_type.lower() == "alpha" or chars_type.lower() == "numeric":
            generated_string = ''.join(random.choice(characters) for _ in range(string_len))

        return generated_string

    def generate_request_body(self, dict_keys=None, default=False):
        if dict_keys is None:
            dict_keys = {}
        if default:
            request_body = {
                "firstName": "jane",
                "lastName": "doe",
                "username": "janedoe",
                "password": "123456Aa*"
            }
            return request_body

        else:
            request_body = {}
            for key, value in zip(dict_keys.keys(), dict_keys.values()):
                request_body[key] = self.generate_string(value["length"], value["range"], value["chars_type"])
            return request_body


class GetUserTestData:
    test_data = [
        {
            "Case": "Get User - Valid User ID",
            "user_id": "c4f6c088-f91b-494e-b7f0-a08f48df3180",
            "is_valid": True
        },
        {
            "Case": "Get User - Valid User ID",
            "user_id": "c3e140a4-99db-44c2-a9ea-896904745993",
            "is_valid": True
        },
        {
            "Case": "Get User - Invalid User ID",
            "user_id": "c1234567-AB12-ABC4-1234-A1B2C3D4E5",
            "is_valid": False
        },
        {
            "Case": "Get User - Invalid User ID",
            "user_id": "c1234567-AB12-ABC4-1234-A1B2C3D4E5",
            "is_valid": False
        },
        {
            "Case": "Get User - Empty User ID",
            "user_id": "",
            "is_valid": False
        }
    ]


class RemoveUserTestData:
    test_data = [
        {
            "Case": "Remove User - Valid User ID",
            "user_id": "c4f6c088-f91b-494e-b7f0-a08f48df3180",
            "Positive Case": True
        },
        {
            "Case": "Remove User - Invalid User ID",
            "user_id": "c1234567-AB12-ABC4-1234-A1B2C3D4E5",
            "Positive Case": False
        },
        {
            "Case": "Remove User - Empty User ID",
            "user_id": "",
            "Positive Case": False
        }
    ]


class SwitchActivityTestData:
    test_data = [
        {
            "Case": "Switch User Activity - Valid User ID - isActive: True (Boolean)",
            "user_id": "c4f6c088-f91b-494e-b7f0-a08f48df3180",
            "new_isActive": False,
            "Positive Case": True
        },
        {
            "Case": "Switch User Activity - Valid User ID - isActive: False (Boolean)",
            "user_id": "c4f6c088-f91b-494e-b7f0-a08f48df3180",
            "new_isActive": False,
            "Positive Case": True
        },
        {
            "Case": "Switch User Activity - Valid User ID - isActive: true (String)",
            "user_id": "c4f6c088-f91b-494e-b7f0-a08f48df3180",
            "new_isActive": "true",
            "Positive Case": False
        },
        {
            "Case": "Switch User Activity - Valid User ID - isActive: false (String)",
            "user_id": "c4f6c088-f91b-494e-b7f0-a08f48df3180",
            "new_isActive": "false",
            "Positive Case": False
        },
        {
            "Case": "Switch User Activity - Valid User ID - isActive: Empty",
            "user_id": "c4f6c088-f91b-494e-b7f0-a08f48df3180",
            "new_isActive": "",
            "Positive Case": False
        },
        {
            "Case": "Switch User Activity - Invalid User ID",
            "user_id": "c1234567-AB12-ABC4-1234-A1B2C3D4E5",
            "new_isActive": False,
            "Positive Case": False
        },
    ]


class UpdateUserInfoTestData:
    def __init__(self):
        first_name_char_range = (2, 50)  # FirstName Char Ranges
        last_name_char_range = (2, 50)  # LastName Char Ranges

        self.updateInfoTestCases = [
            {
                "Case": "Update User Info - Min Values",
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
                    }})
            },
            {
                "Case": "Update User Info - Mid Values",
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
                    }})
            },
            {
                "Case": "Update User Info - Max Values",
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
                    }})
            },
            {
                "Case": "Update User Info - Empty firstName Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "0",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Update User Info - Empty lastName Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "0",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Update User Info - Empty firstName & lastName Field",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "0",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "0",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Update User Info - Firstname & Lastname Alpha",
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
                    }})
            },
            {
                "Case": "Update User Info - Firstname Numeric",
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
                    }})
            },
            {
                "Case": "Update User Info - Firstname AlphaNumeric",
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
                    }})
            },
            {
                "Case": "Update User Info - Firstname Symbolic",
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
                    }})
            },
            {
                "Case": "Update User Info - Firstname AlphaNumeric & Symbolic",
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
                    }})
            },
            {
                "Case": "Update User Info - Lastname Numeric",
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
                    }})
            },
            {
                "Case": "Update User Info - Lastname AlphaNumeric",
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
                    }})
            },
            {
                "Case": "Update User Info - Lastname Symbolic",
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
                    }})
            },
            {
                "Case": "Update User Info - Lastname AlphaNumeric & Symbolic",
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
                    }})
            },
            {
                "Case": "Update User Info - Firstname Below Min Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Below",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Update User Info - LastName Below Min Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Below",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Update User Info - Firstname & Lastname are Below Min Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Below",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Below",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Update User Info - Firstname Above Max Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Above",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Update User Info - Lastname Above Max Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Mid",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Above",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Update User Info - Firstname & Lastname are Above Max Value",
                "Test Type": "Negative",
                "Request_Body": self.generate_request_body(dict_keys={
                    "firstName": {
                        "range": first_name_char_range,
                        "length": "Above",
                        "chars_type": "Alpha"
                    },
                    "lastName": {
                        "range": last_name_char_range,
                        "length": "Above",
                        "chars_type": "Alpha"
                    }})
            },
            {
                "Case": "Update User Info - Invalid Field",
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
                    "invalidField": {
                        "range": (4, 8),
                        "length": "Mid",
                        "chars_type": "Alpha"
                    }
                })
            },
            {
                "Case": "Update User Info - Invalid User ID",
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
                    }
                })
            }
        ]

    def generate_string(self, len_type="Random", char_range=(4, 8), chars_type="All"):
        if len_type.lower() == "min":
            string_len = char_range[0]
        elif len_type.lower() == "max":
            string_len = char_range[1]
        elif len_type.lower() == "mid":
            string_len = round((char_range[1] + char_range[
                0]) / 2)  # Rounded to the integer so the range function does not throw an error.
        elif len_type.lower() == "below":
            string_len = char_range[0] - 1
        elif len_type.lower() == "above":
            string_len = char_range[1] + 1
        elif len_type.lower() == "0":
            string_len = 0
        elif len_type.lower() == "random":
            string_len = random.randint(char_range[0], char_range[1])
        else:
            raise ValueError('Unexpected Length Type', len_type,
                             "Expected Types: Min, Max, Mid, Below, Above, 0, Random")

        if chars_type.lower() == "alpha":  # Alphabetic characters only
            characters = string.ascii_letters

        elif chars_type.lower() == "numeric":  # Numeric Characters only
            characters = string.digits

        elif chars_type.lower() == "alphanumeric":  # Alphabetic and Numeric Characters only

            # Making sure the generated string contains both Ascii letters & digits. Random generation can cause issue that the string not containing one of those.
            string1 = ''.join(random.choice(string.ascii_letters) for _ in range(round(string_len / 2)))
            string2 = ''.join(random.choice(string.digits) for _ in range(string_len - len(string1)))

            generated_string = string1 + string2

        elif chars_type.lower() == "symbolic":  # Symbolic Characters only
            characters = string.punctuation

        elif chars_type.lower() == "all":  # Alphanumeric, Numeric & Symbolic Characters

            # Making sure the generated string contains both Ascii letters & digits & symbols. Random generation can cause issue that the string not containing one of those.
            string1 = ''.join(random.choice(string.ascii_letters) for _ in range(round(string_len / 3)))
            string2 = ''.join(random.choice(string.digits) for _ in range(round(string_len / 2) - len(string1)))
            string3 = ''.join(random.choice(string.punctuation) for _ in range(string_len - len(string1 + string2)))
            generated_string = string1 + string2 + string3

        else:
            raise ValueError('Unexpected Type', chars_type,
                             "Expected Types: Alpha, Numeric, AlphaNumeric, Symbolic, All")

        if chars_type.lower() == "symbolic" or chars_type.lower() == "alpha" or chars_type.lower() == "numeric":  # Generating string
            generated_string = ''.join(random.choice(characters) for _ in range(string_len))

        return generated_string

    def generate_request_body(self, dict_keys=None, default=False):
        if dict_keys is None:
            dict_keys = {}
        if default:
            request_body = {
                "firstName": "jane",
                "lastName": "doe",
                "username": "janedoe",
                "password": "123456Aa*"
            }
            return request_body

        else:
            request_body = {}
            for key, value in zip(dict_keys.keys(), dict_keys.values()):
                request_body[key] = self.generate_string(value["length"], value["range"], value["chars_type"])
            return request_body
