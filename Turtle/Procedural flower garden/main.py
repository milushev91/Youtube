import turtle          # Import turtle graphics to draw shapes
import colorsys        # Import colorsys to create rainbow colors
import random          # Import random to randomize flower sizes
import math            # Import math for circular flower positions

# --- Screen setup ---
screen = turtle.Screen()            # Create a screen (window) for drawing
screen.bgcolor("black")             # Set background color to black for contrast
screen.setup(width=800, height=600) # Set window size
screen.title("Chill Procedural Flower Garden")  # Window title
turtle.colormode(255)               # Enable RGB color mode (0-255)

# --- Turtle setup ---
t = turtle.Turtle()                 # Create a turtle object (drawing pen)
t.hideturtle()                       # Hide the turtle pointer for a clean look
t.speed(0)                           # Set the fastest drawing speed

# --- Function to generate rainbow colors ---
def rainbow_colors(n):
    """Generate a list of n RGB colors forming a rainbow gradient"""
    colors = []                      # Start with an empty list
    for i in range(n):               # Loop n times
        hue = i / n                  # Calculate hue between 0 and 1
        r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
        colors.append((int(r*255), int(g*255), int(b*255)))  # Add RGB tuple
    return colors                     # Return list of RGB colors

# --- Function to draw a large flower ---
def draw_flower(t, size):
    """Draw a flower with 6 rainbow-colored petals"""
    colors = rainbow_colors(6)       # Generate 6 rainbow colors
    for i in range(6):               # Loop for each petal
        t.color(colors[i])           # Set color for this petal
        t.begin_fill()               # Begin filling the petal
        t.circle(size, 60)           # Draw a 60-degree arc for petal
        t.left(120)                  # Turn to continue petal shape
        t.circle(size, 60)           # Complete second arc of petal
        t.left(60)                   # Reorient turtle for next petal
        t.end_fill()                 # Fill the petal with color

# --- Function to draw a bonsai tree ---
def draw_bonsai_tree(t, trunk_length=80, branch_size=10):
    """Draw a fractal bonsai tree with fixed trunk length and branch size"""
    def tree_recursive(t, length, thickness):
        """Recursive function to draw branches"""
        if length < 10:                     # Stop recursion if branch too short
            return
        t.pensize(max(1, thickness))        # Set branch thickness
        t.color((139,69,19))               # Brown color for trunk/branches
        t.forward(length)                   # Draw the branch

        t.left(30)                           # Turn left for left branch
        tree_recursive(t, length * 0.7, thickness * 0.7)  # Draw left branch

        t.right(60)                          # Turn right for right branch
        tree_recursive(t, length * 0.7, thickness * 0.7)  # Draw right branch

        t.left(30)                           # Restore heading
        t.backward(length)                   # Move back to start of branch

    t.setheading(90)          # Point the turtle upwards
    tree_recursive(t, trunk_length, branch_size)  # Start recursive tree drawing

# --- Positions for three trees (triangle layout) ---
tree_positions = [
    (-250, -100),  # Left tree position (x, y)
    (250, -100),   # Right tree position (x, y)
    (0, 150)       # Top tree position (x, y)
]

# --- Draw the trees ---
for x, y in tree_positions:
    t.penup()           # Lift pen to move without drawing
    t.goto(x, y)        # Move turtle to tree position
    t.pendown()         # Put pen down to start drawing
    draw_bonsai_tree(t, trunk_length=80, branch_size=10)  # Draw the tree

# --- Draw flowers in a circular pattern at center ---
center_x, center_y = 0, 0        # Center point for flower circle
num_flowers = 12                 # Number of flowers in the circle
radius = 100                      # Radius of the circle for flowers
angle_gap = 360 / num_flowers     # Angular gap between each flower

for i in range(num_flowers):
    angle = math.radians(i * angle_gap)       # Convert angle to radians
    flower_x = center_x + radius * math.cos(angle)  # X position on circle
    flower_y = center_y + radius * math.sin(angle)  # Y position on circle
    t.penup()                      # Lift pen to move without drawing
    t.goto(flower_x, flower_y)     # Move turtle to flower position
    t.pendown()                    # Put pen down
    flower_size = random.randint(30, 50)  # Randomize flower size slightly
    draw_flower(t, flower_size)     # Draw the flower

# --- Finish ---
turtle.done()                      # Keep window open until manually closed
