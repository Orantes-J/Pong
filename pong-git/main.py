# all imports
import time
from turtle import Turtle, Screen
from score import ScreenMsg
from split_screen import Splits
from players import Paddle
from pong_ball import Pong
from game_over_msg import Message

# don't change
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# screen settings
screen = Screen()
screen.tracer(0)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title("Pong")
screen.listen()

# screen messages settings
screen_msg = Message()

# score settings
score = ScreenMsg()

# paddle settings
left_paddle = Paddle(-300, 0)
right_paddle = Paddle(300, 0)

# splits settings
split = Splits()

# pong ball settings
pong = Pong()

screen.onkey(right_paddle.down, 'Down')
screen.onkey(right_paddle.up, 'Up')

screen.onkey(left_paddle.down, 's')
screen.onkey(left_paddle.up, 'w')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    pong.move()

    # detect a collision with walls
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()
        print("Hit the top")

    # left paddle collision
    if pong.distance(left_paddle) < 40 and pong.xcor() > -300:
        print("made contact")
        pong.bounce_x()

    # right paddle collision
    if pong.distance(right_paddle) < 40 and pong.xcor() < 300:
        print("made contact")
        pong.bounce_x()

    if pong.xcor() > 380 or pong.xcor() < -380:
        pong.refresh()

    if pong.xcor() > 380:
        score.update_left_paddle()
    elif pong.xcor() < -380:
        score.update_right_paddle()


screen.exitonclick()
