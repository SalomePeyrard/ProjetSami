from coordinates import Coordinates
from image import Image


class Room:
    __coordinates: Coordinates
    __image: Image

    def __init__(self, x, y):
        self.__coordinates = Coordinates(x, y)
        self.__image = Image(0, 0, "./image/room.png")


    @property
    def X(self):
        return self.__coordinates.X

    @X.setter
    def X(self, value):
        self.__coordinates.X = value

    @property
    def Y(self):
        return self.__coordinates.Y

    @Y.setter
    def Y(self, value):
        self.__coordinates.Y = value

    def drawRoom(self, screen, x, y):
        return screen.blit(self.__image.load(), (x, y))

