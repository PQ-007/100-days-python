def turn_left():
    print("Turned left")
def move():
    print("Moved forward")
def wall_in_front():
    return False
def wall_on_right():
    return False
def at_goal():
    return False
def front_is_clear():
    return not wall_in_front()

def  turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif wall_in_front() and not wall_on_right():
        turn_right()    
