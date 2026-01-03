from turtle import Turtle,Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Score

#setting up the screen
screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

#player turtle
player =Player()
cars= CarManager()
score =Score()
screen.listen()#listen the input from keyboard


screen.onkey(player.move,"Up") 

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()
    
    if player.ycor() > 280 :
        player.restart()
        score.point()
        cars.level_up()
    
    for car in cars.all_cars:
        if car.distance(player) <20:
            score.game_over()
            game_is_on = False


screen.exitonclick()