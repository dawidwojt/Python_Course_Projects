import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

sleeptime = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)
scoreboard = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.move, "Up")

LANES = int(520/20)
the_y = -250
all_cars = []


def cars_around():
    for _ in range(0, LANES):
        global the_y
        the_x = random.randint(-350, 350)
        new_car = CarManager(the_x, the_y)
        the_y += 20
        all_cars.append(new_car)


def trigger_game():
    global sleeptime
    cars_around()
    game_is_on = True
    while game_is_on:
        scoreboard.update_scoreboard()
        time.sleep(sleeptime)
        for car in all_cars:
            car.car_move()
            if car.xcor() > 310 or car.xcor() < -310:
                car.backward(620)
            if player.distance(car) < 20:
                scoreboard.live_down()
                player.goto(0, -280)
                scoreboard.hit_a_car()
                time.sleep(2)
                scoreboard.clear()
                return()
            if player.ycor() > 280:
                scoreboard.level_up()
                sleeptime *= 0.85
                player.goto(0, -280)
                scoreboard.comleted_level()
                time.sleep(2)
                scoreboard.clear()
                return()
        screen.update()
    screen.exitonclick()


def game_launcher():
    while scoreboard.current_lives > 0:
        trigger_game()
    print(f"The amount of levels you completed: {scoreboard.current_level - 1}")


game_launcher()


question = input("Would you like to play again? [Y/N").lower
if question == "y":
    game_launcher()
else:
    print("GOODBYE")
