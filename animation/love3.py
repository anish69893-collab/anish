import turtle
import time

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

def heart(size):
    t.clear()
    t.begin_fill()
    t.left(140)
    t.forward(size)
    t.circle(-size / 2, 200)
    t.left(120)
    t.circle(-size / 2, 200)
    t.forward(size)
    t.end_fill()

while True:
    for size in range(80, 120, 4):
        heart(size)
        time.sleep(0.03)

    for size in range(120, 80, -4):
        heart(size)
        time.sleep(0.03)