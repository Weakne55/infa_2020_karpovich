import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 700))

#background
rect(screen, (137, 111, 29), (0, 0, 400, 350))
rect(screen, (189, 154, 37), (0, 300, 400, 700))

#window1
rect(screen, (168, 253, 255), (0, 50, 55, 180))
rect(screen, (81, 194, 198),  (0, 55, 50, 60))
rect(screen, (81, 194, 198),  (0, 120, 50, 105))

#window2
rect(screen, (168, 253, 255), (100, 50, 130, 180))

rect(screen, (81, 194, 198),  (105, 55, 55, 60))
rect(screen, (81, 194, 198),  (105, 120, 55, 105))

rect(screen, (81, 194, 198),  (170, 55, 55, 60))
rect(screen, (81, 194, 198),  (170, 120, 55, 105))

#window3














pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
