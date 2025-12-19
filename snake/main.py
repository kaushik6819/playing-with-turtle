import turtle
import time
from snake import Snake
from food import Food
from score_board import Score

screen = turtle.Screen()
turtle.setup(height=600, width=600)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)

anish = Snake()
poison = Food()
score = Score()

screen.listen()
screen.onkey(anish.Up,"Up")
screen.onkey(anish.Down,"Down")
screen.onkey(anish.Left,"Left")
screen.onkey(anish.Right,"Right")


flag = True
while flag:
    screen.update()
    time.sleep(0.2)
    anish.move()

    #collision detection 
    if anish.head.distance(poison) < 15:

        poison.refresh()
        score.count_score()
    if (anish.head.xcor() > 300 or anish.head.xcor() < -300 or anish.head.ycor() > 300 or anish.head.ycor()< -300):
        score.game_over()
        flag = False
    


    
screen.exitonclick()