from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score_Board
import time

screen = Screen()
screen.setup(width=800,height= 600)
screen.bgcolor("black")
screen.tracer(0)


paddle = Paddle()
paddle.right_paddle()

paddle_left = Paddle()
paddle_left.left_paddle()

#Ball class
pong_ball = Ball()
points= Score_Board()




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
sleep_time =0.1
while game_on:
    screen.update()
    pong_ball.move()

    if pong_ball.ycor() > 280  or pong_ball.ycor() < -280:
        pong_ball.bounce_y()


    if (pong_ball.distance(paddle) < 50 and pong_ball.xcor() > 320) or (pong_ball.distance(paddle_left) < 50 and pong_ball.xcor() <-320):
        pong_ball.bounce_x()
        sleep_time -= 0.01



    if pong_ball.xcor() > 380:
        points.r_point()
        pong_ball.reset_ball()
        sleep_time = 0.1

    elif pong_ball.xcor() <-380:
        points.l_point()
        pong_ball.reset_ball()
        sleep_time = 0.1
       

    
    

    time.sleep(sleep_time)

    













screen.exitonclick()