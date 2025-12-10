import random
from turtle import Turtle, Screen


timmy = Turtle()

timmy.speed(10)
timmy.pensize(10)
colours=["gold","green","indianRed","lawngreen","lemonchiffon","Lightblue"]
direction = [0,90,180,270]


def random_walk(n):

    for _ in range(n):
        
        
        timmy.color(random.choice(colours))
        timmy.setheading(random.choice(direction))
        timmy.fd(20)

       

random_walk(500)


my_screen = Screen()
my_screen.canvheight
my_screen.exitonclick()