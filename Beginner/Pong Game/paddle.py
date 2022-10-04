from turtle import Turtle,Screen

screen =Screen()

class Paddle(Turtle):
    def __init__(self,position_x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(4,1)
        self.goto(position_x)

    def move_up(self):
        new_y = self.ycor() + 20  # Getting new position of the paddle by adding 'X'(X=20) to its position
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    screen.listen()