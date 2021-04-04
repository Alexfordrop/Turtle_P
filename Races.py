import turtle
import time

WIDTH, HEIGHT = 500, 500

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

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Гонка черепашек!!!")

racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.forward(100)
racer.left(90)
racer.forward(100)
racer.right(90)
racer.backward(100)
time.sleep(20)