from turtle import Turtle
import random


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", align="center", font=("Courier", 14, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.update_score()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER! ", align="center", font=("Courier", 28, "normal"))