from config_info import Config

class Status(object):
    __name: str = None

    def __init__(self, name):
        if not name in Config.AVAILABLE_STATUS:
            raise ValueError("[" + name + "] is not a valid status!")

        self.__name = name

    def value(self):
        return self.__name