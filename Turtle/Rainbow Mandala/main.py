import turtle           # Import the turtle graphics library
import colorsys         # Import colorsys to create rainbow colors

# --- Function to generate rainbow colors ---
def rainbow_colors(n):
    colors = []           # Initialize empty list for colors
    for i in range(n):    # Loop to create n colors
        hue = i / n       # Hue value between 0 and 1
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
        colors.append((int(r*255), int(g*255), int(b*255)))  # Store as RGB tuple
    return colors          # Return the list of colors
  
# --- Screen setup ---
screen = turtle.Screen()          # Create the drawing window
screen.bgcolor("black")           # Set background color to black for contrast
screen.title("Chill Rainbow Mandala")  # Set window title

# --- Turtle setup ---
t = turtle.Turtle()      # Create a turtle object
t.speed(0)               # Set fastest drawing speed
turtle.colormode(255)    # Use 0-255 RGB color range
t.hideturtle()           # Hide the turtle pointer for clean visuals

# --- Parameters for mandala ---
num_petals = 60       # Total number of shapes (petals) in mandala
petal_size = 100      # Length of each petal line
colors = rainbow_colors(num_petals)   # Generate rainbow colors

# --- Draw the mandala ---
for i in range(num_petals):    # Loop over each petal
    t.color(colors[i])          # Set current color from rainbow list
    t.forward(petal_size)       # Draw forward line
    t.right(60)                 # Turn right 60 degrees
    t.forward(petal_size)       # Draw forward line again
    t.right(120)                # Turn right 120 degrees
    t.forward(petal_size)       # Draw forward line
    t.right(60)                 # Turn right 60 degrees
    t.forward(petal_size)       # Draw final line of petal
    t.right(360 / num_petals)   # Rotate slightly to position next petal

# --- Finish drawing ---
turtle.done()       # Keep window open until closed manually
