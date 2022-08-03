import requests
from requests.exceptions import ConnectionError
from urllib3.exceptions import NewConnectionError
from urllib3.exceptions import MaxRetryError

class ApiRequest:
    __url = "None"

    def __init__(self, url):
        self.__url = url

    def post(self, info) -> requests.Response():
        try:
            return requests.post(self.__url, None, info)
        except (MaxRetryError, ConnectionError, NewConnectionError) as e:
            print(e)
