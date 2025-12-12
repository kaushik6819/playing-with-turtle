import turtle 

timmy = turtle.Turtle()
def forward():
    timmy.fd(10)

def backward():
    timmy.back(10)

def anti_clock_wise():
    timmy.left(10)

def clock_wise():
    timmy.right(10)

def clear_background():
    timmy.reset()
   




screen = turtle.Screen()
screen.onkey(forward, "w")
screen.onkey(backward,"s")
screen.onkey(anti_clock_wise,"a")
screen.onkey(clock_wise,"d")
screen.onkey(clear_background,"c")
screen.listen()
screen.canvheight
screen.exitonclick()