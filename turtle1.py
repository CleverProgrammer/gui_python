import turtle


brad = turtle.Turtle()
brad.begin_fill()
brad.screen.bgcolor('red')
brad.color("white", "green")
brad.fillcolor('white')
brad.speed(100)
for i in range(5):
    brad.forward(30)
    brad.right(144)
brad.end_fill()
turtle.done()
