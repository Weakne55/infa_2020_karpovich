import turtle as t

print('Write your index')

index=input()
A=list(index)
for i in range(len(A)):
    A[i]=int(A[i])

t.shape('turtle')
t.penup()
t.left(180)
t.forward(475)
t.left(180)
t.pendown()

def num (name):

        if name == 1:
            t.penup()
            t.right(90)
            t.forward(50)
            t.pendown()
            t.left(135)
            t.forward(70.7)
            t.right(135)
            t.forward(100)
            t.right(180)
            t.forward(100)
            t.right(90)
            t.penup()
            t.forward(50)
            t.pendown()
        elif name == 2:
            t.forward(50)
            t.right(90)
            t.forward(50)
            t.right(45)
            t.forward(70.7)
            t.left(135)
            t.forward(50)
            t.left(90)
            t.penup()
            t.forward(100)
            t.right(90)
            t.penup()
            t.forward(50)
            t.pendown()
        elif name == 3:
           t.forward(50)
           t.right(135)
           t.forward(70.7)
           t.left(135)
           t.forward(50)
           t.right(135)
           t.forward(70.7)
           t.right(135)
           t.penup()
           t.forward(100)
           t.right(90)
           t.forward(100)
           t.pendown()
        elif name == 4:
           t.right(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.right(90)
           t.forward(50)
           t.right(180)
           t.forward(100)
           t.right(90)
           t.penup()
           t.forward(50)
           t.pendown()
        elif name == 5:
           t.right(90)
           t.penup()
           t.forward(100)
           t.left(90)
           t.pendown()
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.right(90)
           t.forward(50)
           t.right(90)
           t.forward(50)
           t.penup()
           t.forward(50)
           t.pendown()
        elif name == 6:
           t.right(90)
           t.penup()
           t.forward(50)
           t.pendown()
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.right(135)
           t.forward(70.7)
           t.right(45)
           t.penup()
           t.forward(50)
           t.pendown()
        elif name == 7:
           t.forward(50)
           t.right(135)
           t.forward(70.7)
           t.left(45)
           t.forward(50)
           t.right(180)
           t.penup()
           t.forward(100)
           t.right(90)
           t.forward(100)
           t.pendown()
        elif name == 8:
           t.right(90)
           t.forward(100)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(180)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(180)
           t.penup()
           t.forward(100)
           t.pendown()
        elif name == 9:
           t.right(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.penup()
           t.forward(100)
           t.pendown()
           t.left(135)
           t.forward(70.7)
           t.left(45)
           t.forward(50)
           t.right(90)
           t.penup()
           t.forward(50)
           t.pendown()
        elif name == 0:
           t.right(90)
           t.forward(100)
           t.left(90)
           t.forward(50)
           t.left(90)
           t.forward(100)
           t.left(90)
           t.forward(50)
           t.left(180)
           t.penup()
           t.forward(100)
           t.pendown()

print(len(A))

c=len(A)

for i in range(len(A)):
    num(A[i])