#  Squares Grid Pattern
import turtle

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def squares_grid(rows, cols, size):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    for row in range(rows):
        for col in range(cols):
            x = col * size
            y = row * size
            t.goto(x - cols * size / 2, y - rows * size / 2)
            t.pendown()
            draw_square(t, size)
            t.penup()

    turtle.done()

# Example: 10x10 grid of squares with size 20
squares_grid(10, 10, 20)
