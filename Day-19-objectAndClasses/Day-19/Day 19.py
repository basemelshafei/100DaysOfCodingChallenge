# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import random
from turtle import Turtle, Screen 
screen = Screen()
screen.setup(width=500, height=400)

colours = ["red", "orange", "yellow", "green", "blue"]

y_positions = [-100, -50, 0, 50, 100]

user_output = screen.textinput(title="make your bet", prompt= "which will win the race")

is_race_on = False

all_turtle = []

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x= -230, y= y_positions[i] )
    all_turtle.append(new_turtle)

if user_output:
    is_race_on = True
    
while is_race_on:
    
    
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_output:
                print("you win")
            else:
                print(f"you lost. winner is {winning_color}")
                
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
             


# def move_forward():
#    new_turtle.forward(10)

# def move_backward():
#     new_turtle.back(10)

# def turn_clockwise():
#     new_heading = basem.heading() + 10 
#     new_turtle.setheading(new_heading)
    
# def turn_anticlockwise():
#     new_heading = basem.heading() - 10 
#     new_turtle.setheading(new_heading)
    
#  def clear():
#      new_turtle.clear()
#      new_turtle.penup()
#      new_turtle.home()
#      new_turtle.pendown()
     
# screen.listen

# screen.onkey(fun = move_forward, key = "w")
# screen.onkey(fun = move_backward, key = "s")
# screen.onkey(fun = turn_clockwise , key = "a")
# screen.onkey(fun = turn_anticlockwise , key = "d")
# screen.onkey(fun = clear , key = "c")









































   









my_screen = screen.exitonclick()
