import app
import pygame
from pygame.locals import *

# Variables
ang = 0


pygame.init()
screen = pygame.display.set_mode((600, 600))


def draw():
    global ang
    screen.fill((0,0,0));
    app.draw_filled_arc(screen, (0,0,255), (70,70), 50, ang, ang+90)
    ang = ang + 1

app.run(draw)