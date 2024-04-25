import turtle
#turtle = turtle.Turtle()
turtle.screensize(canvwidth =1000,canvheight = 1000)
turtle.penup()
turtle.goto(480,-480)
turtle.pendown()
turtle.speed(0)
turtle.left(180)
def drawSquare(length):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)

size = 15
for i in range(50):
    drawSquare(size)
    size +=15
turtle.penup()
turtle.goto(-400,350)
turtle.pendown()
turtle.write('Squares drawn: 50')
turtle.hideturtle() 
