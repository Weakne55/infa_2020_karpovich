import pygame
from pygame.draw import *
from random import randint
import time
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1280, 720))

maxx=1280
maxy=720
sum=0


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

def click(event):
    global x, y, r
    print(x, y, r)

def score(sum):
    font = pygame.font.Font(None, 25)
    text = font.render('SCORE ' + str(sum), 1, (255, 255, 255))
    screen.blit(text, (1180, 10))


clock = pygame.time.Clock()
finished = False


while not finished:
    click = False
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 100)
    v1 = [-1,1]
    vx = v1[randint(0,1)]
    vy = v1[randint(0,1)]
    color = COLORS[randint(0, 5)]



    while click == False and finished == False:
        new_balls(x, y, r)
        x += vx
        y += vy
        clock.tick(FPS)
        if x >= (1280 - r):
            vx *= (-1)
        elif x <= (0 + r):
            vx *= (-1)
        if y >= (720 - r):
            vy *= (-1)
        elif y <= (0 + r):
            vy *= (-1)
        score(sum)
        pygame.display.update()
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print('Click!')
                if (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 <= r ** 2:
                    sum += 1
                    print('счет ', sum)
                    click = True


pygame.quit()
