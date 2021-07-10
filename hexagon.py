from turtle import *
board=Screen()
pen=Turtle()
pen.shape("turtle")
pen.color("red")
pen.begin_fill()
pen.width(20)
for i in range(6):
    pen.forward(100)
    pen.left(60)
done()