from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", 'r') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()


    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", 'w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()

        self.write(f"Score: {self.score}  Highscore : {self.high_score}", align=ALIGNMENT, font=FONT)
    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
