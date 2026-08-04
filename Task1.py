import turtle
import time
import random

# ==========================
# Screen Setup
# ==========================
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# ==========================
# Game Variables
# ==========================
delay = 0.1
score = 0
high_score = 0

# ==========================
# Snake Head
# ==========================
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("lime")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# ==========================
# Food
# ==========================
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Snake Body
segments = []

# ==========================
# Score Board
# ==========================
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


def update_score():
    pen.clear()
    pen.write(
        f"Score: {score}    High Score: {high_score}",
        align="center",
        font=("Courier", 24, "bold")
    )


update_score()

# ==========================
# Movement Functions
# ==========================
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    x = head.xcor()
    y = head.ycor()

    if head.direction == "up":
        head.sety(y + 20)

    elif head.direction == "down":
        head.sety(y - 20)

    elif head.direction == "left":
        head.setx(x - 20)

    elif head.direction == "right":
        head.setx(x + 20)


# ==========================
# Reset Game
# ==========================
def reset_game():
    global score, delay

    time.sleep(0.5)

    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()

    score = 0
    delay = 0.1

    update_score()


# ==========================
# Spawn Food Safely
# ==========================
def place_food():
    while True:
        x = random.randrange(-280, 281, 20)
        y = random.randrange(-280, 281, 20)

        good = True

        if head.distance(x, y) < 20:
            good = False

        for segment in segments:
            if segment.distance(x, y) < 20:
                good = False
                break

        if good:
            food.goto(x, y)
            break


# ==========================
# Keyboard Controls
# ==========================
wn.listen()

# WASD
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Arrow Keys
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# ==========================
# Main Game Loop
# ==========================
while True:

    wn.update()

    # Border Collision
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        reset_game()

    # Food Collision
    if head.distance(food) < 20:

        place_food()

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()

        segments.append(new_segment)

        score += 10

        if score > high_score:
            high_score = score

        delay = max(0.05, delay - 0.002)

        update_score()

    # Move Body
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        segments[0].goto(head.xcor(), head.ycor())

    # Move Head
    move()

    # Body Collision
    for segment in segments:
        if segment.distance(head) < 15:
            reset_game()
            break

    time.sleep(delay)