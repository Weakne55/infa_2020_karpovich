import pygame
from pygame.draw import *
from random import randint
import time
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1280, 720))

maxx=1280
maxy=720

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]



def new_balls(x,y,r):
    circle(screen, color, (x, y), r)


clock = pygame.time.Clock()
finished = False


while not finished:

    click1 = False
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 100)
    v1 = [-1,1]
    vx = v1[randint(0,1)]
    vy = v1[randint(0,1)]
    color = COLORS[randint(0, 5)]

    while click1 == False and finished == False:
        new_balls(x, y, r)
        x += vx
        y += vy
        clock.tick(FPS)
        pygame.display.update()
        screen.fill(BLACK)
        if x >= (1280 - r):
            vx *= (-1)
        elif x <= (0 + r):
            vx *= (-1)
        if y >= (720 - r):
            vy *= (-1)
        elif y <= (0 + r):
            vy *= (-1)

pygame.quit()
