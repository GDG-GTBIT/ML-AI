from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
game_on =True

screen = Screen()
r_paddle =Paddle((370,0))
l_paddle =Paddle((-370,0))
ball =Ball()

r_score = Score((50,250))
l_score = Score((-50,250))
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("pong")
screen.tracer(0)  #Turning off animation



screen.onkey(r_paddle.move_up,'Up')
screen.onkey(r_paddle.move_down,'Down')


screen.onkey(l_paddle.move_up,'w')
screen.onkey(l_paddle.move_down,'s')

screen.listen()

while game_on:
    time.sleep(ball.move_speed) #add delay of 'X' seconds
    screen.update()
    ball.move()
    if ball.ycor() >280 or ball.ycor() <-280: #collision with walls
        ball.bounce()

    #collision with r_paddle
    if ball.distance(r_paddle) <50 and ball.xcor() > 350:
        ball.paddle_bounce()

    if ball.xcor() >380:
        ball.reset_position()
        l_score.increase_score()



    #collision with l_paddle
    if ball.distance(l_paddle)  <50 and ball.xcor() <-350:
        ball.paddle_bounce()

    if ball.xcor() <-380:
        ball.reset_position()
        r_score.increase_score()









screen.exitonclick()

