import turtle
import math
import time
import threading

# -----------------------------
# Screen setup
# -----------------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("❤️ Love Heart Animation")
screen.setup(width=800, height=700)

# -----------------------------
# Heart turtle
# -----------------------------
heart = turtle.Turtle()
heart.hideturtle()
heart.speed(0)
heart.penup()

# Text turtle
text = turtle.Turtle()
text.hideturtle()
text.color("pink")
text.penup()

# -----------------------------
# Draw a heart
# -----------------------------
def draw_heart(size):
    heart.clear()
    heart.goto(0, -size * 0.35)
    heart.setheading(0)

    heart.color("#ff1744")
    heart.fillcolor("#ff1744")

    heart.begin_fill()

    # Parametric heart shape
    points = []

    for i in range(361):
        t = math.radians(i)

        x = 16 * math.sin(t) ** 3
        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        points.append((x * size / 16, y * size / 16))

    heart.goto(points[0])

    heart.pendown()

    for x, y in points:
        heart.goto(x, y)

    heart.goto(points[0])
    heart.end_fill()
    heart.penup()


# -----------------------------
# Display text
# -----------------------------
def show_text():
    text.clear()

    text.goto(0, -280)
    text.write(
        "❤️ I LOVE YOU ❤️",
        align="center",
        font=("Arial", 28, "bold")
    )

    text.goto(0, -325)
    text.write(
        "You are special to me!",
        align="center",
        font=("Arial", 16, "normal")
    )


# -----------------------------
# Optional music
# -----------------------------
def play_music():
    try:
        import winsound

        # Put "love_music.wav" in the same folder as this program
        winsound.PlaySound(
            "love_music.wav",
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    except:
        print("Music file not found or music is not supported.")


# Start music in the background
music_thread = threading.Thread(target=play_music)
music_thread.daemon = True
music_thread.start()


# -----------------------------
# Heart beating animation
# -----------------------------
show_text()

sizes = [16, 17, 18, 19, 20, 21, 22, 21, 20, 19, 18, 17]

while True:

    for size in sizes:
        draw_heart(size)
        screen.update()
        time.sleep(0.04)

    for size in reversed(sizes):
        draw_heart(size)
        screen.update()
        time.sleep(0.04)
