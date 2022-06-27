import pygame
import math
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Horizonte Artificial')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))



# Draw
pygame.draw.circle(background, (128, 128, 128), [320, 240], 170, 5)
#pygame.draw.circle(background, (0, 255, 0), [320, 240], 150, 0)

widthArc = 160
pygame.draw.arc(background, (255,0,0), [320-widthArc,240-widthArc,widthArc*2,widthArc*2], math.pi, math.pi*2)

# Blit everything
screen.blit(background, (0, 0))
pygame.display.flip()

