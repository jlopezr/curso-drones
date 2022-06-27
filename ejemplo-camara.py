import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

camlist = pygame.camera.list_cameras()
print(camlist)

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

if camlist:
    cam = pygame.camera.Camera(camlist[0],(640,480))
    cam.start()
    cam.set_controls(hflip = True, vflip = False)
    print(cam.get_controls())
    image = cam.get_image()
    
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(image, (0, 0))
        pygame.display.flip()

    pygame.quit()

    
    
