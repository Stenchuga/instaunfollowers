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


def check_down():
    move()
    turn_right()
    while True:
        if wall_in_front() is False:
            move()
        else:
            break


while at_goal() is False:
    if wall_in_front() is False:
        move()
    else:
        check_up()
        check_down()
        turn_left()