import turtle
import random
import time

# Screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Rose ❤️ Love Animation")

# Rose turtle
rose = turtle.Turtle()
rose.speed(0)
rose.color("red")
rose.fillcolor("red")
rose.pensize(2)

# Draw rose
rose.penup()
rose.goto(0, -120)
rose.pendown()
rose.setheading(140)

rose.begin_fill()
for i in range(2):
    rose.circle(100, 60)
    rose.circle(-100, 60)
rose.end_fill()

# Rose petals
for angle in range(0, 360, 45):
    rose.penup()
    rose.goto(0, -20)
    rose.setheading(angle)
    rose.pendown()
    rose.circle(80, 60)
    rose.circle(-80, 60)

# Stem
rose.penup()
rose.goto(0, -120)
rose.setheading(-90)
rose.pendown()
rose.color("green")
rose.pensize(8)
rose.forward(220)

# Leaves
rose.pensize(3)
rose.fillcolor("green")

rose.begin_fill()
rose.circle(60, 60)
rose.left(120)
rose.circle(60, 60)
rose.end_fill()

# Hide rose turtle
rose.hideturtle()

# Message
text = turtle.Turtle()
text.hideturtle()
text.color("pink")
text.penup()
text.goto(0, 220)
text.write("I Love You ❤️", align="center",
           font=("Arial", 28, "bold"))

# Floating hearts
hearts = []

for i in range(15):
    heart = turtle.Turtle()
    heart.hideturtle()
    heart.penup()
    heart.color("pink")
    heart.goto(random.randint(-350, 350),
               random.randint(-250, 250))
    heart.showturtle()
    hearts.append(heart)

# Animation
while True:
    for heart in hearts:
        x = heart.xcor()
        y = heart.ycor()

        heart.goto(x, y + 3)

        if y > 300:
            heart.goto(random.randint(-350, 350), -280)

        # Heart symbol
        heart.clear()
        heart.write("♥", align="center",
                    font=("Arial", random.randint(15, 25), "normal"))

    screen.update()
    time.sleep(0.03)