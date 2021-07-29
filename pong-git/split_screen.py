from turtle import Turtle

splits_in_screen = 20


class Splits(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        y_cord = 250
        for i in range(splits_in_screen):
            self.hideturtle()
            self.goto(x=0, y=y_cord)
            self.setheading(270)
            self.color('white')
            self.pendown()
            self.forward(20)
            y_cord -= 50
            self.penup()

