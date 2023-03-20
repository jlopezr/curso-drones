import app
import pygame
from pygame.locals import *
from djitellopy import tello
import numpy as np
import cv2

me = tello.Tello()
me.connect()

pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.freetype.SysFont("Arial", 12)

me.streamon()

def draw():
    global battery, roll, pitch, yaw, height
    
    # Get data
    battery = me.get_battery()
    roll = me.get_roll()
    pitch = me.get_pitch()
    yaw = me.get_yaw()
    height = me.get_height()

##    battery = 1
##    roll = 2
##    pitch = 3
##    yaw = 4
##    height = 5

    # Draw
    img = me.get_frame_read().frame
    
    if img is not None:
       img = np.fliplr(img)
       img = np.rot90(img)
       #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
       img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
       surf = pygame.surfarray.make_surface(img)
       screen.blit(surf, (0,0))
    else:
        screen.fill((0, 0, 0))
    
    font.render_to(screen, (40, 40), f"Battery: {battery}", (0, 255, 0))
    font.render_to(screen, (40, 60), f"Roll: {roll}", (0, 255, 0))
    font.render_to(screen, (40, 80), f"Pitch: {pitch}", (0, 255, 0))
    font.render_to(screen, (40, 100), f"Yaw: {yaw}", (0, 255, 0))
    font.render_to(screen, (40, 120), f"Height: {height}", (0, 255, 0))
    
    #indicador bateria
    pygame.draw.rect(screen, (128,128,128), [450,40, 100, 30])
    

app.run(draw)

