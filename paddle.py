from turtle import Turtle

class Paddle(Turtle):
    
    #Here in the __init__ function, we create the paddle style and shape. 
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=2)
        self.penup()
        self.goto(position)

    #Here we are creating the commands for the function move the paddle, up and down. 
    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)
