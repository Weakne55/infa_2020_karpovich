import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
screen = pygame.display.set_mode((1280, 720))

x = randint(100, 700)
y = randint(100, 500)
v1 = [-1, 1]
vx = v1[randint(0, 1)]
vy = v1[randint(0, 1)]
main_params=[x,y,vx,vy]



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

a=randint(1,10)

pos_x=[a]
for i in range(len(pos_x)):
    pos_x[i]=randint(100,700)

pos_y=[a]
for i in range(len(pos_y)):
    pos_y[i]=randint(100,700)

pos_r=[a]
for i in range(len(pos_r)):
    pos_r[i]=randint(5,10)

def click(event):
    global x, y, r
    print(x, y, r)

def score(sum):
    font = pygame.font.Font(None, 25)
    text = font.render('SCORE ' + str(sum), 1, (255, 255, 255))
    screen.blit(text, (1180, 10))


clock = pygame.time.Clock()
finished = False

def ball(x,y,r,color,vx,vy):
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
        circle(screen, color, (x, y), r)
        pygame.display.update()
        screen.fill(BLACK)
        return [x,y,vx,vy]


while not finished:
    click = False
    color = COLORS[randint(0, 5)]
    r = randint(30, 100)

    while click == False and finished == False:
        main_params=ball(main_params[0],main_params[1],r,color,main_params[2],main_params[3])
        score(sum)
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
