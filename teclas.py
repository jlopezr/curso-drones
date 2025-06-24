import app
import pygame
from pygame.locals import *

# Variables
y = 0
color = (255,0,0)

pygame.init()
screen = pygame.display.set_mode((600, 600))


def draw():
    global y, color
    screen.fill((0,0,0));
    pygame.draw.line(screen, color, [0, y], [600, y])
    y = y + 1
    
    if app.getKey("UP"):
        color = (255,0,0)
        
    if app.getKey("DOWN"):
        color = (0,255,0)
        
    if app.getKey("b"):
        color = (0,0,255)
    

app.run(draw)