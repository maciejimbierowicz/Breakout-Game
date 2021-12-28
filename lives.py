from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.lives = 5
        self.update_lives()

    def update_lives(self):
        self.clear()
        self.goto(220,-200)
        self.write(f"LIVES: {self.lives}", align='left', font=FONT)

    def life_lost(self):
        self.lives -= 1
        self.update_lives()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)

    def game_win(self):
        self.goto(0, 0)
        self.write(f"YOU WON!!!", align='center', font=FONT)
