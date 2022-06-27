import app
import pygame
from pygame.locals import *

def draw():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), [10, 10, 400,480])


pygame.init()
screen = pygame.display.set_mode((600, 600))

app.run(draw)