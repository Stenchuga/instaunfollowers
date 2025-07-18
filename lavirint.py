def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def check_up():
    while True:
        if wall_in_front() is True:
            turn_left()
            move()
            turn_right()
        else:
            break


while at_goal() is False:
    if wall_on_right() is True and front_is_clear() is True:
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif right_is_clear() is False and front_is_clear() is True:
        move()
    else:
        turn_left()
