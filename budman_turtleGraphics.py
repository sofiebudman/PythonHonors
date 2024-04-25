from turtle import *

setup(1000,1000)
penup()
goto(480,-480)
pendown()
speed(0)
def drawSquare(length):
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)
    forward(length)
    left(90)

size = 15
for i in range(50):
    drawSquare(size)
    size +=15
    print(size)
    

