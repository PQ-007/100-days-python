import turtle as t
from random import choice
timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("red")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(4):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# for i in range(8):
#     for j in range(i+3):
#         timmy.forward(100)
#         timmy.right(360/(i+3))

t.colormode(255)

def random_color():
    r = choice(range(256))
    g = choice(range(256))
    b = choice(range(256))
    return (r, g, b)

# turn = [0, 90, 180, 270]
# timmy.pensize(10)
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(choice(turn))

timmy.speed("fastest")

for _ in range(100):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(5)





screen = t.Screen()
screen.exitonclick()
