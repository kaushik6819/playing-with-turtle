import turtle
import time
from snake import Snake

screen = turtle.Screen()
turtle.setup(height=600, width=600)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)

anish = Snake()
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


    
screen.exitonclick()