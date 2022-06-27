from capture import *
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
print(camlist)

cam = Capture()
cam.main()