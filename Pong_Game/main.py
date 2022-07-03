from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
sleeptime = 0.1

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("THE PONG GAME")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(sleeptime)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325 :
        ball.bounce_x()
        if sleeptime > 0.02:
            sleeptime *= 0.9
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        sleeptime = 0.1
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
        sleeptime = 0.1

screen.exitonclick()
