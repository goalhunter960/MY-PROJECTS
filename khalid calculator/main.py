import os
import random
import turtle


def setup():
    global window, snake, food

    window = turtle.Screen()
    window.setup(width=600, height=400)
    window.bgcolor("black")
    window.title("Snake Game")

    snake = turtle.Turtle()
    snake.shape("square")
    snake.color("white")
    snake.speed(0)

    food = turtle.Turtle()
    food.shape("circle")
    food.color("red")
    food.speed(0)
    food.penup()
    food.setposition(random.randint(-290, 290), random.randint(-190, 190))


def move():
    global snake
    snake.forward(20)


def check_collision():
    global snake

    if snake.xcor() < -300 or snake.xcor() > 300:
        game_over()
    elif snake.ycor() < -200 or snake.ycor() > 200:
        game_over()

    for segment in snake.segments[1:]:
        if snake.position() == segment.position():
            game_over()


def game_over():
    print("Game over!")
    window.bye()


def main():
    global snake, food

    setup()

    while True:
        move()
        check_collision()
        window.update()


if __name__ == "__main__":
    main()
