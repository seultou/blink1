from typing import final


class Color:
    RED: final = (1000, 255, 0, 0)
    GREEN: final = (1000, 0, 255, 0)
    __value: tuple = None

    def __init__(self, name):
        self.__value = getattr(self, name.upper())

    def settings(self) -> tuple:
        return self.__value
