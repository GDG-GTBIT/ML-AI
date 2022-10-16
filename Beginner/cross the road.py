import turtle
import random
import time
import sys
ppx = -400
ppy = 0
lives = 3
mapsc = 0


player = turtle.Turtle()
player.speed(0)
player.shape("triangle")
player.color("blue")
player.penup()
player.goto(-400,0)

car = turtle.Turtle()
car.speed(2)
car.color("red")
car.shape("square")
car.penup()
car.goto(-315,300)
car.direction = "stop"
car.hideturtle()
car2 = turtle.Turtle()
car2.speed(2)
car2.color("red")
car2.shape("square")
car2.penup()
car2.goto(-285,-300)
car2.direction = "stop"
car2.hideturtle()
car3 = turtle.Turtle()
car3.speed(2)
car3.color("red")
car3.shape("square")
car3.penup()
car3.goto(0,300)
car3.direction = "stop"
car3.hideturtle()
car4 = turtle.Turtle()
car4.speed(2)
car4.color("red")
car4.shape("square")
car4.penup()
car4.goto(385,300)
car4.direction = "stop"
car4.hideturtle()
car5 = turtle.Turtle()
car5.speed(2)
car5.color("red")
car5.shape("square")
car5.penup()
car5.goto(415,-300)
car5.direction = "stop"
car5.hideturtle()


border1 = turtle.Turtle()
border1.speed(0)
border1.penup()
border1.goto(-500,300)
border1.pendown()
border1.forward(1000)
border1.hideturtle()
border2 = turtle.Turtle()
border2.speed(0)
border2.penup()
border2.goto(-500,300)
border2.right(90)
border2.pendown()
border2.forward(600)
border2.hideturtle()
border3 = turtle.Turtle()
border3.speed(0)
border3.penup()
border3.goto(500,300)
border3.right(90)
border3.pendown()
border3.forward(1000)
border3.hideturtle()
border4 = turtle.Turtle()
border4.speed(0)
border4.penup()
border4.goto(-500,-300)
border4.pendown()
border4.forward(1000)
border4.hideturtle()

pen = turtle.Turtle()
pen.speed(0)
pen.right(90)
pen2 = turtle.Turtle()
pen2.speed(0)

def goup():
    global ppx, ppy
    ppy = ppy + 10
    player.goto(ppx,ppy)

def godown():
    global ppx, ppy
    ppy = ppy - 10
    player.goto(ppx,ppy)

def goleft():
    global ppx, ppy
    ppx = ppx - 10
    player.goto(ppx,ppy)
def goright():
    global ppx, ppy
    ppx = ppx + 10
    player.goto(ppx,ppy)


def map1():
    global car, car2, car3, car4, car5, player, border, ppx, ppy, lives, mapsc, pen, pen2
    screen = turtle.Screen()
    screen.title("Crossy Road by Matthew Xie")
    screen.bgcolor("lightgreen")
    screen.setup(width=600,height=600)
    screen.tracer(0)

    pen.color("black")
    pen.up()
    pen.goto(-300,300)
    pen.pensize(60)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(0,300)
    pen.down()
    pen.pensize(30)
    pen.forward(600)
    pen.up()
    pen.goto(400,300)
    pen.pensize(60)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-300,300)
    pen.pensize(1)
    pen.color("yellow")
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(400,300)
    pen.down()
    pen.forward(600)
    pen.hideturtle()
    pen2.color("black")
    pen2.hideturtle()
    pen2.up()
    pen2.goto(0,-350)
    pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))

    screen.listen()
    screen.onkeypress(goup, "w")
    screen.onkeypress(godown, "s")
    screen.onkeypress(goleft, "a")
    screen.onkeypress(goright, "d")
    def carmove():
        y = car.ycor()
        car.showturtle()
        car.sety(y-1.5)
        y2 = car2.ycor()
        car2.showturtle()
        car2.sety(y2+1.5)
        y3 = car3.ycor()
        car3.showturtle()
        car3.sety(y3-1.5)
        y4 = car4.ycor()
        car4.showturtle()
        car4.sety(y4-1.5)
        y5 = car5.ycor()
        car5.showturtle()
        car5.sety(y5+1.5)
        if car.ycor()<=-300:
            car.hideturtle()
            car.goto(-315,300)
        if car2.ycor()>=300:
            car2.hideturtle()
            car2.goto(-285,-300)
        if car3.ycor()<=-300:
            car3.hideturtle()
            car3.goto(0,300)
        if car4.ycor()<=-300:
            car4.hideturtle()
            car4.goto(385,300)
        if car5.ycor()>=300:
            car5.hideturtle()
            car5.goto(415,-300)

    while True:
        screen.update()
        carmove()
        if player.ycor()>=300:
            ppy = ppy - 10
            player.goto(ppx,ppy)
        if player.xcor()<=-500:
            ppx = ppx + 10
            player.goto(ppx,ppy)
        if player.ycor()<=-300:
            ppy = ppy + 10
            player.goto(ppx,ppy)
        if player.xcor()>=500:
            car.hideturtle()
            car2.hideturtle()
            car3.hideturtle()
            car4.hideturtle()
            car5.hideturtle()
            pen.clear()
            mapsc=mapsc+1
            break
        if player.distance(car) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car2) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car3) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car4) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car5) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if lives == 0:
            pen2.clear()
            pen2.write("You died! You completed {} maps".format(mapsc), align="center", font=("Courier", 80, "normal"))
            sys.exit()
def map2():
    global car, car2, car3, car4, car5, player, border, ppx, ppy, lives, mapsc, pen, pen2
    screen2 = turtle.Screen()
    screen2.title("Crossy Road(map2) by Matthew Xie")
    screen2.bgcolor("lightgreen")
    screen2.setup(width=600,height=600)
    screen2.tracer(0)
    pen.clear()
    player.goto(-400,0)
    ppx = -400
    ppy = 0
    pen.color("black")
    pen.up()
    pen.goto(-300,300)
    pen.pensize(30)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-200,300)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(0,300)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(200,300)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(300,300)
    pen.down()
    pen.forward(600)
    pen.hideturtle()
    car.goto(-300,300)
    car2.goto(-200,300)
    car3.goto(0,300)
    car4.goto(200,300)
    car5.goto(300,300)
    screen2.listen()
    screen2.onkeypress(goup, "w")
    screen2.onkeypress(godown, "s")
    screen2.onkeypress(goleft, "a")
    screen2.onkeypress(goright, "d")
    def carmove2():
        y12 = car.ycor()
        car.showturtle()
        car.sety(y12-2)
        y22 = car2.ycor()
        car2.showturtle()
        car2.sety(y22-2)
        y32 = car3.ycor()
        car3.showturtle()
        car3.sety(y32-2)
        y42 = car4.ycor()
        car4.showturtle()
        car4.sety(y42-2)
        y52 = car5.ycor()
        car5.showturtle()
        car5.sety(y52-2)
        if car.ycor()<=-300:
            car.hideturtle()
            car.goto(-300,300)
        if car2.ycor()<=-300:
            car2.hideturtle()
            car2.goto(-200,300)
        if car3.ycor()<=-300:
            car3.hideturtle()
            car3.goto(0,300)
        if car4.ycor()<=-300:
            car4.hideturtle()
            car4.goto(200,300)
        if car5.ycor()<=-300:
            car5.hideturtle()
            car5.goto(300,300)
    while True:
        screen2.update()
        carmove2()
        if player.ycor()>=300:
            ppy = ppy - 10
            player.goto(ppx,ppy)
        if player.xcor()<=-500:
            ppx = ppx + 10
            player.goto(ppx,ppy)
        if player.ycor()<=-300:
            ppy = ppy + 10
            player.goto(ppx,ppy)
        if player.xcor()>=500:
            car.hideturtle()
            car2.hideturtle()
            car3.hideturtle()
            car4.hideturtle()
            car5.hideturtle()
            pen.clear()
            mapsc = mapsc+1
            break
        if player.distance(car) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car2) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car3) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car4) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car5) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if lives == 0:
            pen2.clear()
            pen2.write("You died! You completed {} maps".format(mapsc), align="center", font=("Courier", 80, "normal"))
            sys.exit()
def map3():
    global car, car2, car3, car4, car5, player, border, ppx, ppy, lives, mapsc, pen, pen2
    screen3 = turtle.Screen()
    screen3.title("Crossy Road(map3) by Matthew Xie")
    screen3.bgcolor("lightgreen")
    screen3.setup(width=600,height=600)
    screen3.tracer(0)
    car6 = turtle.Turtle()
    car6.speed(4)
    car6.color("red")
    car6.shape("square")
    car6.penup()
    car6.goto(200,-300)
    car6.direction = "stop"
    car6.hideturtle()
    pen.clear()
    player.goto(-400,0)
    ppx = -400
    ppy = 0
    pen.color("black")
    pen.up()
    pen.goto(-300,300)
    pen.pensize(60)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-200,300)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(0,300)
    pen.pensize(30)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(200,300)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.color("yellow")
    pen.goto(-300,300)
    pen.pensize(1)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-200,300)
    pen.down()
    pen.forward(600)
    pen.hideturtle()
    car.goto(-315,-300)
    car2.goto(-285,300)
    car3.goto(-215, 300)
    car4.goto(-185, -300)
    car5.goto(0,300)
    screen3.listen()
    screen3.onkeypress(goup, "w")
    screen3.onkeypress(godown, "s")
    screen3.onkeypress(goleft, "a")
    screen3.onkeypress(goright, "d")
    def carmove3():
        y122 = car.ycor()
        car.showturtle()
        car.sety(y122+2.5)
        y222 = car2.ycor()
        car2.showturtle()
        car2.sety(y222-2.5)
        y322 = car3.ycor()
        car3.showturtle()
        car3.sety(y322-2.5)
        y422 = car4.ycor()
        car4.showturtle()
        car4.sety(y422+2.5)
        y522 = car5.ycor()
        car5.showturtle()
        car5.sety(y522-2.5)
        y622 = car6.ycor()
        car6.showturtle()
        car6.sety(y622+2.5)
        if car.ycor()>=300:
            car.hideturtle()
            car.goto(-315,-300)
        if car2.ycor()<=-300:
            car2.hideturtle()
            car2.goto(-285,300)
        if car3.ycor()<=-300:
            car3.hideturtle()
            car3.goto(-215,300)
        if car4.ycor()>=300:
            car4.hideturtle()
            car4.goto(-185,-300)
        if car5.ycor()<=-300:
            car5.hideturtle()
            car5.goto(0,300)
        if car6.ycor()>=300:
            car6.hideturtle()
            car6.goto(200,-300)
    while True:
        screen3.update()
        carmove3()
        if player.ycor()>=300:
            ppy = ppy - 10
            player.goto(ppx,ppy)
        if player.xcor()<=-500:
            ppx = ppx + 10
            player.goto(ppx,ppy)
        if player.ycor()<=-300:
            ppy = ppy + 10
            player.goto(ppx,ppy)
        if player.xcor()>=500:
            car.hideturtle()
            car2.hideturtle()
            car3.hideturtle()
            car4.hideturtle()
            car5.hideturtle()
            car6.hideturtle()
            pen.clear()
            mapsc = mapsc+1
            break
        if player.distance(car) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car2) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car3) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car4) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car5) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car6) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx=-400
            ppy=0
        if lives == 0:
            pen2.clear()
            pen2.write("You died! You completed {} maps".format(mapsc), align="center", font=("Courier", 80, "normal"))
            sys.exit()
def map4():
    global car, car2, car3, car4, car5, player, border, ppx, ppy, lives, mapsc, pen, pen2
    screen4 = turtle.Screen()
    screen4.title("Crossy Road(map4) by Matthew Xie")
    screen4.bgcolor("lightgreen")
    screen4.setup(width=600,height=600)
    screen4.tracer(0)
    car6 = turtle.Turtle()
    car6.speed(4)
    car6.color("red")
    car6.shape("square")
    car6.penup()
    car6.goto(215,-300)
    car6.direction = "stop"
    car6.hideturtle()
    pen.clear()
    player.goto(-400,0)
    ppx = -400
    ppy = 0
    pen.color("black")
    pen.up()
    pen.goto(-200,300)
    pen.pensize(120)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(200,300)
    pen.pensize(60)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-240,300)
    pen.pensize(1)
    pen.color("yellow")
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-200,300)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(-160,300)
    pen.down()
    pen.forward(600)
    pen.up()
    pen.goto(200,300)
    pen.down()
    pen.forward(600)
    pen.hideturtle()
    car.goto(-255,300)
    car2.goto(-215,-300)
    car3.goto(-175,-300)
    car4.goto(-135,300)
    car5.goto(185,300)
    screen4.listen()
    screen4.onkeypress(goup, "w")
    screen4.onkeypress(godown, "s")
    screen4.onkeypress(goleft, "a")
    screen4.onkeypress(goright, "d")
    def carmove4():
        y1222 = car.ycor()
        car.showturtle()
        car.sety(y1222-2)
        y2222 = car2.ycor()
        car2.showturtle()
        car2.sety(y2222+2.5)
        y3222 = car3.ycor()
        car3.showturtle()
        car3.sety(y3222+1.5)
        y4222 = car4.ycor()
        car4.showturtle()
        car4.sety(y4222-2)
        y5222 = car5.ycor()
        car5.showturtle()
        car5.sety(y5222-3)
        y6222 = car6.ycor()
        car6.showturtle()
        car6.sety(y6222+3)
        if car.ycor()<= -300:
            car.hideturtle()
            car.goto(-255,300)
        if car2.ycor()>=300:
            car2.hideturtle()
            car2.goto(-215,-300)
        if car3.ycor()>=300:
            car3.hideturtle()
            car3.goto(-175,-300)
        if car4.ycor()<=-300:
            car4.hideturtle()
            car4.goto(-135,300)
        if car5.ycor()<=-300:
            car5.hideturtle()
            car5.goto(185,300)
        if car6.ycor()>=300:
            car6.hideturtle()
            car6.goto(215,-300)
    while True:
        screen4.update()
        carmove4()
        if player.ycor()>=300:
            py = ppy - 10
            player.goto(ppx,ppy)
        if player.xcor()<=-500:
            ppx = ppx + 10
            player.goto(ppx,ppy)
        if player.ycor()<=-300:
            ppy = ppy + 10
            player.goto(ppx,ppy)
        if player.xcor()>=500:
            car.hideturtle()
            car2.hideturtle()
            car3.hideturtle()
            car4.hideturtle()
            car5.hideturtle()
            car6.hideturtle()
            pen.clear()
            mapsc = mapsc+1
            break
        if player.distance(car) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car2) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car3) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car4) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car5) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx = -400
            ppy = 0
            pen2.clear()
            pen2.write("Lives: {}".format(lives), align="center", font=("Courier", 24, "normal"))
        if player.distance(car6) < 15:
            lives=lives-1
            player.goto(-400,0)
            ppx=-400
            ppy=0
        if lives == 0:
            pen2.clear()
            pen2.write("You died! You completed {} maps".format(mapsc), align="center", font=("Courier", 80, "normal"))
            sys.exit()
while True:
  map1()
  map2()
  map3()
  map4()

screen.mainloop()
