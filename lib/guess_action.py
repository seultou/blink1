from lib.vo.status import Status

class GuessAction:
    __status: str = None

    def __init__(self, status: Status):
        self.__status = status.value()

    def run(self):
        pass