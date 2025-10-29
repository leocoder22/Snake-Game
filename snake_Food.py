from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        rand_x = random.randint(-280,280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)
        self.dot(10, "blue")
        self.hideturtle()
