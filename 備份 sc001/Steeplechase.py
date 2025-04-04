"""
File: Steeplechase.py
Name: Rachel
---------------------------------
TODO:Rachel
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    pass
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()

def jump():
    """
    Pre-condition:Karel is on the left side of the wall,facing East
    post-condition:Karel is on the right side of the wall
    """
    up()
    cross()
    down()


def up():
    """
    Pre-condition:Karel is on the left side of the wall,facing East
    post-condition:Karel is at the upper left  of the wall
    """
    turn_left()
    while not right_is_clear():
        move()
    # alternative:
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()



def turn_right():
    turn_left()
    turn_left()
    turn_left()

def cross():
    """
    Pre-condition:Karel is on the upper left of the wall,facing North
    Post-condition:Karel is on the upper right of the wall
    """
    turn_right()
    move()
    turn_right()

def down():
    """
    Pre-condition:Karel is on the upper right of the wall,facing South
    Post-condition:Karel is on the right side of the wall,facing East
    """
    while front_is_clear():
        move()





# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
