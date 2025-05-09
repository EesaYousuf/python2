# Hexagonal Tiling Pattern
import turtle
import math

def draw_hexagon(t, size):
    for _ in range(6):
        t.forward(size)
        t.right(60)

def hexagonal_tiling(rows, cols, size):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    height = size * math.sqrt(3)
    for row in range(rows):
        for col in range(cols):
            x = col * size * 1.5
            y = row * height
            if row % 2 == 1:
                x += size * 0.75  # offset every other row
            t.goto(x - cols * size * 0.75, y - rows * height / 2)
            t.pendown()
            draw_hexagon(t, size)
            t.penup()

    turtle.done()

# Example: 8x8 hex pattern with hexagon size 20
hexagonal_tiling(8, 8, 20)
