from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

for _ in range(4):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

for i in range(8):
    for j in range(i+3):
        timmy.forward(100)
        timmy.right(360/(i+3))








screen = Screen()
screen.exitonclick()
