class Coordinates:
    __x: int
    __y: int

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def X(self):
        return self.__x

    @X.setter
    def X(self, value):
        self.__x = value

    @property
    def Y(self):
        return self.__y

    @Y.setter
    def Y(self, value):
        self.__y = value
