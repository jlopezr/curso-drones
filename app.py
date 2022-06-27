import sys
import pygame
from pygame.locals import *

def run(draw):
    running = True
    while running:
        # Wait for events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    
        # Draw
        draw()
    
        # Blit everything
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()
