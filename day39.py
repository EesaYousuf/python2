"""Python code to generate a tessellated pattern of triangles
CopyReplit"""
import turtle

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.left(120)

def draw_pattern(rows, cols, size):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    for row in range(rows):
        for col in range(cols):
            # Calculate position
            x = col * size * 1.5
            y = row * size * (3**0.5) / 2
            if row % 2 == 1:
                x += size * 0.75  # offset every other row for tessellation
            t.goto(x - 300, y - 200)  # adjust for screen center
            t.pendown()
            draw_triangle(t, size)
            t.penup()

    turtle.done()

# Parameters: number of rows, columns, size of triangles
draw_pattern(10, 10, 30)