import pygame
from pygame.draw import *
from random import randint
import time
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))
sum=0

maxx=1200
maxy=900

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_ball():
    global x, y, r,color
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]

def move_balls():
    time.sleep(3)
    global x, y, r
    while (x+r <=maxx) or (y+r <= maxy):
        circle(screen,color,(x,y),r)
        x +=1
        y +=1
        # screen.fill(BLACK)

def click(event):
    global x, y, r
    print(x, y, r)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(event)
            if (x-event.pos[0])**2+(y-event.pos[1])**2 <= r**2:
                sum += 1
                print(sum)
            if sum == 10:
                finished = True
    new_ball()
    move_balls()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
