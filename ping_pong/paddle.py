from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
    
    def left_paddle(self):
        self.goto(-350,0)

    def right_paddle(self):
        self.goto(350,0)
        
