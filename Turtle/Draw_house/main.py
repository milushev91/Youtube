import turtle
import time

# ----- Screen Window -----
screen = turtle.Screen() # set up window
screen.bgcolor("light sky blue") # change background color

# Get window dimensions
screen_width = screen.window_width()
screen_height = screen.window_height()

x_left = - screen_width / 2
x_right = screen_width / 2
y_bottom =  - screen_height / 2
y_top = - screen_height / 2

# ---- Starting Position ----
t = turtle.Turtle() # create turtle object
t.speed()
t.penup()
t.goto(x_left, y_bottom)

# ---- Draw grass ---
t.pencolor("lime green")

t.fillcolor("lime green")
t.begin_fill()
t.goto(x_left, y_bottom - 100)
t.forward(screen_width)
t.end_fill()
# ---- Draw house body ----

t.penup()
t.goto(-150, y_bottom + 50)
t.setheading(90)

t.pendown()
t.pensize(2)
t.pencolor("black")
t.fillcolor("seashell")

t.begin_fill()
t.forward(200)
t.setheading(0)
t.forward(300)
t.setheading(270)
t.forward(200)
t.setheading(180)
t.forward(300)
t.end_fill()
