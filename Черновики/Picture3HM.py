import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 500))

#background
rect(screen,   (112, 239, 243),  (0, 0, 800, 250))
rect(screen,   (41, 212, 92),    (0, 250, 800, 250))

#kid1
ellipse(screen,(210, 121, 238),  (110,  230, 50, 110))
circle(screen, (255, 255, 255),  (135, 215), 25)






#kid4
ellipse(screen,(210, 121, 238),  (660,  230, 50, 110))
circle(screen, (255, 255, 255),  (685, 215), 25)






pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()