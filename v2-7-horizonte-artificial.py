import app
import pygame
import math
from pygame.locals import *
from djitellopy import tello

#me = tello.Tello()
#me.connect()

pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.freetype.SysFont("Arial", 12)

roll = 0
image = pygame.image.load('AirPlaneFront.png')

def toRadians(degrees):
    return (degrees*2*math.pi)/360

def blitRotate(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect.topleft)

def draw():
    global roll
    
    # Get data    
    #roll = me.get_roll()
    roll = roll + 1
    if roll == 360:
        roll = 0

    # Draw
    screen.fill((0, 0, 0))
    font.render_to(screen, (40, 60), f"Roll: {roll}", (0, 255, 0))
    blitRotate(screen, image, (300,300), roll)
    
app.run(draw)


