import turtle          # Import the turtle graphics library so we can draw shapes
import colorsys        # Import colorsys to generate rainbow colors easily

# --- Screen setup ---
screen = turtle.Screen()            # Create a window for drawing
screen.bgcolor("black")             # Set background color to black for contrast
screen.setup(width=800, height=800) # Set window size to 800x800 pixels
screen.title("Chill Kaleidoscope Pattern")  # Set the window title

# --- Turtle setup ---
t = turtle.Turtle()                 # Create a turtle object (our drawing pen)
t.speed(0)                           # Set drawing speed to the fastest
t.hideturtle()                        # Hide the turtle pointer for clean visuals
turtle.colormode(255)               # Enable RGB colors with values 0-255

# --- Function to generate rainbow colors ---
def rainbow_colors(n):
    """Generate n rainbow colors as RGB tuples"""
    colors = []                       # Start with an empty list
    for i in range(n):                # Loop n times
        hue = i / n                   # Calculate the hue value (0.0 to 1.0)
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
        colors.append((int(r*255), int(g*255), int(b*255)))  # Add RGB tuple to list
    return colors                     # Return the list of colors

# --- Parameters for kaleidoscope ---
num_shapes = 36                      # Number of polygons to draw around the center
num_sides = 6                        # Number of sides per polygon (hexagon)
radius = 100                          # Length of each side
colors = rainbow_colors(num_shapes)   # Generate a rainbow color for each polygon

# --- Draw the kaleidoscope ---
for i in range(num_shapes):          # Repeat for each polygon
    t.pencolor(colors[i])             # Set the pen color for this polygon
    t.penup()                         # Lift pen to move without drawing
    t.home()                           # Move turtle to the center of the screen
    t.pendown()                        # Put pen down to start drawing
    t.setheading(i * (360 / num_shapes))  # Rotate turtle for symmetrical effect

    # --- Draw the polygon ---
    for _ in range(num_sides):        # Repeat for each side of the polygon
        t.forward(radius)             # Draw one side
        t.right(360 / num_sides)      # Turn right to draw the next side

# --- Finish drawing ---
turtle.done()                         # Keep the window open until user closes it
