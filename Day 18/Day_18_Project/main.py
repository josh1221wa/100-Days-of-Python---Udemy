#  Recreate a Hirst dot painting using python

# import colorgram

# extracted_colors = colorgram.extract("hirst_demo.webp", 84)
# colors = []
# for i in extracted_colors:
#     rgb_obj = i.rgb
#     colors.append((rgb_obj.r, rgb_obj.g, rgb_obj.b))

# print(colors)

# We have wxtracted the color values and now we save them in the color_list.

import turtle as t
import random


def draw_dots(turtle, repeat):
    for i in range(repeat):
        for i in range(10):
            color = random.choice(color_list)
            turtle.dot(20, color)
            turtle.up()
            turtle.forward(50)
            turtle.down()
        turtle.up()
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.backward(500)
        turtle.down()


color_list = [(202, 166, 109), (152, 73, 47), (170, 153, 41), (222, 202, 138), (53, 93, 124), (135, 32, 22), (132, 163, 184), (48, 118, 88), (198, 91, 71), (16, 97, 75), (100, 73, 75), (67, 47, 41), (147, 178, 147), (163, 142, 156), (234, 177, 165),
              (55, 46, 50), (130, 28, 31), (184, 205, 174), (41, 60, 72), (83, 147, 126), (181, 87, 90), (31, 77, 84), (47, 65, 83), (215, 177, 182), (19, 71, 63), (175, 192, 212), (109, 123, 149), (173, 198, 205), (105, 136, 143), (72, 64, 55)]

t.TurtleScreen._RUNNING = True

turtle_obj = t.Turtle()
t.colormode(255)
turtle_obj.speed(10)

# To centre the image
turtle_obj.up()
turtle_obj.backward(250)
turtle_obj.right(90)
turtle_obj.forward(250)
turtle_obj.left(90)
turtle_obj.down()

draw_dots(turtle_obj, 10)

screen = t.Screen()
screen.exitonclick()
