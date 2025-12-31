from turtle import Turtle

FONT = ("Arial",13,"normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        
        self.hideturtle()
        self.penup()
        self.goto(0,280)
    
    def update(self):
        self.write(f"SCORE :{self.count}",True,font=FONT, align="center")
    
    def game_over(self):
        self.home()
        self.write(f"High Score is :70 \nTerse sai nahi hoga chorde",True,font=FONT, align="center")
    

    def count_score(self):
        self.clear()
        self.count+=1
        self.goto(0,280)
        self.update()
        
        


    