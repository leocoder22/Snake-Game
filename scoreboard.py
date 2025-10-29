from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.score_update()
        with open("data.txt",mode="r") as data:
             self.high_score = int(data.read())

    def score_update(self):
        self.hideturtle()
        self.penup()
        self.goto(-90, 270)
        self.color("white", "white")
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(-90, 270)
        self.write(f"Score : {self.score}", False, align=ALIGNMENT, font=FONT)

    def display_high_score(self):
        self.hideturtle()
        self.goto(90, 270)
        self.write(f"High Score : {self.high_score}",align=ALIGNMENT,font=FONT)