import app
import pygame
from pygame.locals import *

# Variables
x = 300
y = 300
speedX = 1
speedY = 2

l = 0

pygame.init()
screen = pygame.display.set_mode((600, 600))
app.frameRate(60)

def draw():
    global x,y,l
    screen.fill((0,0,0));
    pygame.draw.line(screen, (255, 0, 0), [0, l], [600, l])
    l = l + 1
    if l>610:
        l = -10
    
    pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, (0,255,0), pos, 10)
    
    
    

    pygame.draw.circle(screen, (0,0,255), (x,y), 10)
    if app.getKey("UP"):
        y=y-1
    if app.getKey("DOWN"):
        y=y+1
    if app.getKey("LEFT"):
        x=x-1
    if app.getKey("RIGHT"):
        x=x+1
    x = x + speedX
    y = y + speedY
    
app.run(draw)
