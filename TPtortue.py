import turtle
import random
print("hello")
maTortue=turtle.Turtle()
maTortue.pencolor("red")
maTortue.speed(0)
Tortue1=turtle.Turtle()
Tortue1.pencolor("cyan")
Tortue2=turtle.Turtle()
Tortue2.pencolor("green")
Tortue3=turtle.Turtle()
Tortue3.pencolor("orange")
turtle.delay(5)



def gauche (tortue):
    tortue.left(90)
def droite (tortue):
    tortue.right(90)

def carré (tortue,distance):
    for i in range (0,4):
        tortue.forward(distance)
        gauche(tortue)

def cercle (tortue):
    for i in range (0,360):
        tortue.forward(1)
        tortue.left(1)

def escarc (tortue,tour):
    for i in range (0,tour*4):
        tortue.forward(10+i*5)
        gauche(tortue)


def escarr (tortue,tour):
    for i in range (0,360*tour):
        tortue.forward(0.1+i/750)
        tortue.left(1)

def maral (tortue):
    turtle.delay(0)
    test = random.randint(1,4)
    if test == 1:
        gauche(tortue)
        tortue.forward(6)
    elif test ==2:
        droite(tortue)
        tortue.forward(6)
    else:
        tortue.forward(12)


def changeUpPosition():
    maTortue.setheading(90)

def changeRightPosition():
    maTortue.setheading(0)

def changeLeftPosition():
    maTortue.setheading(180)

def changeDownPosition():
    maTortue.setheading(270)

def changeUpPosition1():
    Tortue1.setheading(90)

def changeRightPosition1():
    Tortue1.setheading(0)

def changeLeftPosition1():
    Tortue1.setheading(180)

def changeDownPosition1():
    Tortue1.setheading(270)

Tortue2.penup()
Tortue2.goto(300,300)
Tortue2.pendown()
Tortue3.penup()
Tortue3.goto(random.randint(-300,300),random.randint(-300,300))
Tortue3.pendown()

turtle.onkeypress(changeUpPosition,"Up")
turtle.onkeypress(changeLeftPosition,"Left")
turtle.onkeypress(changeRightPosition,"Right")
turtle.onkeypress(changeDownPosition,"Down")
turtle.onkeypress(changeUpPosition1,"z")
turtle.onkeypress(changeLeftPosition1,"q")
turtle.onkeypress(changeRightPosition1,"d")
turtle.onkeypress(changeDownPosition1,"s")

turtle.listen()

while 1:
    maTortue.forward(1)
    Tortue1.forward(1)

input()
