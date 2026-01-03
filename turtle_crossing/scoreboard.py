from turtle import Turtle
FONT = ("Arial",13,"normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        self.score =0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score :{self.score}",align="center",font=FONT)

    def point(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)