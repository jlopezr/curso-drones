import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))


# Draw
screen.fill((0, 0, 0))
pygame.draw.rect(screen, (255, 255, 0), [10, 10, 400,480])

# Blit everything
pygame.display.flip()
