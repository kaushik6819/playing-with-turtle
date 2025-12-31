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

snake = Snake()
poison = Food()
score = Score()

screen.listen()
screen.onkey(snake.Up,"Up")
screen.onkey(snake.Down,"Down")
screen.onkey(snake.Left,"Left")
screen.onkey(snake.Right,"Right")


flag = True
while flag:
    screen.update()
    
    time.sleep(0.2)
    snake.move()

    #collision detection 
    if snake.head.distance(poison) < 15:

        poison.refresh()
        snake.extend()
        score.count_score()
    if (snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor()< -300):
        score.game_over()
        flag = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            flag = False
            score.game_over()
    


    
screen.exitonclick()