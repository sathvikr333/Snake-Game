from turtle import Screen
import time
from snake import Snake
from food import Food
from score import scorecard
def restart_game():
    global game_is_on 
    game_is_on = True
    snake.reset()
    scoreboard.reset_score()
    food.refresh()
def quit_game():
    global running
    running = False
    


screen = Screen()
screen.setup(width = 600,height = 600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = scorecard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(restart_game,"r")
screen.onkey(quit_game, "q")

running = True
game_is_on = True
while running:
    screen.update()
    time.sleep(0.1)
    if game_is_on: 
        snake.move()
    

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.new_score()
        snake.extend_snake()

    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        
        game_is_on = False
        scoreboard.game_over()


    for segment in snake.turtles[1:]:
        
        if snake.head.distance(segment) < 10:
            
            game_is_on = False
            scoreboard.game_over()

screen.bye()



