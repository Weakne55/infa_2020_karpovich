import pygame
from pygame.draw import *
import time
import math

pygame.init()
FPS = 30
x, y = [int(j) for j in input('введите через пробел целочисленные длину и ширину рабочего окна').split()]
ori = int(input('введите 1, если задаёте многоугольник по часовой стрелке, иначе введите -1'))
screen = pygame.display.set_mode((x, y))
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

def tru_v(coor, ori, z = 1):
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

t = coords()
newc = tru_v(t, ori)
polygon(screen, (11, 111, 32), newc)
x_coor, y_coor = dev_coords(newc)


#поиск длин сторон
def side (x,y):
    length=[]
    for i in range(len(x)):
        length.append(math.sqrt((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2))
    return int(max(length))

#поиск координат самой длинной стороны
def points(max,x,y):
    x0=0
    y0=0
    x1=0
    x2=0
    y1=0
    y2=0
    auxiliary_arr = []

    for i in range(len(x)):
        auxiliary_arr.append(math.sqrt((x[i] - x[i - 1]) ** 2 + (y[i] - y[i - 1]) ** 2))
        if max == int(auxiliary_arr[i]):
            x1 = x[i]
            x2 = x[i-1]
            y1 = y[i]
            y2 = y[i - 1]
            if x1 > x2:
                x0=x2
                x2=x1
                x1=x0
                y0 = y2
                y2 = y1
                y1 = y0
    return x1,x2,y1,y2


print(points(side(x_coor,y_coor),x_coor,y_coor))
''' эти две строчки можно стереть они нужны были для проверки'''
print(x_coor, y_coor)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()