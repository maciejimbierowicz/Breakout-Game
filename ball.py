from turtle import Turtle
import time

# Create ball from turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.goto(0, 0)
        self.speed(0.1)
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.03

# Ball movement
    def ball_move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() - self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= - 1

    def bounce_x(self):
        self.xmove *= -1

    def reset_game(self):
        self.hideturtle()
        self.goto(0, 0)
        self.showturtle()
        time.sleep(1)
        self.move_speed = 0.03
        self.ball_move()
