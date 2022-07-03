from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        self.movement_info()

    def movement_info(self):
        #self.clear()
        self.goto(-280, 280)
        self.write("UP=W DOWN=S", align="center",font=("Courier", 15, "bold"))
        self.goto(280, 280)
        self.write("UP=↑ DOWN=↓", align="center", font=("Courier", 15, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center",font=("Courier", 40, "bold"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Courier", 40, "bold"))
        self.movement_info()

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()