import turtle          # Import the turtle graphics library
import colorsys# Import colorsys (not strictly needed here but useful for gradients)
import time            # Import time (can be used for animation if desired)

# --- Screen setup ---
screen = turtle.Screen()             # Create the drawing window
screen.bgcolor("black")              # Set background to black for contrast
screen.title("Realistic Fractal Tree")  # Set the window title

# --- Turtle setup ---
t = turtle.Turtle()                  # Create a turtle object
t.speed(0)                           # Set turtle to fastest speed
t.hideturtle()                        # Hide the turtle pointer for clean visuals
turtle.colormode(255)                # Use RGB color mode (0-255)

# --- Recursive function for realistic fractal tree ---
def realistic_tree(t, branch_length, angle, thickness, max_depth, depth=0):
    """
    Draws a realistic fractal tree.
    - branch_length: length of the current branch
    - angle: branching angle
    - thickness: pen size for the branch
    - max_depth: maximum recursion depth
    - depth: current recursion depth
    """
    if branch_length < 10:            # Stop recursion when branch is too small
        return

    # --- Determine branch color ---
    if depth < max_depth * 0.6:       # First ~60% of tree is brown
        color = (139, 69, 19)         # Brown color for trunk/branches
    else:                             # Last ~40% is green for leaves
        green_intensity = int(150 + 105 * ((depth - max_depth * 0.6)/(max_depth*0.4)))
        color = (34, green_intensity, 34)   # Gradient green color

    t.pensize(int(thickness))         # Set branch thickness
    t.color(color)                    # Set branch color
    t.forward(branch_length)          # Draw the branch forward

    # --- Left branch ---
    t.left(angle)                     # Turn left by branching angle
    realistic_tree(t, branch_length * 0.7, angle, thickness * 0.7, max_depth, depth + 1)
                        # Recursively draw left subtree, shorten length and thickness

    # --- Right branch ---
    t.right(2 * angle)                # Turn right to draw right branch
    realistic_tree(t, branch_length * 0.7, angle, thickness * 0.7, max_depth, depth + 1)
                                      # Recursively draw right subtree

    # --- Restore original position ---
    t.left(angle)                     # Turn back to original direction
    t.backward(branch_length)         # Move back to branch starting point

# --- Starting position for the tree ---
t.penup()                            # Lift pen to move without drawing
t.goto(0, -300)                      # Move turtle near bottom center of screen
t.pendown()                          # Place pen down to start drawing
t.left(90)                            # Point turtle upwards

# --- Tree parameters ---
initial_branch_length = 180          # Starting trunk length
initial_thickness = 15               # Starting trunk thickness
angle = 25                            # Branching angle
max_depth = 10                    # Controls recursion depth and color transition

# --- Draw the realistic tree ---
realistic_tree(t, initial_branch_length, angle, initial_thickness, max_depth)

# --- Finish ---
turtle.done()                         # Keep the window open until manually closed
