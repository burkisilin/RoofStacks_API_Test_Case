import requests


class Client:
    __BASE_URL: str

    @classmethod
    def set_url(cls, url: str):
        cls.__BASE_URL = url

    @classmethod
    def get_url(cls):
        return cls.__BASE_URL

    def get(self, endpoint):
        response = requests.get(self.__BASE_URL + endpoint)
        return response

    def post(self, endpoint, body):
        response = requests.post(self.__BASE_URL + endpoint, json=body)
        return response

    def delete(self, endpoint):
        response = requests.delete(self.__BASE_URL + endpoint)
        return response

    def put(self):
        pass

    def patch(self, endpoint, body):
        response = requests.patch(self.__BASE_URL + endpoint, json=body)
        return response

