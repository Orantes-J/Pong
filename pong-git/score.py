from turtle import Turtle

user_one_score = 0
user_two_score = 0
ALIGNMENT = "center"
FONT = ('Courier', 25, 'normal')
POSITION = (0, 250)


class ScreenMsg(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.left_score = 0
        self.right_score = 0

    def update_scoreboard(self):
        self.write(f"{self.left_score}  {self.right_score}", align=ALIGNMENT, font=FONT)

    def update_left_paddle(self):
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def update_right_paddle(self):
        self.right_score += 1
        self.clear()
        self.update_scoreboard()

