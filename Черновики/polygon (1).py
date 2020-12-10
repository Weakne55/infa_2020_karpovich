import pygame
from pygame.draw import *
import time
import math
pygame.init()
FPS = 30
w = input('Введите ширину прямоугольника ')
h = input('Введите высоту прямоугольника ')
d, sh = [int(j) for j in input('введите через пробел целочисленные длину и ширину рабочего окна ').split()]
ori = int(input('введите 1, если задаёте многоугольник по часовой стрелке, иначе введите -1 :'))
screen = pygame.display.set_mode((d, sh))
clock = pygame.time.Clock()

def vipukl(coord, ori):
    """ coord - list with starting coordinates of polygon
        ori - ориентация построения многоугольника:
                если ori = 1, следует задавать многоугольник по часовой стрелке,
                если ori = -1, следует задавать против часовой стрелки
    """

    nc = coord.copy()
    kc = []
    z0 = ori
    z1 = 0
    z2 = 0
    l = len(coord)
    for i in range(l):

        AB = [0, 0]
        BC = [0, 0]

        AB[0] = coord[(i+1)%l][0] - coord[i%l][0]
        AB[1] = coord[(i+1)%l][1] - coord[i%l][1]
        BC[0] = coord[(i+2)%l][0] - coord[(i+1)%l][0]
        BC[1] = coord[(i+2)%l][1] - coord[(i+1)%l][1]

        if AB[0]*BC[1] - AB[1]*BC[0] < 0:
            z1 = -1
        elif AB[0]*BC[1] - AB[1]*BC[0] > 0:
            z1 = 1
        elif AB[0]*BC[1] - AB[1]*BC[0] == 0:
            z1 = 0


        if z1*z0 == -1:
            nc.remove(coord[(i+1)%l])
            kc.append(coord[(i+1)%l])
            z2 = 1

    return nc, z2

def coords():
    coord = []
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                '''при нажатии левой кнопки мыши ставит точку, координты точки помещает в список'''
                if event.button == 1:
                    circle(screen, (100, 100, 100), event.pos, 1)
                    s = event.pos
                    coord.append(s)
                    pygame.display.update()
            elif event.type == pygame.KEYDOWN:
                ''' при нажатии пробела рисует многоульник, ждет пару секунд и заверщает цикл'''
                if event.key == pygame.K_SPACE:
                    polygon(screen, (100, 100, 100), coord, 5)
                    pygame.display.update()
                    time.sleep(3)
                    finished = True
    return coord

def tru_v(coor, ori, z =1):
    '''coor - список координат многоугольника
    ori - ориентация вращения (объяснено выше)
    функция возвращает список координат выпуклого многоугольника'''
    while z == 1:
        coor, z = vipukl(coor, ori)
    return coor

def dev_coords(coords):
    '''разбивает список кортежей на координаты х и у. Возвращает 2 списка с иксовыми и игрековыми координатами'''
    x = []
    y = []
    for i in range(len(coords)):
        x.append(coords[i][0])
        y.append(coords[i][1])
    return x, y

'''x1, y1, x2, y2 координаты точек стороны с наибольшей длиной x1<x2
inpolygon - проверяет что точка в многоугольнике
l- длина стороны длинной
w - ширина прямоугольника
h - высота прямоугольника'''

def rect():
    xw = ((w*(x2-x1))/l)
    yw = ((w*(y2-y1))/l)
    xh = -((h*(y2-y1))/l)
    yh = ((h*(x2-x1))/l)
    xt = x1
    yt = y1
    for i in range ((sqrt(d**2+sh**2))//h) :
        while ((xw+x1)<=x2) and ((yw+y1)<=y2):
            if inpolygon(x1+xw+xh, y1+yw+yh, xc, yc)=1 :
                polygon(screen, (255, 255, 255, 175), [(x1,y1),(x1+xw,y1+yw),(x1+xw+xh,y1+yw+yh),(x1+xh,y1+yh)])
            elif inpolygon(x1+xw-xh, y1+yw-yh, xc, yc)=1:
                polygon(screen, (255, 255, 255, 175), [(x1,y1),(x1+xw,y1+yw),(x1+xw-xh,y1+yw-yh),(x1-xh,y1-yh)])
            x1 = x1+xw
            y1 = y1+yw
        if inpolygon(xt+xh,yt+yh, xc, yc)=1:
            xt = xt+xh
            yt = yt+yh
        else:
            xt = xt+xh
            yt = yt+yh
            
t = coords()
newc = tru_v(t, ori)

polygon(screen, (11, 111, 32), newc)
xc, yc = dev_coords(newc)
print(xc, yc)
rect()
pygame.display.update()
clock = pygame.time.Clock()
finished = False




while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
