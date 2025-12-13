import turtle


screen = turtle.Screen()
screen.bgcolor("black")


star = turtle.Turtle()
star.color("purple")
star.pensize(3)
star.speed(9)


for i in range(5):
    star.forward(150)
    star.right(144)


turtle.done()
