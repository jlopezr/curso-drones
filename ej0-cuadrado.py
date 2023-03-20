import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

# Draw
pygame.draw.rect(background, (237, 166, 208), [10, 10, 400,480])

# Blit everything
screen.blit(background, (0, 0))
pygame.display.flip()
