from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 20, "normal"))

    def update_scoreboard(self):
        print("updated")

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Ariel", 20, "normal"))
