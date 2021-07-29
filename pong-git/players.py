from turtle import Turtle


PADDLE_POSITION = (350, 0)


class Paddle(Turtle):
    paddles = []

    def __init__(self, x_position, y_position):
        super().__init__()
        paddle = []
        self.goto(x_position, y_position)
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        paddle.append(self)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



