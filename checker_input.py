class CheckerInput:
    def __init__(self, string_input):
        self.__string = string_input
        self.__length = len(self.string)

    @property
    def string(self):
        return self.__string

    @property
    def length(self):
        return self.__length

