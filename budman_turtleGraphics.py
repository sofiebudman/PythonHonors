from turtle import *

setup(1000,1000)
penup()
goto(480,-380)
pendown()
speed(0)
left(180)
def drawSquare(length):
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)
    forward(length)
    right(90)

size = 15
for i in range(50):
    drawSquare(size)
    size +=15
penup()
goto(-350,350)
pendown()
write('Squares drawn: 50')
hideturtle() 

