import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

## Draw Flower {{{
pygame.draw.ellipse(screen, (255, 192, 203), [20, 20, 10, 25], 0)
#pygame.draw.ellipse(screen, (255, 192, 203), [20, 5, 10, 25], 0)
#pygame.draw.ellipse(screen, (255, 192, 203), [7, 20, 20, 10], 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()