'''
Modify the starter code below to create your own cool drawing
and then Pull Request it to your instructor. Make sure you
keep the last two lines of code. Your first and last name must be written on your art.
The last line keeps the window open until you click to close.

Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle

'''
import turtle
ham=turtle.Turtle()
screen=turtle.Screen() # makes a screen object
screen.bgcolor('black') # colors the screen
ham.pensize(3) # width of pen line
ham.speed(0)  # speed of drawing. Go fast to not waste time.
ham.color("#00FF00")
#ham.circle(50)  #head
ham.penup()
ham.goto(-40,-60)
ham.pendown()
#ham.circle(50)
ham.penup()
#ham.pendown()
#ham.goto(40,-80)
#ham.penup()
#ham.pendown()
#ham.goto(-200,210)
ham.goto(-88,145)
ham.penup()
#ham.setpos(200,-300)
for i in range(36):
    ham.pendown()
    ham.forward(50)
    ham.right(90)
    ham.circle(50)
    ham.forward(60)
    ham.right(100)
ham.penup()
ham.goto(-100,-60)
for i in range(3):
    ham.pendown()
    ham.forward(30)
    ham.right(90)
    ham.forward(30)
    ham.right(90)
    for i in range(8):
        ham.begin_fill()
        ham.circle(25)
        ham.forward(20)

ham.penup()
ham.goto(-190,-85)
ham.pendown()
ham.pencolor('blue')


ham.write('Bawi Thawng',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
