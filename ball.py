from turtle import Turtle

class Ball(Turtle):

    #Here in the __init__ function we are creating the shape, color and speed the ball will be moving in the game.
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_movement = 3
        self.y_movement = 3
        self.move_speed = 0.01

    #Here, we are telling the ball how to move in the game, by give the ball the new coordinates to move.
    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)

    #Here we are making the function for when the ball is touching the walls and what the ball should be doing if that happens.
    def bounce_y(self):
        self.y_movement *= -1

    def bounce_x(self):
        self.x_movement *= -1
        self.move_speed *= 0.9
        
    #Here we are giving the new position for the ball to being, for instance, after score was made the ball needs to go to the original position.
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()