import turtle
import time
import random


screen = turtle.Screen()
screen.title("Creative Square Art")
screen.setup(width=900, height=700)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2)         
pen.pensize(3)


colors = [
    "red", "blue", "green", "purple",
    "orange", "pink", "cyan", "gold"
]


def draw_square(size, color):
    pen.color("black", color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()


def change_background():
    bg_colors = ["lavender", "lightyellow", "lightblue", "honeydew"]
    screen.bgcolor(random.choice(bg_colors))


pen.penup()
pen.goto(0, 0)
pen.pendown()

size = 40

for i in range(10):
    change_background()
    
    square_color = random.choice(colors)
    draw_square(size, square_color)
    
    pen.right(20)    
    size += 25        
    
    time.sleep(0.5)   


pen.penup()
pen.goto(0, -300)
pen.color("black")
pen.write(
    "Turtle Graphics Square Design",
    align="center",
    font=("Comic Sans MS", 20, "bold")
)

pen.hideturtle()
turtle.done()
