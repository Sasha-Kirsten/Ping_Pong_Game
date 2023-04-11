from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Using the Screen function to make screen for the Ping Pong Game and setting it up for the game, like the color of the background, size and the title of the screen
screenWindow = Screen()
screenWindow.bgcolor("black")
screenWindow.setup(width=800, height=600)
screenWindow.title("The Pong Pong Game")
screenWindow.tracer(0)

#Creating the paddles and position them on the screen, and creating the ball object and the scoreboard objects in the main file. 
r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

#Here we are making commands for the keys to control the paddles, so that they can go up and down. 
screenWindow.listen()
screenWindow.onkey(r_paddle.go_up, "Up")
screenWindow.onkey(r_paddle.go_down, "Down")
screenWindow.onkey(l_paddle.go_up, "w")
screenWindow.onkey(l_paddle.go_down, "s")

#Starting the while loop for the game to play until the user closes the screen. Furthermore, there are if statements to check where the ball is: like if it hit the wall or the other side of the oponent.
game_is_on = True
while game_is_on:
    screenWindow.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()