from turtle import Turtle, Screen

# triangle, square 
timmy= Turtle()
timmy.shape("turtle")
timmy.speed(5)

timmy.color("red")
#triangle
for _ in range(3): 
    timmy.forward(100)
    timmy.left(240)


#square
timmy.color("blue")
for _ in range(4):
    timmy.forward(100)
    timmy.left(270)
    

#pentagon
timmy.color("green")
for _ in range(5):
    timmy.forward(100)
    timmy.left(288)

#hexagon

timmy.color("pink")
for _ in range(6):
    timmy.fd(100)
    timmy.left(300)

#heptagon
timmy.color("yellow")
for _ in range(7):
    timmy.fd(100)
    timmy.left(308.57)

#octagon
timmy.color("orange")
for _ in range(8):
    timmy.fd(100)
    timmy.left(315)

#nonagon
timmy.color("firebrick")
for _ in range(9):
    timmy.fd(100)
    timmy.left(320)

#decagon
timmy.color("gold1")
for _ in range(10):
    timmy.fd(100)
    timmy.left(324)


my_screen = Screen()
my_screen.canvheight
my_screen.exitonclick()