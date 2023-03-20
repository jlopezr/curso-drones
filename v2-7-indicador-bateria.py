import app
import pygame
from pygame.locals import *
from djitellopy import tello

me = tello.Tello()
me.connect()

pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.freetype.SysFont("Arial", 12)

def draw():
    global battery, roll, pitch, yaw, height
    
    # Get data
    battery = me.get_battery()
    roll = me.get_roll()
    pitch = me.get_pitch()
    yaw = me.get_yaw()
    height = me.get_height()

##    battery = 10
##    roll = 2
##    pitch = 3
##    yaw = 4
##    height = 5

    # Draw
    screen.fill((100, 100, 100))
    font.render_to(screen, (40, 40), f"Battery: {battery}", (0, 255, 0))
    font.render_to(screen, (40, 60), f"Roll: {roll}", (0, 255, 0))
    font.render_to(screen, (40, 80), f"Pitch: {pitch}", (0, 255, 0))
    font.render_to(screen, (40, 100), f"Yaw: {yaw}", (0, 255, 0))
    font.render_to(screen, (40, 120), f"Height: {height}", (0, 255, 0))
    
    #indicador bateria
    pygame.draw.rect(screen, (128,128,128), [450,40, 100, 30])
    if battery > 20:
        pygame.draw.rect(screen, (0,255,0), [450,40, battery, 30])
    else:
        pygame.draw.rect(screen, (255,0,0), [450,40, battery, 30])
    pygame.draw.rect(screen, (0,0,0), [450,40, 100, 30],2)        
    

app.run(draw)

