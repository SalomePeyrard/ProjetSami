
import pygame
from image import Image


class Player:
    __x: int
    __y: int
    __image: Image

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__image = Image(0, 0, "./image/sami.png")


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

    def drawPlayer(self, screen, x, y):
        return screen.blit(self.__image.load(), (x, y))

    def move(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.X -= 1
                print("left")
            if keys[pygame.K_RIGHT]:
                self.X += 1
                print("right")
            if keys[pygame.K_UP]:
                self.Y -= 1
                print("up")
            if keys[pygame.K_DOWN]:
                self.Y += 1
                print("down")


