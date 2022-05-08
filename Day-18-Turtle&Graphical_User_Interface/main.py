from turtle import Turtle, Screen
from random import choice, randint
basem_the_turtle = Turtle()

# basem_the_turtle.shape("circle")
# basem_the_turtle.color("DarkViolet")
# basem_the_turtle.forward(100)
# basem_the_turtle.right(90)
# basem_the_turtle.forward(100)
# basem_the_turtle.right(90)
# basem_the_turtle.forward(100)
# basem_the_turtle.right(90)
# basem_the_turtle.forward(100)

# for i in range(10):
#     basem_the_turtle.forward(10)
#     basem_the_turtle.up()
#     basem_the_turtle.forward(10)
#     basem_the_turtle.down()

colours = ["red","black","blue","yellow","green","orange","purple"]
direction = [0, 90, 180, 270]
basem_the_turtle.pensize(15)
basem_the_turtle.speed(0)

# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for i in range(num_of_sides):
#             basem_the_turtle.forward(50)
#             basem_the_turtle.right(angle)
#
# for num_of_sides in range(3, 11):
#     basem_the_turtle.pencolor(choice(colours))
#     draw_shape(num_of_sides)

def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colour = (r, g, b)
    return colour

# for _ in range(200):
#     basem_the_turtle.color(random_colour())
#     basem_the_turtle.forward(20)
#     basem_the_turtle.setheading(choice(direction))

for i in range(100):
    basem_the_turtle.circle(100)
    current_heading = basem_the_turtle.heading()
    basem_the_turtle.setheading(current_heading + 10)












# import heroes
#
# hero = heroes.WORDLIST
# hero_name = heroes.gen()
# print(hero)
# print(hero_name)



















screen = Screen()
screen.exitonclick()
