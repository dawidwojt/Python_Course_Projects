import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("USA states game.")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_names = data["state"].to_list()
states_x = data["x"].to_list()
states_y = data["y"].to_list()
#print(states_names)

current_score = 0
states_number = 50
current_title= "Guess the State"
game_is_on = True
guessed_states = []

def add_name(x, y, z):
    guessed_name = turtle.Turtle()
    guessed_name.color("black")
    guessed_name.penup()
    guessed_name.hideturtle()
    guessed_name.goto(x, y)
    guessed_name.write(f"{answer_state}")


def you_won():
    name = turtle.Turtle()
    name.color("black")
    name.penup()
    name.hideturtle()
    name.write(f"!!! YOU WON !!!", align="center", font=("Courier", 30, "bold"))


while game_is_on:
    answer_state = (screen.textinput(title=current_title, prompt="What is another state's name? ")).title()
    if answer_state == "Exit":
        missing_states = [name for name in states_names if name not in guessed_states]
        # for state in states_names:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_missing.csv")
        print("THE STATES YOU MISSED ARE: ")
        print(missing_states)
        break
    for state in states_names:
        if answer_state == state:
            guessed_states.append(state)
            the_index = states_names.index(answer_state)
            x_value = states_x[the_index]
            y_value = states_y[the_index]
            add_name(x_value, y_value, answer_state)
            current_score += 1
            current_title = f"{current_score} / {states_number} States Correct"
        if current_score == 50:
            print("YOU WON! YOU GUESSED ALL THE STATES")
            you_won()
            game_is_on = False


print(answer_state)
#screen.exitonclick()
