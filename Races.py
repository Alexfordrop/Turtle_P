import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow',
 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Введите количество гонщиков (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Введено не число... Попробуй снова!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Число гонщиков может быть от 2 до 10. Попробуй снова!")

def create_turtles(colors):
    turtle = []
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        recer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # позиция черепашки
        racer.pendown()
        turtles.append(racer)

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Гонка черепашек!!!")

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
create_turtles(colors)

