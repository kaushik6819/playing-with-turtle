from turtle import Turtle,Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800,height= 600)
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle()
paddle.right_paddle()

paddle_left = Paddle()
paddle_left.left_paddle()

"""paddle.shape("square")
paddle.color("white")
paddle.penup()
#paddle.left(90)
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.goto(350,0)
"""

screen.listen()

def f():
    new_y = paddle.ycor()+20
    paddle.goto(paddle.xcor(),new_y)
 
def b():
    new_y = paddle.ycor()-20
    paddle.goto(paddle.xcor(),new_y)

def forward():
    new_y = paddle_left.ycor()+20
    paddle_left.goto(paddle_left.xcor(),new_y)

def backward():
    new_y = paddle_left.ycor()-20
    paddle_left.goto(paddle_left.xcor(),new_y)


screen.onkey(f,"Up")
screen.onkey(b,"Down")
screen.onkey(forward,"w")
screen.onkey(backward,"s")

game_on = True

while game_on:
    screen.update()













screen.exitonclick()