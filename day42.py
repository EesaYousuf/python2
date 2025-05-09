# Circular Pattern (Radial Design)
import turtle

def draw_circle(t, radius):
    t.circle(radius)

def circular_pattern(repeats, radius):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    for i in range(repeats):
        t.goto(0, 0)
        t.setheading(i * 360 / repeats)
        t.forward(100)
        t.pendown()
        draw_circle(t, radius)
        t.penup()

    turtle.done()

# Example: 36 repetitions with circle radius 50
circular_pattern(36, 50)
