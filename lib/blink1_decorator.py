from blink1.blink1 import Blink1
from lib.color import Color


class B1:
    __dongle: Blink1 = None
    __alert_list: list[tuple] = [
        (750, 'red', 1),
        (750, 'white', 2),
    ]
    __alert_mail_list: list[tuple] = [
        (750, 'white', 1),
        (750, 'black', 2),
    ]

    def __init__(self, dongle: Blink1):
        self.__dongle = dongle

    def off(self) -> None:
        self.__dongle.off()

    def close(self) -> None:
        self.__dongle.close()

    def fade(self, color: Color) -> None:
        self.__dongle.fade_to_rgb(*color.settings())

    def play_pattern(self, name) -> None:
        method = '_' + name
        if callable(getattr(self, method)):
            getattr(self, method)()

    def _alert(self) -> None:
        for sequence in self.__alert_list:
            self.__dongle.write_pattern_line(*sequence)
        self.__dongle.play(1, 2, count=10)

    def _alert_mail(self) -> None:
        for sequence in self.__alert_mail_list:
            self.__dongle.write_pattern_line(*sequence)
        self.__dongle.play(1, 2, count=5)

