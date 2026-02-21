# Import the turtle module so we can draw graphics on the screen
import turtle  

# Import the random module to generate random numbers (for random colors)
import random  

# Create a screen (window) where the turtle will draw
screen = turtle.Screen()  

# Create a turtle object (this is our drawing pen)
t = turtle.Turtle()  

# Set the turtle's drawing speed to the fastest (0 is the maximum speed)
t.speed(0)  

# Set the thickness of the pen to 2 pixels
t.width(2)  

# Change color mode to RGB (values from 0 to 255 for Red, Green, Blue)
turtle.colormode(255)  

# Loop from 0 to 360 degrees, increasing by 10 each time
# This means the loop will run 36 times (360 ÷ 10)
for angle in range(0, 360, 10):  

    # Set a random Red, Green, and Blue value (each between 0 and 255)
    # Together, these create a random RGB color for each circle
    t.pencolor(random.randint(0,255),
               random.randint(0,255),
               random.randint(0,255))  

    # Turn the turtle to face the current angle
    t.setheading(angle)  

    # Draw a circle with a radius of 100 pixels
    t.circle(100)  

# Keep the window open until the user closes it manually
turtle.done()  
