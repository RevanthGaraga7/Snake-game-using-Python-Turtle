from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard
import time
DISTANCE=20

#screen
screen=Screen()
screen.setup(width=800,height=500)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

#creating main objects
snake=Snake()
food = Food() 
score=Scoreboard()

screen.listen()
screen.onkey(snake.UP,"Up")
screen.onkey(snake.DOWN,"Down")
screen.onkey(snake.RIGHT,"Right")
screen.onkey(snake.LEFT,"Left")


game_is_on = True
while game_is_on :
    screen.update()
    time.sleep(0.2)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increasing_score()
        
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 230 or snake.head.ycor() < -230:
        game_is_on=False
        score.game_over()

    for i in snake.segments[1: ]:
       if snake.head.distance(i)<10:
            game_is_on=False
            score.game_over()

screen.exitonclick()

   



