from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:

    def __init__(self):
        self.snake_body = []
        self.snake_born()
        self.head = self.snake_body[0]

    def snake_born(self):
        for position in START_POSITION:
            self.add_part(position)

    def add_part(self,position):
        part = Turtle("square")
        part.color("white")
        part.penup()
        part.goto(position)
        self.snake_body.append(part)

    def extend(self):
        self.add_part(self.snake_body[-1].position())


    def move(self):
        for part_num in range(len(self.snake_body) -1, 0, -1):
            xcor = self.snake_body[part_num -1].xcor()
            ycor = self.snake_body[part_num -1].ycor()
            self.snake_body[part_num].goto(xcor,ycor)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)