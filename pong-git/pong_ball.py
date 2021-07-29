from turtle import Turtle


class Pong(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 0)
        self.penup()
        self.shape('circle')
        self.color('red')
        self.setheading(0)
        self.speed(5)
        self.x_move = 10
        self.y_move = 10
        self.points = 0

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.bounce_x()




