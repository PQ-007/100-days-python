import turtle as t
from random import randint
tim = t.Turtle()
screen = t.Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="2xbet", prompt="Betee tavi")
# def move_f():
#     tim.forward(10)
# def move_b():
#     tim.backward(10)
# def move_r():
#     tim.right(10)
# def move_l():
#     tim.left(10)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home() 
#     tim.pendown()

# screen.listen()

# screen.onkey(move_f, "w")
# screen.onkey(move_b, "s")
# screen.onkey(move_r, "d")
# screen.onkey(move_l, "a")
# screen.onkey(clear, "c")

def take_speed():
    return randint(3, 21)

turtles = [t.Turtle() for _ in range(5)]
colors = ['red', 'blue', 'green', 'yellow', 'pink']
def race_setup():
    #place turtles
    for i in range(5):
        turtles[i].shape("turtle")
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].goto(-240, 150-50*i)
        turtles[i].pendown()
    
    #draw finish line
    pen = t.Turtle()
    pen.penup()
    pen.goto(220, 190)
    pen.pendown()
    pen.goto(220, -190)

def check_finish(turtle: t.Turtle):
    if turtle.xcor() > 220:
        return True

finish = False
race_setup()

while not finish:
    for turtle in turtles:
        turtle.forward(take_speed())
        if check_finish(turtle):
            win_color = turtle.pencolor()
            finish = True
            if win_color == user_bet:
                print(f'{win_color} won, take your bet beeb')
            else:
                print(f'{win_color} won, loser never give up')
            break







screen.exitonclick()

