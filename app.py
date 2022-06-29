import sys
import pygame
from pygame.locals import *

frames = 60

def frameRate(f):
    global frames
    frames = f

def getKey(keyName):
    ans = False
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    return ans

def run(draw):
    global frames
    
    clock = pygame.time.Clock()
    running = True
    while running:
        # Wait for fps
        clock.tick(frames)
        
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
