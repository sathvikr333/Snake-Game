from turtle import Turtle
class scorecard(Turtle):
    def __init__(self):
        super(). __init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.goto(0,270)
        self.color("white")
        self.update_score()


        self.message = Turtle()
        self.message.penup()
        self.message.hideturtle()
        self.message.color("white")
    
    def update_score(self):
        self.write(f"Score : {self.score}", align = "center",font = ("Arial",18,"normal"))
    
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER",align ="center",font = ("Arial",24,"bold"))
        self.show_restart_message()
    def show_restart_message(self):
        self.message.goto(0, -80)
        self.message.write(
            "Press R to Restart\n\nPress Q to Quit",
            align="center",
            font=("Arial", 16, "normal")
        )
    
    
    
    def reset_score(self):
        
        self.clear()
        self.message.clear()
        self.score = 0
        self.goto(0, 270)
        self.update_score()

    def new_score(self):

        self.score += 1
        self.clear()
        self.update_score()

