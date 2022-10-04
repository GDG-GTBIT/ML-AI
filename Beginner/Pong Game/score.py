from turtle import Turtle

class Score(Turtle):

    def __init__(self,position_x):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position_x)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):

        self.write(f" {self.score}", align='center', font=('Couries', 36, 'normal'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center', font=('Couries', 24, 'normal'))

