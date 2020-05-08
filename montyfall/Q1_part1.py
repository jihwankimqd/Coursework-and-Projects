import numpy as np
import matplotlib.pyplot as plt
import math
import random

player_switch = input("Switch No.1 to No.2, True or False: ")

def switch_door(player_switch):
    player_choice = random.randint(1,3)
    if player_switch: # same as if player_switch == True:
        # to make sure that the host_open doesn't overlap with player_choice
        # the number will be random because is it dependent on the value of player_choice
        # which is random
        host_open = random.randint(2,3)
        while host_open == player_choice:
            host_open = random.randint(2,3)

        # unopened door will be one of 1,2,3 but not be player_choice and host_open
        unopened_door = [i for i in range(1,4)
                            if i not in (player_choice, host_open)]
        player_choice = random.choice(unopened_door)
    # check if player's choice is correct
    if player_choice == 1:
        print("You Win")
        return
    else:
        print("You Lose")
        return

switch_door(player_switch)