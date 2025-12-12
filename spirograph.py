import turtle
import random


timmy= turtle.Turtle()
timmy.speed(20)
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color

def number_circle(n,radius):
    for _ in range(n):
        timmy.color(random_color())
        timmy.circle(radius)
        timmy.left(5)



number_circle(200,100)
    







my_screen = turtle.Screen()
my_screen.canvheight
my_screen.exitonclick()