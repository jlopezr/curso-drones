import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Draw
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 0), [10, 10, 400,480])

    # Blit everything
    pygame.display.flip()

pygame.quit()
sys.exit()
