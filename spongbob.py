import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
sponge = turtle.Turtle()
sponge.speed(10)
sponge.pensize(3)

# Draw the main body (a rectangle)
def draw_body1():
    sponge.penup()
    sponge.goto(-100, -100)
    sponge.pendown()
    sponge.color("yellow")
    sponge.begin_fill()
    for _ in range(2):
        sponge.forward(200)
        sponge.left(90)
        sponge.forward(200)
        sponge.left(90)
    sponge.end_fill()

# Draw eyes
def draw_eye(x, y):
    sponge.penup()
    sponge.goto(x, y)
    sponge.pendown()
    sponge.color("white")
    sponge.begin_fill()
    sponge.circle(20)
    sponge.end_fill()
    # Pupil
    sponge.penup()
    sponge.goto(x, y + 20)
    sponge.pendown()
    sponge.color("black")
    sponge.begin_fill()
    sponge.circle(8)
    sponge.end_fill()

# Draw mouth
def draw_mouth():
    sponge.penup()
    sponge.goto(-50, -50)
    sponge.setheading(-60)
    sponge.pendown()
    sponge.color("black")
    sponge.width(4)
    sponge.circle(50, 120)

# Draw teeth
def draw_teeth1():
    sponge.penup()
    sponge.goto(0, -70)
    sponge.setheading(0)
    sponge.pendown()
    sponge.color("white")
    sponge.begin_fill()
    for _ in range(2):
        sponge.forward(10)
        sponge.left(90)
        sponge.forward(20)
        sponge.left(90)
    sponge.end_fill()

def draw_teeth2():
    sponge.penup()
    sponge.goto(-15, -70)
    sponge.setheading(0)
    sponge.pendown()
    sponge.color("white")
    sponge.begin_fill()
    for _ in range(2):
        sponge.forward(10)
        sponge.left(90)
        sponge.forward(20)
        sponge.left(90)
    sponge.end_fill()


# Draw body2
def draw_body2():
    sponge.penup()
    sponge.goto(-80, -120)
    sponge.pendown()
    sponge.color("black")
    sponge.begin_fill()
    for _ in range(2):
        sponge.forward(160)
        sponge.left(90)
        sponge.forward(20)
        sponge.left(90)
    sponge.end_fill()

# Draw legs as lines
def draw_legs():
    # Left leg
    sponge.penup()
    sponge.goto(-50, -120)
    sponge.pendown()
    sponge.setheading(-90)
    sponge.color("brown")
    sponge.width(20)
    sponge.forward(50)
    # Right leg
    sponge.penup()
    sponge.goto(50, -120)
    sponge.pendown()
    sponge.setheading(-90)
    sponge.forward(50)

#Draw arms
def draw_arm1():
    sponge.penup()
    sponge.goto(-100, 0)
    sponge.setheading(180)
    sponge.pendown()
    sponge.color("yellow")
    sponge.width(10)
    sponge.circle(-40, 120)

def draw_arm2():
    sponge.penup()
    sponge.goto(100, 0)
    sponge.setheading(0)
    sponge.pendown()
    sponge.color("yellow")
    sponge.width(10)
    sponge.circle(40, 120)

# Draw the body
draw_body1()
draw_body2()

# Draw eyes
draw_eye(-50, 30)
draw_eye(50, 30)

# Draw mouth
draw_mouth()
draw_teeth1()
draw_teeth2()

# Draw legs
draw_legs()
draw_arm1()
draw_arm2()

# Finish drawing
sponge.hideturtle()

# Keep window open
turtle.done()

