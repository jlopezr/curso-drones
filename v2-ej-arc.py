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
    app.draw_filled_arc()
    y = y + 1

app.run(draw)