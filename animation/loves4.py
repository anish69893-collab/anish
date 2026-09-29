import turtle
import time
import random

# Screen
screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("black")
screen.title("For Manvi ❤️")

# Turtle
t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Draw heart
def heart(size, color):
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()

    t.left(140)
    t.forward(size)

    t.circle(-size / 2, 200)

    t.left(120)

    t.circle(-size / 2, 200)

    t.forward(size)

    t.end_fill()

# Main animation
while True:

    # Clear screen
    t.clear()

    # Big heart
    t.penup()
    t.goto(0, -100)
    t.setheading(140)
    t.pendown()

    heart(180, "red")

    # Name
    t.penup()
    t.goto(0, 80)
    t.color("pink")
    t.write(
        "MANVI ❤️",
        align="center",
        font=("Arial", 35, "bold")
    )

    # Message
    t.goto(0, -230)
    t.color("white")
    t.write(
        "You are very special to me ❤️",
        align="center",
        font=("Arial", 22, "normal")
    )

    screen.update()
    time.sleep(0.3)

    # Heartbeat smaller
    t.clear()

    t.penup()
    t.goto(0, -90)
    t.setheading(140)
    t.pendown()

    heart(150, "deeppink")

    t.penup()
    t.goto(0, 80)
    t.color("pink")
    t.write(
        "MANVI ❤️",
        align="center",
        font=("Arial", 35, "bold")
    )

    t.goto(0, -230)
    t.color("white")
    t.write(
        "Forever in my heart 💖",
        align="center",
        font=("Arial", 22, "normal")
    )

    screen.update()
    time.sleep(0.3)