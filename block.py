from turtle import Turtle
import random

COLORS = ['green', 'blue', 'yellow', 'red']

# Creating blocks to destroy
class Block:

    def __init__(self):
        self.all_blocks = []

    def block_creator(self):
            y = 280
            for n in range(5):
                new_block = Turtle()
                new_block.hideturtle()
                new_block.shape('square')
                new_block.color(random.choice(COLORS))
                new_block.speed('fastest')
                new_block.penup()
                new_block.shapesize(stretch_wid=1.5, stretch_len=5.5)
                new_block.showturtle()
                new_block.goto(-330, y)
                d = -200
                self.all_blocks.append(new_block)
                for x in range(5):
                    new_block = Turtle()
                    new_block.hideturtle()
                    new_block.shape('square')
                    new_block.color(random.choice(COLORS))
                    new_block.speed('fastest')
                    new_block.penup()
                    new_block.shapesize(stretch_wid=1.5, stretch_len=5.5)
                    new_block.showturtle()
                    new_block.goto(d, y)
                    self.all_blocks.append(new_block)
                    d += 130
                y -= 50


