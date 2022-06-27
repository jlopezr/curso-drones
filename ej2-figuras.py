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

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Draw
    pygame.draw.rect(background, (255, 255, 0), [10, 10, 400,480],8)
    pygame.draw.line(background, (255, 0, 0), (0,0),(600,600))
    pygame.draw.circle(background, (0, 255, 0), (300,300), 100)
    pygame.draw.circle(background, (0, 255, 200), (300,300), 100, 8)
    pygame.draw.ellipse(background, (0, 255, 200), (400,200, 100, 50))
    

    # Blit everything
    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()