from __future__ import annotations
from smsapi.client import SmsApiPlClient
from smsapi.exception import SmsApiException


class SMS:
    __client = None

    def __init__(self, client: SmsApiPlClient):
        self.__client = client

    def send(self, **kwargs) -> None:
        try:
            self.__client.sms.send(to=kwargs.get('to'), message=kwargs.get('message'))
        except SmsApiException as e:
            print(e.message, e.code)

