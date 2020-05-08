import numpy as np
import matplotlib.pyplot as plt
import math
import random


def switch_door(player_switch):
    player_choice = random.randint(1,3)
    host_open = random.randint(2,3)

    if player_switch: # same as if player_switch == True:
        # to make sure that the host_open doesn't overlap with player_choice
        # the number will be random because is it dependent on the value of player_choice
        # which is random
        while host_open == player_choice:
            host_open = random.randint(2,3)

        # unopened door will be one of 1,2,3 but not be player_choice and host_open
        unopened_door = [i for i in range(1,4)
                        if i not in (player_choice, host_open)]
        player_choice = unopened_door[0]
    # check if player's choice is correct
    if player_choice == 1:
        return True
    else:
        return False

trials = 1000000
def repeat(player_switch, trials):
    win_count = 0
    for i in range(trials):
        # if switch_door function above returns True,
        if switch_door(player_switch): 
            win_count += 1
    return win_count

wins_no_switch = repeat(False,trials)
wins_yes_switch = repeat(True,trials)

print("Number of Winning if No Switch:", wins_no_switch)
print("Number of Winning if Yes Switch:", wins_yes_switch)

print("Probability of Winning if No Switch:", wins_no_switch/trials)
print("Probability of Winning if Yes Switch:", wins_yes_switch/trials)
