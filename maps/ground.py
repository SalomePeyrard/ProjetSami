from image import Image


class Ground:
    __x: int
    __y: int
    __image: Image

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = Image(0, 0, "./image/solpetit.png")

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

    def drawGround(self, screen, x, y):
        return screen.blit(self.image.load(), (x, y))
