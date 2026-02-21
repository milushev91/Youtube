import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

turtle.colormode(255)

for angle in range(0, 360, 10):
    t.pencolor(random.randint(0,255),
               random.randint(0,255),
               random.randint(0,255))
    t.setheading(angle)
    t.circle(100)

turtle.done()
