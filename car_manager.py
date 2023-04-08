from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        i = random.randint(0, 5)
        if i == 0:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            random_ycor = random.randint(-250, 250)
            new_car.goto(300, random_ycor)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
