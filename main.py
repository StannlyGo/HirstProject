from turtle import Turtle, Screen
import random
import colorgram

turtle = Turtle()
color_list = []
screen = Screen()
turtle.hideturtle()

my_colors = colorgram.extract('image.jpg', 30)

for color in my_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    color_list.append(rgb)

current_y = 0

for _ in range(10):
    for item in range(10):
        screen.colormode(255)
        color_selector = random.choice(color_list)
        turtle.dot(20, color_selector)
        turtle.penup()
        turtle.forward(40)
    current_y += 40
    turtle.goto(0, current_y)
