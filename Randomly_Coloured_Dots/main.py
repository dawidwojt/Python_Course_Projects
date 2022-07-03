#import colorgram
import turtle
import random
#rgb_colors = []
#colors = colorgram.extract('20_001.jpg', 26)
#print(colors)
#for color in colors:
#   #r = color.rgb.r
#   #g = color.rgb.g
#   #b = color.rgb.b
#   #new_color = (r, g, b)
#   #rgb_colors.append(new_color)
#print(rgb_colors)
color_list = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120)]
turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
number_of_dots = 100
timmy.hideturtle()
for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()



