from turtle import *
board=Screen()
pen=Turtle()
pen.shape("turtle")
pen.color("red")
pen.begin_fill()
pen.width(20)
for i in range(4):
    pen.forward(200)
    pen.left(90)
pen.fillcolor("yellow")
pen.end_fill()

pen.penup()
pen.goto(-100,100)
pen.pendown()
pen.circle(50)

done()