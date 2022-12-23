from turtle import *


# def random_color():
#     r = random.randint(50, 255)
#     g = random.randint(50, 255)
#     b = random.randint(50, 255)
#     random_color = (r, g, b)
#     return random_color

class Rectangle:
    def __init__(self, _length):
        self.rectangle = Turtle()
        self.rectangle.height = _length
        self.rectangle.shape("square")
        self.rectangle.penup()
        self.rectangle.color("white")
        # self.rectangle.color(255,255,255)
        self.rectangle.shapesize(round(_length/2), 0.3)
