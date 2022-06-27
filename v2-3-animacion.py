import app
import pygame
from pygame.locals import *

# Variables
y = 0


pygame.init()
screen = pygame.display.set_mode((600, 600))


def draw():
    global y
    screen.fill((0,0,0));
    pygame.draw.line(screen, (255, 0, 0), [0, y], [600, y])
    y = y + 1

app.run(draw)