import turtle as t
import time
import random
import math

# =========================
# 🌿 Setup the drawing canvas
# =========================
# Here we configure the window and the turtle so the drawing looks clean and fast
t.title("Hand-Drawn Flower Bush With Naturally Curved Stems")  # Window title
t.bgcolor("navy")   # Background color
t.speed(0)          # Fastest drawing speed
t.width(2)          # Pen width for outlines
t.hideturtle()      # Hide the cursor for better visual

# =========================
# 🌱 Function: draw_stem
# =========================
# Draws a single stem with natural curvature and returns:
# 1) Tip position (x, y) for the flower
# 2) List of points along the stem with their angle, for leaf placement
def draw_stem(start_x, start_y, stem_length=240):
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()

    # Base direction: mostly upwards with slight random tilt
    base_angle = 90 + random.uniform(-10, 10)
    t.setheading(base_angle)
    t.color("green")  # Stem fill color

    stem_step = 3  # Step size for moving forward
    stem_points = []  # Keep track of positions and angles for leaves
    total_steps = stem_length // stem_step

    # Draw stem with smooth sine-wave curvature + tiny hand-drawn wobble
    for i in range(total_steps):
        curve = math.sin(i / 15.0) * 2.5  # Smooth S-shaped wave
        small_random = random.uniform(-0.5, 0.5)  # Hand-drawn imperfection
        t.setheading(base_angle + curve + small_random)
        t.forward(stem_step)
        stem_points.append((t.position(), t.heading()))
        time.sleep(0.002)  # Slow down slightly for smooth animation effect

    # Draw black outline on top of the green stem
    t.penup()
    t.goto(start_x, start_y)
    t.pendown()
    t.color("black")
    t.setheading(base_angle)
    for i in range(total_steps):
        curve = math.sin(i / 15.0) * 2.5
        small_random = random.uniform(-0.5, 0.5)
        t.setheading(base_angle + curve + small_random)
        t.forward(stem_step)

    # Return stem tip and list of points for leaf placement
    return t.position(), stem_points

# =========================
# 🍃 Function: draw_leaf
# =========================
# Draws a single leaf at a given point along the stem, angled naturally
def draw_leaf(x, y, stem_angle):
    # Decide if the leaf sprouts left or right, with small randomness
    leaf_angle = stem_angle + random.choice([-40, 40]) + random.uniform(-5, 5)

    # Draw green leaf
    t.penup()
    t.goto(x, y)
    t.setheading(leaf_angle)
    t.pendown()
    t.begin_fill()
    t.color("green")
    for _ in range(2):
        t.circle(22, 90)  # Big curve
        t.circle(10, 90)  # Small curve
    t.end_fill()

    # Draw black outline for realism
    t.penup()
    t.goto(x, y)
    t.setheading(leaf_angle)
    t.pendown()
    t.color("black")
    for _ in range(2):
        t.circle(22, 90)
        t.circle(10, 90)

# =========================
# 🌹 Function: draw_wobbly_petal
# =========================
# Draws a single petal with slight wobble to mimic hand-drawn style
def draw_wobbly_petal(radius, angle):
    # Fill red
    t.begin_fill()
    t.color("red")
    for _ in range(2):
        t.circle(radius + random.uniform(-2,2), angle + random.uniform(-3,3))
        t.left(180 - angle + random.uniform(-3,3))
    t.end_fill()

    # Outline in black
    t.color("black")
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

# =========================
# 🌸 Function: draw_flower
# =========================
# Draws a full flower at the tip of a stem:
# - Multiple layers of petals
# - Inner swirl to mimic rose curl
def draw_flower(flower_x, flower_y):
    t.penup()
    t.goto(flower_x, flower_y)
    t.setheading(0)
    t.pendown()

    # Multiple petal layers with increasing radius
    layers = [
        (18, 60, 6),
        (25, 80, 6),
        (32, 100, 6),
    ]
    for radius, angle, count in layers:
        for _ in range(count):
            draw_wobbly_petal(radius, angle)
            t.left(360 / count)

    # Inner swirl (dark red)
    t.penup()
    t.goto(flower_x, flower_y + 25)
    t.pendown()
    t.color("darkred")
    for i in range(10):
        t.circle(5 + i, 30)
        t.left(15)

    # Outline of inner swirl
    t.penup()
    t.goto(flower_x, flower_y + 25)
    t.pendown()
    t.color("black")
    for i in range(10):
        t.circle(5 + i, 30)
        t.left(15)

# =========================
# 🌹 Main Rose Bush Drawing
# =========================
# Define starting positions for multiple stems
stem_positions = [(-120, -220), (-60, -240), (0, -230), (70, -250), (130, -230)]

for pos in stem_positions:
    # Draw stem and capture tip & points along stem
    tip_pos, stem_points = draw_stem(pos[0], pos[1], stem_length=random.randint(180, 240))
    tip_x, tip_y = tip_pos

    # Attach 2-4 leaves along the stem
    leaf_count = random.randint(2, 4)
    if len(stem_points) >= leaf_count + 20:  # Avoid extreme top/bottom
        selected_points = random.sample(stem_points[20:-10], leaf_count)
        for point, heading in selected_points:
            draw_leaf(point[0], point[1], heading)

    # Draw flower at stem tip
    draw_flower(tip_x, tip_y)

# =========================
# ✨ Add Signature
# =========================
t.penup()
t.goto(-180, -300)
t.color("white")
t.pendown()
t.write("Hand-Drawn Flower Bush (Curved Stems & Natural Leaves)", font=("Arial", 16, "bold"))

t.done()
