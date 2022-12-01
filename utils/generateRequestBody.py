from config.Config import TestData


class RequestBody(object):

    @staticmethod
    def generate_register_body(validity):

        if validity.lower() == "valid":
            request_dict = {
                "firstName": "jan1e",
                "lastName": "doe",
                "username": "doejj",
                "password": "123456Aa*"
            }
            TestData.requestBodies.append(request_dict)
            print(TestData.requestBodies)
        elif validity.lower() == "invalid":
            pass
        else:
            raise ValueError('Unexpected Validty Type', validity, "Expected Types: Valid, Invalid")
        types = ["alpha", "alpha", "alphaNumeric"]

        return request_dict


