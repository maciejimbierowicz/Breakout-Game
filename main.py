from turtle import Screen
from paddle import Paddle
from block import Block
from ball import Ball
from lives import Lives
import time

#Creating game screen
screen = Screen()
screen.setup(width=800, height = 600)
screen.title('Breakout Game')
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

# Importing blocks, ball, paddle and scoreboard
paddle = Paddle()
ball = Ball()
block = Block()
block.block_creator()
live = Lives()

# Paddle move keys
screen.onkey(paddle.paddlemoveleft, "Left")
screen.onkey(paddle.paddlemoveright, "Right")

# Game engine
def game():
    count = 0
    game_on = True
    while game_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.ball_move()

        # Detecting colision with blocks
        for b in block.all_blocks:
            if ball.distance(b) < 55:
                ball.bounce_y()
                b.goto(-1000, -1000)
                count +=1
                if count == 30:
                    b.hideturtle()
                    live.game_win()
                    game_on = False
                    break

        # Detecting ball collision with paddle
        if ball.distance(paddle) > 40 and ball.ycor() == -290:
            live.life_lost()
            if live.lives == 0:
                live.game_over()
                game_on = False
                break
            ball.reset_game()
        elif ball.distance(paddle) < 40 and ball.ycor() > -290:
            ball.bounce_y()
        elif ball.ycor() == 290:
            ball.bounce_y()
        if ball.xcor() == -390 or ball.xcor() == 390:
            ball.bounce_x()
game()












screen.exitonclick()