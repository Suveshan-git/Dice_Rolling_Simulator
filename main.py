# DICE DOLLING SIMULATOR

import random

# Ask the user how many die they wish to roll
number_of_die = int(input("Enter the number of die you wish to roll: "))

# Display the values of all the die
total_dice_value = 0
dice = 0
while dice != number_of_die:
    dice_roll = random.randint(1, 6)
    print(f"Dice {dice+1}: {dice_roll}")
    total_dice_value = total_dice_value + dice_roll
    dice += 1

# Display the sum of all the die values
print("--------------")
print(f"Total value of rolled die: {total_dice_value}")
