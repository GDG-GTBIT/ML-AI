import turtle
from turtle import Turtle,Screen
import random
riv = Turtle()


screen = Screen()
screen.bgcolor("black") #Setting background color as black

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color=(r, g, b)
    return random_color



riv.speed("fastest")#changing the speen of turtle
def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        riv.color(random_color())
        riv.circle(200)
        riv.left(gap)
draw_spirograph(10)
screen.exitonclick()

######## Challenge 1 - Draw a Square ############