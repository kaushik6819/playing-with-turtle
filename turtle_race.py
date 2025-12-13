import turtle
from random import randint

red = turtle.Turtle()
green = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()
brown = turtle.Turtle()
orange = turtle.Turtle()

screen = turtle.Screen()
bet = screen.textinput("make your bet","who will win the race")

red.shape("turtle")
red.color("red")

green.shape("turtle")
green.color("green")

blue.shape("turtle")
blue.color("blue")

yellow.shape("turtle")
yellow.color("yellow")

brown.shape("turtle")
brown.color("brown")

orange.shape("turtle")
orange.color("orange")

red.penup()
red.setpos(-360,280)

green.penup()
green.setpos(-360,200)

blue.penup()
blue.setpos(-360,120)

yellow.penup()
yellow.setpos(-360,40)

brown.penup()
brown.setpos(-360,-40)

orange.penup()
orange.setpos(-360,-120)

winner = ""
turtles = [red, green, blue, yellow, brown,  orange]
flag = True
while flag:
    turtles[0].fd(randint(0,10))
    turtles[1].fd(randint(0,10))
    turtles[2].fd(randint(0,10))
    turtles[3].fd(randint(0,10))
    turtles[4].fd(randint(0,10))
    turtles[5].fd(randint(0,10))

    if turtles[0].xcor()>350:
        winner ="red"
        flag = False
    elif turtles[1].xcor()> 350:
        winner = "green"
        flag = False
    elif turtles[2].xcor()> 350:
        winner = "blue"
        flag = False
    elif turtles[3].xcor()> 350:
        winner = "yellow"
        flag = False
    elif turtles[4].xcor()> 350:
        winner = "brown"
        flag = False
    elif turtles[5].xcor()> 350:
        winner = "orange"
        flag = False
    



if bet == winner:
    print("you won the bet")
else:
    print(f"you lose the bet the winner is {winner}")









screen.canvheight
