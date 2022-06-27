import sys
import pygame
from pygame.locals import *
from djitellopy import tello

me = tello.Tello()
me.connect()

pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.freetype.SysFont("Arial", 12)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Get data
    battery = me.get_battery()
    roll = me.get_roll()
    pitch = me.get_pitch()
    yaw = me.get_yaw()
    height = me.get_height()

    # Draw
    font.render_to(background, (40, 40), f"Battery: {battery}", (0, 255, 0))
    font.render_to(background, (40, 60), f"Roll: {roll}", (0, 255, 0))
    font.render_to(background, (40, 80), f"Pitch: {roll}", (0, 255, 0))
    font.render_to(background, (40, 100), f"Yaw: {roll}", (0, 255, 0))
    font.render_to(background, (40, 120), f"Height: {height}", (0, 255, 0))

    # Blit everything
    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()


