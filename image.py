import pygame
class Image:
    __width = 0
    __height = 0
    __file = ""

    def __init__(self, width: int, height: int, file: str):
        self.__width = width
        self.__height = height
        self.__file = file

    @property
    def Width(self):
        return self.__width

    @Width.setter
    def Width(self, value):
        self.__width = value

    @property
    def Height(self):
        return self.__height

    @Height.setter
    def Height(self, value):
        self.__height = value

    @property
    def File(self):
        return self.__file

    @File.setter
    def File(self, value):
        self.__file = value

    def load(self):
        image = pygame.image.load(self.__file).convert_alpha()
        return image
