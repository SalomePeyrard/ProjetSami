from coordinates import Coordinates
from image import Image


class Ground:
    __Coordinates: Coordinates
    __image: Image

    def __init__(self, x, y):
        self.Coordinates = Coordinates(x, y)
        self.image = Image(0, 0, "./image/solpetit.png")

    @property
    def X(self):
        return self.Coordinates.X

    @X.setter
    def X(self, value):
        self.Coordinates.X = value

    @property
    def Y(self):
        return self.Coordinates.Y

    @Y.setter
    def Y(self, value):
        self.Coordinates.Y = value

    def drawGround(self, screen, x, y):
        return screen.blit(self.image.load(), (x, y))
