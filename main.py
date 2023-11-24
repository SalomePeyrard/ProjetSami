from maps.ground import Ground
from maps.room import Room
from maps.wall import Wall
import pygame
from game.config import *
from player.player import Player

mur = Wall(0, 0)  # image de mur
sol = Ground(0, 0)  # image de sol
room = Room(0, 0)  # image de salle
sami = Player(0, 0)  # image de sami

pygame.init()

screen = pygame.display.set_mode((640, 640))  # taille de la fenetre
pygame.display.set_caption("Super Sami Bosse")  # nom de la fenetre


def affichage(screen):
    for i in range(0, 640, 16):
        for j in range(0, 640, 16):
            sol.drawGround(screen, i, j)
            if tilemap[0][j // 16][i // 16] == 'B':
                mur.drawWall(screen, i, j)
            if tilemap[0][j // 16][i // 16] == '_':
                room.drawRoom(screen, i, j)


screen.fill((0, 0, 0))
affichage(screen)

run = True
while run:  # boucle de jeu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    sami.drawPlayer(screen, sami.X, sami.Y)
    sami.move()
    pygame.display.update()

pygame.quit()
quit()
