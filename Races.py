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
        racer.setpos()
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



##########################
racer = turtle.Turtle()
racer2 = turtle.Turtle()

racer.speed(1)
racer.penup()
racer.shape("turtle")
racer.color('cyan')
racer.forward(100)
racer.left(90)
racer.pendown()
racer.forward(100)
racer.right(90)
racer.backward(100)

racer2.speed(5)
racer2.penup()
racer2.shape("turtle")
racer2.color('red')
racer2.forward(150)
racer2.left(90)
racer2.pendown()
racer2.forward(100)
racer2.right(90)
racer2.backward(150)