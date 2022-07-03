import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "brown"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CARS_DIRECTIONS = [0, 180]
CARS_SPEED = [0, 10]


class CarManager(Turtle):
    def __init__(self, the_x, the_y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=random.randint(1, 2), stretch_wid=0.9)
        self.penup()
        self.goto(the_x, the_y)
        self.setheading(random.choice(CARS_DIRECTIONS))
        self.speed(random.choice(CARS_SPEED))

    def car_move(self):
        self.forward(STARTING_MOVE_DISTANCE)
