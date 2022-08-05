from __future__ import annotations
from typing import final



class Color:
    RED: final = (1000, 255, 0, 0)
    GREEN: final = (1000, 0, 255, 0)
    __value: tuple = None

    def __init__(self, name: str):
        self.__value = getattr(self, name.upper())

    def settings(self) -> tuple:
        return self.__value

    def speed(self, speed: int = 300) -> Color:
        list(self.__value)[0] = speed
        self.__value = tuple(self.__value)

        return self
