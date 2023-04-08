import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("AntiqueWhite")
screen.setup(width=600, height=600)
screen.tracer(0)

score_board = Scoreboard()
player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    if player.ycor() > 290:
        player.go_to_start()
        car_manager.speed_up()
        score_board.increase_score()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            score_board.game_over()
            game_is_on = False


screen.exitonclick()
