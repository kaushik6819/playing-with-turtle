from turtle import Turtle,Screen

timmy = Turtle()
timmy.shape("turtle")

"""timmy.forward(100)
timmy.left(90)
timmy.home()"""


'''for steps in range(100):
    for c in ("blue","red","green"):
        timmy.color(c)
        timmy.forward(steps)
        timmy.right(30)
        #timmy.fillcolor(c)
        timmy.begin_fill()'''

while True:
    for c in "yellow","red","pink","blue":
        timmy.forward(200)
        timmy.left(170)
        timmy.color(c)
    

    if abs(timmy.pos()) < 1:
        break


my_screen = Screen()
my_screen.canvheight
my_screen.exitonclick()

