import turtle
from random import randint


screen = turtle.Screen()
turtle.setup(height=600, width=600)
screen.title("My snake game")
screen.bgcolor("black")


timmy = turtle.Turtle()
timmy.shape("square")
timmy.color("white")
timmy.speed(5)
timmy.penup()


tom = turtle.Turtle()
tom.shape("square")
tom.color("white")
tom.speed(5)
tom.penup()
tom.setposition(-20,0)


top = turtle.Turtle()
top.shape("square")
top.color("white")
top.speed(5)
top.penup()
top.setposition(-40,0)

screen.tracer(2, 5)

flag = True
while flag:
    timmy.fd(10)
    tom.fd(10)
    top.fd(10)



screen.exitonclick()