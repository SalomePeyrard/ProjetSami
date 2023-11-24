from image import Image


class Room:
    __x: int
    __y: int

    __image: Image

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__image = Image(0, 0, "./image/room.png")


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

    def drawRoom(self, screen, x, y):
        return screen.blit(self.__image.load(), (x, y))

