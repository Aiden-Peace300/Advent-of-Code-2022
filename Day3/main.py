# Programmer: Aiden Peace
# Date: Dec, 11th 2022
# Program : Day 3: Rucksack Reorganization
# website URL: https://adventofcode.com/2022/day/3
# -------------------------------------------------------------------------------------------------------
# Prompt:
# One Elf has the important job of loading all the rucksacks with supplies for the jungle journey.
# Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need
# to be rearranged.
#
# Each rucksack has two large compartments. All items of a given type are meant to go into exactly one
# of the two compartments. The Elf that did the packing failed to follow this rule for exactly one
# item type per rucksack.
#
# The Elves have made a list of all the items currently in each rucksack (your puzzle input), but
# they need your help finding the errors. Every item type is identified by a single lowercase or
# uppercase letter (that is, a and A are referred to different as different types of items).
#
# The list of items for each rucksack is given as characters all on a single line. A given rucksack
# always has the same number of items in each of its two compartments, so the first half of the
# characters represent items in the first compartment, while the second half of the characters
# represent items in the second compartment.
#
# For example, suppose you have the following list of contents from six rucksacks:
#
#   vJrwpWtwJgWrhcsFMMfFFhFp
#   jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
#   PmmdzqPrVvPwwTWBwg
#   wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
#   ttgJtRGJQctTZtZT
#   CrZsJsPPZsGzwwsLwLmpwMDw
#   
# - The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first
#   compartment contains the items vJrwpWtwJgWr, while the second compartment contains the
#   items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
# - The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL.
#   The only item type that appears in both compartments is uppercase L.
# - The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only
#   common item type is uppercase P.
# - The fourth rucksack's compartments only share item type v.
# - The fifth rucksack's compartments only share item type t.
# - The sixth rucksack's compartments only share item type s.

# To help prioritize item rearrangement, every item type can be converted to a priority:
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
#
# In the above example, the priority of the item type that appears in both compartments of
# each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.
#
# Find the item type that appears in both compartments of each rucksack. What is the
# sum of the priorities of those item types?
#
# THE ANSWER IS FOR THE CURRENT input.txt FILE IS THE FOLLOWING:
# "The sum of the rucksacks (input.txt) duplicates is:  7568"
# -------------------------------------------------------------------------------------------------------
# VARIABLES BELOW
duplicates = []      # declaring empty list that will soon hold desired duplicates.
result = 0           # declaring empty total


# convert_duplicates_to_points() function's goal is to convert
# the duplicates found in the first_chunk and second_chunk to
# the desired point system.
#
# BRINGING ATTN TO KEY SENTENCES FROM PROMPT:
# - Lowercase item types a through z have priorities 1 through 26.
# - Uppercase item types A through Z have priorities 27 through 52.
def convert_duplicates_to_points(first_chunk, second_chunk):
    for c in first_chunk:
        if c in second_chunk:
            # handling lower case ascii characters
            # then converting them to desired point
            # system.
            if 97 <= ord(c) <= 122:
                points_for_lower_case = ord(c) - 96
                print("Duplicate at this rucksack is:", c, "The point for", c, "is", points_for_lower_case)
                duplicates.append(points_for_lower_case)
            # handling upper case ascii characters
            # then converting them to desired point
            # system.
            elif 65 <= ord(c) <= 90:
                points_for_upper_case = ord(c) - 38
                print("Duplicate at this rucksack is:", c, "The point for", c, "is", points_for_upper_case)
                duplicates.append(points_for_upper_case)


# read from file
# opening input file and saving each line in a list called 'rucksack_file_list'
with open("input.txt") as file:
    rucksack_file_list = file.readlines()
    rucksack_file_list = [line.rstrip() for line in rucksack_file_list]

for i in rucksack_file_list:
    # splitting rucksack in half we will need
    # list to display to user
    firstCompartment = i[:len(i)//2]
    secondCompartment = i[len(i) // 2:]

    # we will need sets to avoid having duplicates later on
    firstCompartmentSet = set(firstCompartment)
    secondCompartmentSet = set(secondCompartment)

    print("Current value is:", i)
    print("First Compartment of current value is:", firstCompartment)
    print("Second Compartment of current value is:", secondCompartment)

    # implementing convert_duplicates_to_points() function
    # we have to use pass in sets to make sure our duplicates list
    # (ironically enough) won't have any duplicates of duplicates
    # while working one rucksack.
    convert_duplicates_to_points(firstCompartmentSet, secondCompartmentSet)

    # Use the sum function to add up all the elements in the list
    result = sum(duplicates)
    print()     # for spacing purposes during outputting

# Print the sum aka "result" at the very end of the program
print("The sum of the rucksacks (input.txt) duplicates is: ", result, "\n")

''' ----- HAPPY HOLIDAYS DAY 3 FROM AIDEN PEACE -----
⠀⠀⠀⠀⠀⠀⣠⣴⣶⣶⣦⣄⠀⠀⠀⠀⠀⠀   
⠀⠀⠀⠀⠀⢰⣿⡟⢻⡟⢻⣿⡆⠀⠀⠀⠀⠀
⠀⣀⣀⠀⠀⠸⣿⣿⣻⣟⣿⣿⠇⠀⠀⣀⣀⠀
⣾⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢻⣿⣷
⠘⠛⠁⠿⠿⣿⣿⣿⣇⣸⣿⣿⣿⡿⠿⠈⠛⠃
⠀⠀⠀⠀⠀⠈⣿⣿⡟⢻⣿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⣿⣿⣷⣾⣿⣿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⣿⣿⣿⠇⠸⣿⣿⣿⣇⠀⠀⠀⠀
⠀⠀⠀⢰⣦⣭⣉⠋⠀⠀⠙⣉⣭⣴⡆⠀⠀⠀
⠀⠀⠀⠘⠿⠿⠟⠀⠀⠀⠀⠻⠿⠿⠃⠀
------------------------------------------------- '''
