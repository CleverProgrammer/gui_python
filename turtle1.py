import turtle


def draw_star(size, color):
    angle = 120
    turt = turtle.Turtle()
    turt.speed(100)
    turt.fillcolor(color)
    turt.screen.bgcolor('red')
    turt.begin_fill()

    for side in range(5):
        turt.forward(size)
        turt.right(angle)
        turt.forward(size)
        turt.right(72 - angle)
    turt.end_fill()
    turtle.done()

draw_star(6, "white")
