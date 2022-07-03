from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="This is a game where 6 turtles run with random sized move each time. \n Your job is to pick one that you think can win. \n Enter a color, you can choose between: \n [red] [green] [blue] [yellow] [pink] [brown] \n Psst! Type it correctly or the game won't start.")

y_value = 120
colors = ["red", "green", "blue", "yellow", "pink", "brown"]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-220, y=y_value)
    y_value -= 40
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True
while is_race_on:
    turtle: Turtle
    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won. The {winning_color} is the winner of this race. ")
            else:
                print(f"You have lost. The winning color is: {winning_color}. ")
        distance = random.randint(0, 10)
        turtle.forward(distance)

print(user_bet)
screen.exitonclick()