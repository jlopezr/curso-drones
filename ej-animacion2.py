import pygame
from pygame.locals import *
import sys

pygame.init()
screen = pygame.display.set_mode((600, 600))

# Variables
y=0

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Draw
    pygame.draw.line(background, (255, 0, 0), [0, y], [600, y])
    y = y + 1
    
    # Blit everything
    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()

