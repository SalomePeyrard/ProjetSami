from coordinates import Coordinates
from image import Image


class Monster:
    __coordinates: Coordinates
    __image: Image

    def __init__(self, coordinates: Coordinates, image: Image):
        self.__coordinates = coordinates
        self.__image = image

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

    @property
    def Image(self):
        return self.__image
    