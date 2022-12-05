# Programmer: Aiden Peace
# Date: Dec, 4th 2022
# Program : Day 1: Calorie Counting (PART B/PART 2) 
# website URL: https://adventofcode.com/2022/day/1
# -------------------------------------------------------------------------------------------------------
# Prompt:
# By the time you calculate the answer to the Elves' question, they've already realized that the Elf
# carrying the most Calories of food might eventually run out of snacks.
#
# To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried
# by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of
# snacks, they still have two backups.
#
# In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third
# Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried
# by these three elves is 45000.
#
# Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
# -------------------------------------------------------------------------------------------------------
#
# Aiden's Algo:
# - read from file
# - count up calories of each elf til you reach empty line
# - calc EACH elf's calories
# - compare current elf's calories to last three max elf's calories
# - save the elfs with the most calories.
# - print the elf with the most calories to console/terminal.
#
# -------------------------------------------------------------------------------------------------------

max_elf_calories1 = 0
max_elf_calories2 = 0
max_elf_calories3 = 0

each_elf_sum_of_calories = 0
save = 0

# read from file
# opening input file and saving each line in a list called 'list_of_cals'
with open("input.txt") as file:
    list_of_cals = file.readlines()
    list_of_cals = [line.rstrip() for line in list_of_cals]

# count up calories of each elf til you reach empty line
for line in list_of_cals:
    if line == '':
        # compare current elf's calories to last elf's calories
        if max_elf_calories1 <= each_elf_sum_of_calories:
            max_elf_calories3 = max_elf_calories2
            max_elf_calories2 = max_elf_calories1
            max_elf_calories1 = each_elf_sum_of_calories
        elif max_elf_calories2 <= each_elf_sum_of_calories:
            max_elf_calories3 = max_elf_calories2
            max_elf_calories2 = each_elf_sum_of_calories
        elif max_elf_calories3 <= each_elf_sum_of_calories:
            max_elf_calories3 = each_elf_sum_of_calories

        each_elf_sum_of_calories = 0

    else:
        # calc EACH elf's calories
        each_elf_sum_of_calories += int(line)

# checking to see if last elf's calories was larger than the last
# we have to do this because the last elf won't have a '' behind it
# in the list of 'list_of_cals' so we have to check to see if the
# elf's calories sum is larger than the last elf's calories sum

if max_elf_calories1 <= each_elf_sum_of_calories:
    max_elf_calories3 = max_elf_calories2
    max_elf_calories2 = max_elf_calories1
    max_elf_calories1 = each_elf_sum_of_calories
elif max_elf_calories2 <= each_elf_sum_of_calories:
    max_elf_calories3 = max_elf_calories2
    max_elf_calories2 = each_elf_sum_of_calories
elif max_elf_calories3 <= each_elf_sum_of_calories:
    max_elf_calories3 = each_elf_sum_of_calories

# print the elf with the most calories to console/terminal.
print('The calories of the top three elfs with the most food is: ')
print(max_elf_calories1 + max_elf_calories2 + max_elf_calories3)

'''------------ MERRY CHRISTMAS DAY 1 FROM AIDEN PEACE -------------
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
#--------------- CHRISTMAS BLIZZARD IS COMING LOOK OUT ------------'''
