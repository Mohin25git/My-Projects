import turtle # Our friendly drawing robot
import math   # For angles, sin/cos — feathers need curves!
import random # For organic randomness (nature hates perfection)
import time   # For smooth animation pacing

# -------------------- SETUP --------------------
screen = turtle.Screen()
screen.bgcolor("black")   # Dark background makes colors glow beautifully
screen.title("Peacock Fanning-out Animation")

pen = turtle.Turtle()
pen.hideturtle()          # Hide the triangle cursor — artistic invisibility
pen.speed(0)              # Fastest drawing speed
pen.pensize(2)            # Default line thickness for stems & outlines

screen.tracer(0, 0)       # Manual control of animation frames → smoother

BASE_X, BASE_Y = 0, -220  # The "root" where all stems sprout from
TOTAL_ANIMATION_TIME = 25 # Animation must finish in exactly 25 seconds

# -------------------- COLOR VARIATION --------------------
def vary_color(hex_color, shift=10):
    """
    Slightly wiggle the given color → creates natural variation.
    Think of leaves in sunlight: never the exact same shade.
    """
    hex_color = hex_color.lstrip("#") # Remove '#' if present

    # Extract R, G, B from hex
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    # Ensure values never exceed 0–255
    clamp = lambda x: max(0, min(255, x))

    # Randomly shift each color channel slightly
    r = clamp(r + random.randint(-shift, shift))
    g = clamp(g + random.randint(-shift, shift))
    b = clamp(b + random.randint(-shift, shift))

    # Repackage into hex string
    return f"#{r:02x}{g:02x}{b:02x}"

# -------------------- DRAW ROTATED ELLIPSE --------------------
def draw_rotated_ellipse(cx, cy, rx, ry, angle_deg, color):
    """
    Draws a filled ellipse rotated by angle_deg around (cx, cy).
    Used for peacock eye layers.
    """
    angle_rad = math.radians(angle_deg) # Convert degrees → radians
    steps = 120                         # More steps = smoother ellipse

    # Outline is black, fill is lightly varied color
    pen.color("black", vary_color(color, 5))

    pen.penup()
    ellipse_points = []

    # Generate ellipse perimeter points
    for i in range(steps + 1):
        t = 2 * math.pi * i / steps # Angle around ellipse
        x = rx * math.cos(t)        # Horizontal ellipse coordinate
        y = ry * math.sin(t)        # Vertical ellipse coordinate

        # Rotate point by angle_rad
        xr = x * math.cos(angle_rad) - y * math.sin(angle_rad)
        yr = x * math.sin(angle_rad) + y * math.cos(angle_rad)

        ellipse_points.append((cx + xr, cy + yr))

    # Draw the filled ellipse
    pen.goto(ellipse_points[0])
    pen.pendown()
    pen.begin_fill()

    for p in ellipse_points:
        pen.goto(p)

    pen.end_fill()
    pen.penup()

# -------------------- DRAW CURVED STEM --------------------
def draw_curved_stem(length, spread_angle, delay_per_step):
    """
    Grows a stem upward with a natural curve and wobble.
    Returns:
    - final tip position
    - heading angle
    - list of points along the stem (for barb placement)
    """
    pen.penup()
    pen.goto(BASE_X, BASE_Y)               # Start at stem root
    pen.setheading(90 + spread_angle)      # Tilt left/right depending on angle
    pen.color(vary_color("#2ECC71", 20)) # Fresh leafy green
    pen.pensize(3)
    pen.pendown()

    points = []                     # To store stem path
    step = 3                        # Each growth step = 3 pixels
    curvature = spread_angle * 0.18 # Curvature factor
    steps = int(length / step)      # How many steps needed

    # ---- Grow the stem with wobble ----
    for i in range(steps):

        wobble = random.uniform(-0.35, 0.35)   # Tiny left-right jitter → organic feel
        pen.left((curvature / steps) + wobble) # Soft curve + wobble
        pen.forward(step)                      # Growth!
        points.append(pen.position())          # Save position for barbs

        # Ease-out timing → slows slightly as it grows upward
        eased_delay = delay_per_step * (1 + 0.5 * (i / steps))

        # Update screen occasionally
        if i % 3 == 0:
            screen.update()
            time.sleep(eased_delay)

    # ---- Add tiny micro texture strokes along stem ----
    pen.pensize(1)
    pen.color(vary_color("#1e8449", 10))

    for j in range(0, len(points), 12): # Every few steps
        x, y = points[j]
        if j < len(points) - 1:
            nx, ny = points[j + 1]

            # Direction of this stem segment
            local_heading = math.degrees(math.atan2(ny - y, nx - x))

            pen.penup()
            pen.goto(x, y)
            pen.setheading(local_heading + random.uniform(-10, 10))
            pen.pendown()

            flick = random.uniform(4, 6) # Short flick stroke
            pen.forward(flick)

        pen.penup()

    return pen.position(), pen.heading(), points

# -------------------- DRAW BARBS --------------------
def draw_barbs(points, barb_len, delay_per_step):
    """
    Draws fine hair-like barbs on BOTH sides of the stem.
    Balanced, natural, and slightly curly.
    """
    pen.pensize(1)

    # Skip first/last 10 points to avoid weird end-effects
    for i in range(10, len(points)-10):

        x, y = points[i]
        nx, ny = points[i + 1]

        # Local stem direction at this point
        local_heading = math.degrees(math.atan2(ny - y, nx - x))

        wobble = random.uniform(-4, 4) # Organic asymmetry

        # Perpendicular directions
        left_angle  = local_heading + 90 + wobble
        right_angle = local_heading - 90 + wobble * 0.85

        # Taper barb length as we go upward
        scale = 1 - (i / len(points))
        bl = barb_len * scale * 1.10
        bl += random.uniform(-1.5, 1.5)        # Slight size variety

        pen.color(vary_color("#27ae60", 18)) # Natural green with variation

        # ---- LEFT BARB ----
        pen.penup()
        pen.goto(x, y)
        pen.setheading(left_angle)
        pen.pendown()

        curl_strength = random.uniform(-2.5, 2.5)
        for _ in range(3):
            pen.forward(bl / 3)
            pen.left(curl_strength * 0.3 + random.uniform(-0.2, 0.2))
        pen.penup()

        # ---- RIGHT BARB ----
        pen.goto(x, y)
        pen.setheading(right_angle)
        pen.pendown()

        curl_strength = random.uniform(-2.5, 2.5)
        for _ in range(3):
            pen.forward(bl / 3)
            pen.right(curl_strength * 0.3 + random.uniform(-0.2, 0.2))
        pen.penup()

        # Occasionally update frame
        if i % 6 == 0:
            screen.update()
            time.sleep(delay_per_step)

# -------------------- DRAW EYE --------------------
def draw_eye(cx, cy, angle, scale, delay_per_step):
    """
    Draws the 'peacock eye feather':
    A stack of 5 ellipses with shimmering colors and size variation.
    """
    layers = [
        (55*scale, 30*scale, "#19D3C5"), # Outer aqua glow
        (44*scale, 24*scale, "#4472C4"), # Blue layer
        (32*scale, 18*scale, "#7030A0"), # Purple core
        (20*scale, 10*scale, "#FFC000"), # Golden ring
        (10*scale, 5*scale, "#002060")   # Dark pupil
    ]

    angle += random.uniform(-1, 1)         # Natural tilt jitter

    # Draw each ellipse layer
    for index, (rx, ry, col) in enumerate(layers):

        rx *= random.uniform(0.96, 1.04)   # Slight size variation
        ry *= random.uniform(0.96, 1.04)

        # Tiny positional jitter → painterly look
        cx_j = cx + random.uniform(-1.2, 1.2)
        cy_j = cy + random.uniform(-1.2, 1.2)

        # More inner layers = stronger color variation
        adjusted_color = vary_color(col, shift=6 + index * 3)

        draw_rotated_ellipse(cx_j, cy_j, rx, ry, angle, adjusted_color)

        screen.update()
        time.sleep(delay_per_step * 3)

# -------------------- DRAW PEACOCK BODY --------------------
def draw_peacock_body(delay_per_step):
    """
    Draws the peacock body in front of the fan:
    - Rounded body
    - Curved neck
    - Small head with crown
    - Beak
    Positioned at the base where feathers sprout from.
    """
    # Body position - slightly forward from base
    body_x, body_y = BASE_X, BASE_Y + 15
    
    # ---- Draw Body with Clean Gradient and Chest Band ----
    body_rx, body_ry = 35, 50
    steps = 80
    
    # Draw full body base in purple (lower body) - no outline
    pen.penup()
    pen.color(vary_color("#7030A0", 10), vary_color("#7030A0", 10))  # Rich purple, same for fill and outline
    pen.goto(body_x, body_y - body_ry)
    pen.pendown()
    pen.begin_fill()
    
    # Draw complete ellipse for lower body
    for i in range(steps + 1):
        t = 2 * math.pi * i / steps
        x = body_x + body_rx * math.cos(t)
        y = body_y + body_ry * math.sin(t)
        if i == 0:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)
    
    pen.end_fill()
    pen.penup()
    
    # Draw upper body section in blue (clean overlay) - no outline
    pen.color(vary_color("#0066CC", 10), vary_color("#0066CC", 10))  # Deep blue, same for fill and outline
    pen.goto(body_x, body_y + body_ry)
    pen.pendown()
    pen.begin_fill()
    
    # Draw upper portion of ellipse (from top to middle)
    transition_y = body_y + 5  # Smooth transition point
    
    # Top half of ellipse
    for i in range(steps // 2 + 1):
        t = math.pi * i / (steps // 2)  # 0 to pi (top half)
        x = body_x + body_rx * math.cos(t)
        y = body_y + body_ry * math.sin(t)
        if i == 0:
            pen.goto(x, y)
        else:
            pen.goto(x, y)
    
    # Draw straight line across the transition
    pen.goto(body_x - body_rx, transition_y)
    pen.goto(body_x + body_rx, transition_y)
    pen.goto(body_x, body_y + body_ry)
    
    pen.end_fill()
    pen.penup()
    
    # Draw golden chest band (clean horizontal band) - no outline
    pen.color(vary_color("#FFC000", 8), vary_color("#FFC000", 8))  # Golden chest band, same for fill and outline
    chest_band_y = body_y + 8
    chest_band_height = 16
    chest_band_width = body_rx * 1.6  # Slightly wider than body
    
    # Draw chest band as a clean curved rectangle
    pen.goto(body_x - chest_band_width/2, chest_band_y + chest_band_height/2)
    pen.pendown()
    pen.begin_fill()
    
    # Top curve
    for i in range(20):
        t = i / 20
        x = body_x - chest_band_width/2 + chest_band_width * t
        y = chest_band_y + chest_band_height/2 - (chest_band_height/2) * (t * (1-t) * 4)  # Slight curve
        pen.goto(x, y)
    
    # Right side
    pen.goto(body_x + chest_band_width/2, chest_band_y - chest_band_height/2)
    
    # Bottom curve
    for i in range(20, 0, -1):
        t = i / 20
        x = body_x - chest_band_width/2 + chest_band_width * t
        y = chest_band_y - chest_band_height/2 + (chest_band_height/2) * ((1-t) * t * 4)  # Slight curve
        pen.goto(x, y)
    
    # Left side
    pen.goto(body_x - chest_band_width/2, chest_band_y + chest_band_height/2)
    
    pen.end_fill()
    pen.penup()
    
    # Draw clean body outline ONCE at the end
    pen.color("black")
    pen.pensize(2)
    pen.goto(body_x, body_y - body_ry)
    pen.pendown()
    
    # Draw full body outline
    for i in range(steps + 1):
        t = 2 * math.pi * i / steps
        x = body_x + body_rx * math.cos(t)
        y = body_y + body_ry * math.sin(t)
        if i == 0:
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
        else:
            pen.goto(x, y)
    
    pen.penup()
    screen.update()
    time.sleep(delay_per_step * 5)
    
    # ---- Draw Wings (outline curves on sides) ----
    # Left wing - filled with orangish-yellow (larger and more visible)
    wing_left_start_x = body_x - 28
    wing_left_start_y = body_y + 8
    wing_left_peak_x = body_x - 55  # Extended further out
    wing_left_peak_y = body_y + 20  # Higher peak
    wing_left_end_x = body_x - 48   # Extended further out
    wing_left_end_y = body_y - 15   # Lower end for larger wing
    
    # Draw filled left wing
    pen.color("black", vary_color("#FF8C00", 12))  # Orangish-yellow fill (less variation for more visibility)
    pen.pensize(3)  # Thicker outline
    pen.penup()
    
    # Create wing shape points for filling
    wing_left_points = []
    wing_steps = 35  # More steps for smoother curve
    for i in range(wing_steps + 1):
        t = i / wing_steps
        # Quadratic bezier curve
        x = (1-t)**2 * wing_left_start_x + 2*(1-t)*t * wing_left_peak_x + t**2 * wing_left_end_x
        y = (1-t)**2 * wing_left_start_y + 2*(1-t)*t * wing_left_peak_y + t**2 * wing_left_end_y
        wing_left_points.append((x, y))
    
    # Add connection points to body for closed shape (wider connection)
    wing_left_points.insert(0, (body_x - 28, body_y + 8))
    wing_left_points.append((body_x - 22, body_y - 8))
    wing_left_points.append((body_x - 28, body_y + 8))
    
    # Draw filled wing
    pen.goto(wing_left_points[0])
    pen.pendown()
    pen.begin_fill()
    for p in wing_left_points:
        pen.goto(p)
    pen.end_fill()
    pen.penup()
    
    # Right wing - filled with orangish-yellow (larger and more visible)
    wing_right_start_x = body_x + 28
    wing_right_start_y = body_y + 8
    wing_right_peak_x = body_x + 55  # Extended further out
    wing_right_peak_y = body_y + 20  # Higher peak
    wing_right_end_x = body_x + 48   # Extended further out
    wing_right_end_y = body_y - 15   # Lower end for larger wing
    
    # Draw filled right wing
    pen.color("black", vary_color("#FF8C00", 12))  # Orangish-yellow fill
    pen.pensize(3)  # Thicker outline
    pen.penup()
    
    # Create wing shape points for filling
    wing_right_points = []
    for i in range(wing_steps + 1):
        t = i / wing_steps
        # Quadratic bezier curve
        x = (1-t)**2 * wing_right_start_x + 2*(1-t)*t * wing_right_peak_x + t**2 * wing_right_end_x
        y = (1-t)**2 * wing_right_start_y + 2*(1-t)*t * wing_right_peak_y + t**2 * wing_right_end_y
        wing_right_points.append((x, y))
    
    # Add connection points to body for closed shape (wider connection)
    wing_right_points.insert(0, (body_x + 28, body_y + 8))
    wing_right_points.append((body_x + 22, body_y - 8))
    wing_right_points.append((body_x + 28, body_y + 8))
    
    # Draw filled wing
    pen.goto(wing_right_points[0])
    pen.pendown()
    pen.begin_fill()
    for p in wing_right_points:
        pen.goto(p)
    pen.end_fill()
    pen.penup()
    
    # Add feather detail lines on each wing (darker orangish-yellow, more visible)
    pen.pensize(2)  # Thicker detail lines
    pen.color(vary_color("#FF6B00", 8))  # Darker orangish-yellow for detail lines
    
    # Left wing feather lines (more lines, longer)
    for i in range(5):  # More feather lines
        t = 0.2 + i * 0.15  # Position along wing curve
        x = (1-t)**2 * wing_left_start_x + 2*(1-t)*t * wing_left_peak_x + t**2 * wing_left_end_x
        y = (1-t)**2 * wing_left_start_y + 2*(1-t)*t * wing_left_peak_y + t**2 * wing_left_end_y
        
        # Draw short line perpendicular to wing curve
        angle = math.degrees(math.atan2(
            (wing_left_peak_y - wing_left_start_y) * (1-t) + (wing_left_end_y - wing_left_peak_y) * t,
            (wing_left_peak_x - wing_left_start_x) * (1-t) + (wing_left_end_x - wing_left_peak_x) * t
        ))
        perp_angle = angle + 90
        
        pen.goto(x, y)
        pen.setheading(perp_angle)
        pen.pendown()
        pen.forward(7 + random.uniform(-1, 1))  # Longer feather lines
        pen.penup()
    
    # Right wing feather lines (more lines, longer)
    for i in range(5):  # More feather lines
        t = 0.2 + i * 0.15  # Position along wing curve
        x = (1-t)**2 * wing_right_start_x + 2*(1-t)*t * wing_right_peak_x + t**2 * wing_right_end_x
        y = (1-t)**2 * wing_right_start_y + 2*(1-t)*t * wing_right_peak_y + t**2 * wing_right_end_y
        
        # Draw short line perpendicular to wing curve
        angle = math.degrees(math.atan2(
            (wing_right_peak_y - wing_right_start_y) * (1-t) + (wing_right_end_y - wing_right_peak_y) * t,
            (wing_right_peak_x - wing_right_start_x) * (1-t) + (wing_right_end_x - wing_right_peak_x) * t
        ))
        perp_angle = angle - 90
        
        pen.goto(x, y)
        pen.setheading(perp_angle)
        pen.pendown()
        pen.forward(7 + random.uniform(-1, 1))  # Longer feather lines
        pen.penup()
    
    screen.update()
    time.sleep(delay_per_step * 3)
    
    # ---- Draw Neck (curved S-shape) ----
    pen.color(vary_color("#0066CC", 12))
    pen.pensize(8)
    pen.goto(body_x, body_y + 25)  # Top of body
    pen.pendown()
    
    # Curved neck upward
    neck_points = []
    for i in range(25):
        t = i / 25
        # S-curve using sine
        curve = math.sin(t * math.pi) * 8
        x = body_x + curve
        y = body_y + 25 + i * 3.5
        pen.goto(x, y)
        neck_points.append((x, y))
        if i % 5 == 0:
            screen.update()
            time.sleep(delay_per_step * 0.5)
    
    # Get neck end point
    neck_end_x, neck_end_y = neck_points[-1]
    
    pen.penup()
    
    # ---- Draw Head (refined oval shape) ----
    # Position head so bottom connects to neck (head center is above neck end)
    head_rx, head_ry = 14, 11  # Slightly wider head
    
    # Head center should be positioned so bottom of head (head_y - head_ry) connects to neck
    # Add small overlap to ensure connection
    head_x = neck_end_x
    head_y = neck_end_y + head_ry - 2  # Position head so bottom overlaps neck slightly
    
    # Fine-tuned head: slightly oval, better proportions
    pen.color("black", vary_color("#0066CC", 10))
    pen.penup()
    
    # Draw head as a refined ellipse (wider than tall)
    head_steps = 60
    head_points = []
    for i in range(head_steps + 1):
        t = 2 * math.pi * i / head_steps
        x = head_x + head_rx * math.cos(t)
        y = head_y + head_ry * math.sin(t)
        head_points.append((x, y))
    
    pen.goto(head_points[0])
    pen.pendown()
    pen.begin_fill()
    for p in head_points:
        pen.goto(p)
    pen.end_fill()
    pen.penup()
    
    # Draw a small connection segment to ensure smooth transition
    # Extend neck slightly into head area
    pen.color(vary_color("#0066CC", 10))
    pen.pensize(6)  # Slightly thinner than main neck
    pen.goto(neck_end_x, neck_end_y)
    pen.pendown()
    pen.goto(head_x, head_y - head_ry + 3)  # Connect to bottom of head
    pen.penup()
    
    screen.update()
    time.sleep(delay_per_step * 3)
    
    # ---- Draw Crown/Crest (refined, more elegant) ----
    pen.color(vary_color("#FFD700", 20))  # Golden crown
    pen.pensize(2)
    crown_base_x, crown_base_y = head_x, head_y + 8
    
    # Three main crown feathers with slight variation
    for i in range(3):
        angle_offset = -15 + i * 15  # -15, 0, 15 degrees
        pen.goto(crown_base_x, crown_base_y)
        pen.setheading(90 + angle_offset)
        pen.pendown()
        
        # Crown feather with slight curve
        feather_len = 10 + random.uniform(-1, 1)
        for step in range(3):
            pen.forward(feather_len / 3)
            pen.left(2 if step < 1 else -1)  # Slight curve
        
        pen.penup()
    
    screen.update()
    time.sleep(delay_per_step * 2)
    
    # ---- Draw Beak (refined, more bird-like) ----
    beak_base_x, beak_base_y = head_x + 12, head_y - 1
    
    # Upper beak
    pen.color("black", vary_color("#FFA500", 5))  # Orange beak
    pen.pensize(2)
    pen.goto(beak_base_x, beak_base_y)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    pen.forward(7)
    pen.left(135)
    pen.forward(5)
    pen.left(45)
    pen.forward(4)
    pen.end_fill()
    pen.penup()
    
    # Lower beak (smaller)
    pen.goto(beak_base_x + 2, beak_base_y - 2)
    pen.setheading(0)
    pen.pendown()
    pen.begin_fill()
    pen.forward(5)
    pen.left(120)
    pen.forward(3)
    pen.left(60)
    pen.forward(3)
    pen.end_fill()
    pen.penup()
    
    # ---- Draw Eye (refined, more detailed) ----
    eye_x, eye_y = head_x + 5, head_y + 3
    
    # Eye white
    pen.color("white")
    pen.goto(eye_x, eye_y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(3)
    pen.end_fill()
    pen.penup()
    
    # Eye iris (colored ring)
    pen.color(vary_color("#FFD700", 10))  # Golden iris
    pen.goto(eye_x, eye_y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(2)
    pen.end_fill()
    pen.penup()
    
    # Eye pupil
    pen.color("black")
    pen.goto(eye_x, eye_y)
    pen.pendown()
    pen.begin_fill()
    pen.circle(1.5)
    pen.end_fill()
    pen.penup()
    
    # Eye highlight (tiny white dot)
    pen.color("white")
    pen.goto(eye_x + 0.5, eye_y + 0.5)
    pen.pendown()
    pen.begin_fill()
    pen.circle(0.5)
    pen.end_fill()
    pen.penup()
    
    screen.update()
    time.sleep(delay_per_step * 2)
    
    # ---- Draw Legs with Toes/Claws ----
    pen.color(vary_color("#FFA500", 10))  # Orange legs
    pen.pensize(3)
    
    for leg_x in [body_x - 12, body_x + 12]:
        leg_start_y = body_y - 45
        leg_end_y = leg_start_y - 15
        
        # Draw leg
        pen.goto(leg_x, leg_start_y)
        pen.pendown()
        pen.setheading(270)
        pen.forward(15)
        pen.penup()
        
        # Draw foot with toes
        foot_x = leg_x
        foot_y = leg_end_y
        
        # Main foot structure (small oval)
        pen.color("black", vary_color("#FFA500", 8))
        pen.goto(foot_x, foot_y - 2)
        pen.pendown()
        pen.begin_fill()
        pen.setheading(0)
        pen.forward(3)
        pen.left(90)
        pen.forward(4)
        pen.left(90)
        pen.forward(3)
        pen.left(90)
        pen.forward(4)
        pen.end_fill()
        pen.penup()
        
        # Draw 3 toes per foot (typical bird foot)
        pen.color(vary_color("#FF8C00", 5))  # Slightly darker orange for toes
        pen.pensize(2)
        
        # Toe angles: forward, left, right
        toe_angles = [0, -25, 25]
        
        for toe_angle in toe_angles:
            pen.goto(foot_x, foot_y)
            pen.setheading(270 + toe_angle)
            pen.pendown()
            
            # Draw toe with claw
            toe_length = 6 + random.uniform(-0.5, 0.5)
            pen.forward(toe_length)
            
            # Draw small claw at tip
            pen.left(30)
            pen.forward(2)
            pen.backward(2)
            pen.right(60)
            pen.forward(2)
            pen.backward(2)
            pen.left(30)
            
            pen.penup()
        
        screen.update()
        time.sleep(delay_per_step * 1)
    
    screen.update()

# -------------------- DRAW FAN --------------------
def draw_fan():
    """
    Draws the full 6-feather peacock fan:
    - Curved stems
    - Barbs
    - Eye feathers
    All placed symmetrically with organic variation.
    """
    angles = [-55, -32, -12, 12, 32, 55] # Spread-out fan angles

    # Longer stems in the center, shorter on sides → natural fan
    stem_lengths = [
        205 if abs(a) < 12 else
        185 if abs(a) < 40 else
        170
        for a in angles
    ]

    # Total steps across all stems → create time per step
    total_steps = sum([int(l/3) for l in stem_lengths])
    delay_per_step = TOTAL_ANIMATION_TIME / total_steps

    # Draw each feather in the fan
    for idx, ang in enumerate(angles):

        stem_len = stem_lengths[idx]

        # GROW THE STEM
        tip, heading, pts = draw_curved_stem(stem_len, ang, delay_per_step)

        # Draw barbs along it
        barb_len = 30 - (abs(ang) / 55) * 10
        draw_barbs(pts, barb_len, delay_per_step)

        # Compute feather-eye position beyond tip
        offset = 40
        rad = math.radians(heading)
        eye_x = tip[0] + math.cos(rad) * offset
        eye_y = tip[1] + math.sin(rad) * offset

        # Tilt eyes slightly inward → aesthetic symmetry
        tilt = -7 * math.copysign(1, ang) if ang != 0 else 0
        eye_angle = heading + tilt

        # Scale smaller as feathers fan outward
        scale = 1.0 - (abs(ang) / 55) * 0.22

        # Draw the layered eye feather
        draw_eye(eye_x, eye_y, eye_angle, scale, delay_per_step)
    
    return delay_per_step

# -------------------- RUN --------------------
delay = draw_fan()

# Draw peacock body in front of the fan
draw_peacock_body(delay)

pen.penup()
pen.goto(0, -310)
pen.color("gold")
pen.write("Peacock Fan Animation using Python",
          align="center", font=("Arial", 14, "bold"))

screen.update()
turtle.done()

# with AI
