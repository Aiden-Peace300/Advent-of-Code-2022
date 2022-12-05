# Programmer: Aiden Peace
# Date: Dec, 4th 2022
# Program : Day 1: Calorie Counting
# -------------------------------------------------------------------------------------------------------
# Prompt:
# Santa's reindeer typically eat regular reindeer food, but they need
# a lot of magical energy to deliver presents on Christmas. For that,
# their favorite snack is a special type of star fruit that only grows
# deep in the jungle. The Elves have brought you on their annual expedition
# to the grove where the fruit grows.
#
# The Elves take turns writing down the number of Calories contained by the
# various meals, snacks, rations, etc. that they've brought with them, one
# item per line. Each Elf separates their own inventory from the previous
# Elf's inventory (if any) by a blank line.
# For example, suppose the Elves finish writing their items'
# Calories and end up with the following list:
# 1000
# 2000
# 3000
#
# 4000
#
# 5000
# 6000
#
# 7000
# 8000
# 9000
#
# 10000
#
# This list represents the Calories of the food carried by five Elves:
#
#   - The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
#   - The second Elf is carrying one food item with 4000 Calories.
#   - The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
#   - The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
#   - The fifth Elf is carrying one food item with 10000 Calories.
#
# In case the Elves get hungry and need extra snacks, they need to know which Elf to.
# ask: they'd like to know how many Calories are being carried by the Elf carrying
# the most Calories. In the example above, this is 24000 (carried by the fourth Elf).
#
# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
# -------------------------------------------------------------------------------------------------------
#
# Aiden's Algo:
# - read from file
# - count up calories of each elf til you reach empty line
# - calc EACH elf's calories
# - compare current elf's calories to last elf's calories
# - save the elfs with the most calories.
# - print the elf with the most calories to console/terminal.
#
# -------------------------------------------------------------------------------------------------------

max_elf_calories = 0
each_elf_sum_of_calories = 0
save = 0
one_elfs_sum_of_cals = []

# read from file
# opening input file and saving each line in a list called 'list_of_cals'
with open("input.txt") as file:
    list_of_cals = file.readlines()
    list_of_cals = [line.rstrip() for line in list_of_cals]

print(list_of_cals)

# count up calories of each elf til you reach empty line
for line in list_of_cals:
    if line == '':
        # compare current elf's calories to last elf's calories
        if max_elf_calories <= each_elf_sum_of_calories:
            max_elf_calories = each_elf_sum_of_calories
            each_elf_sum_of_calories = 0
        else:
            each_elf_sum_of_calories = 0
    else:
        # calc EACH elf's calories
        each_elf_sum_of_calories += int(line)

# checking to see if last elf's calories was larger than the last
# we have to do this because the last elf won't have a '' behind it
# in the list of 'list_of_cals' so we have to check to see if the
# elf's calories sum is larger than the last elf's calories sum
if max_elf_calories <= each_elf_sum_of_calories:
    max_elf_calories = each_elf_sum_of_calories

# print the elf with the most calories to console/terminal.
print(max_elf_calories)

'''
# ----------- MERRY CHRISTMAS DAY 1 FROM AIDEN PEACE ---------
#　　　　　·　　❅·　　❆　❅❆　　❅　　*　　　　　　　　❆　❆　　*❆　　　.
#　　*　　　❅　·　.·　*　　*.　　　　•❅　　　•.　　　.　　•　.　　.　　•　
#　*　.·.　　　　　　.　　　·　❅*　　　　❅　　　　　　❆　❆　　*❆　.　　.
#　　•　　　　❆　❅　*　.　·　　　❆　❆　　*❆　　　.　　　　　　　　❅　.　
#　　　　•　　　　　　·　*　　　　❆　*❅❆　　　　*　.　　　❅　　　.　　•　
#　　　　.　.　　　　❅•　❅　　　　　　　❅　　　·　.　　　.　*　　　　　.　
#•　　　　　　　　　　　　　　❅　　　　　　　　　　　·　　　❅　·　.·　*　　
#　　*　　　❅　　　　*　·•　.　　　❅　　　.　　•　.　　　*　·•　.　❅•　❅
#　　　　　　.　*　　　　　.　　　**　❅　　..　　　  ❆　❅　*　.　·　  ❅·
#　　　　　　　　　　•·*　·　　　　　•　　❅　❆　　　　　❅·　　❆　❅❆　.·.
#------------ CHRISTMAS BLIZZARD IS COMING LOOK OUT ------------
'''
