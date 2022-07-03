from turtle import Turtle
FONT = ("Courier", 16, "bold")
FONT2 = ("Courier", 30, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.current_level = 1
        self.current_lives = 5

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 260)
        self.write(f" LEVEL: {self.current_level}", align="center", font=FONT)
        self.goto(200, 260)
        self.write(f"LIVES: {self.current_lives}", align="center", font=FONT)

    def level_up(self):
        self.current_level += 1
        self.update_scoreboard()

    def live_down(self):
        self.current_lives -= 1
        self.update_scoreboard()

    def hit_a_car(self):
        self.goto(0, 0)
        self.write(f" YOU HAVE LOST A LIFE. ", align="center", font=FONT2)

    def comleted_level(self):
        self.goto(0, 0)
        self.write(f"LEVEL COMPLETED. ", align="center", font=FONT2)
