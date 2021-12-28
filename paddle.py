from turtle import Turtle

# Creating player's paddle
class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.shapesize(stretch_len=5, stretch_wid=0.5)
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.goto(0, -270)
        self.showturtle()

# Define paddle's movement
    def paddlemoveleft(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def paddlemoveright(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
