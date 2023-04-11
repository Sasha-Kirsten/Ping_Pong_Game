from turtle import Turtle

class Scoreboard(Turtle):

    #Here in the __init__ function we are creating the scoreboard style, shape and the what it will contain. 
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    #Here the function will update the scoreboard integer values. The other two fucntions will individually update the integer values of the left and right side of the scorebaord.
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Calibri", 80, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Calibri", 80, "bold"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()