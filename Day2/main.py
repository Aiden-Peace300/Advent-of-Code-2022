# Programmer: Aiden Peace
# Date: Dec, 5th 2022
# Program : Day 2: Rock Paper Scissors
# website URL: https://adventofcode.com/2022/day/2
# -------------------------------------------------------------------------------------------------------
# Prompt:
# The Elves begin to set up camp on the beach. To decide whose tent gets to be closest to the snack
# storage, a giant Rock Paper Scissors tournament is already in progress.
#
# Rock Paper Scissors is a game between two players. Each game contains many rounds; in each round,
# the players each simultaneously choose one of Rock, Paper, or Scissors using a hand shape. Then,
# a winner for that round is selected: Rock defeats Scissors, Scissors defeats Paper, and Paper
# defeats Rock. If both players choose the same shape, the round instead ends in a draw.
#
# Appreciative of your help yesterday, one Elf gives you an encrypted strategy guide
# (your puzzle input) that they say will be sure to help you win. "The first column is what
# your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second
# column--" Suddenly, the Elf is called away to help with someone's tent.
#
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper,
# and Z for Scissors. Winning every time would be suspicious, so the responses must have been
# carefully chosen.
#
# The winner of the whole tournament is the player with the highest score. Your total score is the
# sum of your scores for each round. The score for a single round is the score for the shape you
# selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the
# round (0 if you lost, 3 if the round was a draw, and 6 if you won).
#
# Since you can't be sure if the Elf is trying to help you or trick you, you should calculate
# the score you would get if you were to follow the strategy guide.
#
# For example, suppose you were given the following strategy guide:
#
# A Y
# B X
# C Z
# This strategy guide predicts and recommends the following:
#
#   - In the first round, your opponent will choose Rock (A), 4, and
#     you should choose Paper (Y). This ends in a win for
#     you with a score of 8 (2 because you chose Paper + 6
#     because you won).
#   - In the second round, your opponent will choose Paper (B), and
#     you should choose Rock (X). This ends in a loss for you with
#     a score of 1 (1 + 0).
#   - The third round is a draw with both players choosing
#     Scissors, giving you a score of 3 + 3 = 6.
#
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).
# What would your total score be if everything goes exactly according to your strategy guide? ->
# -------------------------------------------------------------------------------------------------------

# we will need this variable ‘characters’ to hold input file information In list format
characters = []

# variables to hold elf score
elf1Score = 0           # elf1Score is your elf opponent Score
elf2Score = 0           # elf2Score is your elf Score

# constant to hold stagnant score
ROCK_SCORE = 1          # ROCK_SCORE is constant because the score for rock will always be 1
PAPER_SCORE = 2         # PAPER_SCORE is constant because the score for rock will always be 2
SCISSOR_SCORE = 3       # SCISSOR_SCORE is constant because the score for rock will always be 1
LOSE_ROUND_SCORE = 0    # LOSE_ROUND_SCORE is constant because the score for losing will always be 0
DRAW_ROUND_SCORE = 3    # DRAW_ROUND_SCORE is constant because the score for a drawing will always be 3
WON_ROUND_SCORE = 6     # WON_ROUND_SCORE is constant because the score for a winning will always be 6

# opening file to READ in one char at a time til end of the file is reached
with open('input.txt', 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            # then we have reached end of the file
            break
        characters.append(char)

    # creating list for the first elf's plays during the game
    elf1Choices = characters[::4]

    # creating list for the first elf's plays during the game
    elf2Choices = characters[2::4]

for i in (range(len(elf1Choices))):
    # ------------------------ START OF HANDLING DRAWS ------------------------
    # if elf1 and elf2 BOTH play rock during any round
    # rock = 1 point
    # draw = 3 points
    # each player gets 4 points in this case
    if elf1Choices[i] == 'A' and elf2Choices[i] == 'X':
        rockDrawScore = ROCK_SCORE + DRAW_ROUND_SCORE
        elf1Score += rockDrawScore
        elf2Score += rockDrawScore
    # if elf1 and elf2 BOTH play paper during any round
    # paper = 2 point
    # draw = 3 points
    # each player gets 5 points in this case
    elif elf1Choices[i] == 'B' and elf2Choices[i] == 'Y':
        paperDrawScore = PAPER_SCORE + DRAW_ROUND_SCORE
        elf1Score += paperDrawScore
        elf2Score += paperDrawScore
    # if elf1 and elf2 play scissor during any round
    # scissor = 3 point
    # draw = 3 points
    # each player gets 5 points in this case
    elif elf1Choices[i] == 'C' and elf2Choices[i] == 'Z':
        scissorsDrawScore = SCISSOR_SCORE + DRAW_ROUND_SCORE
        elf1Score += scissorsDrawScore
        elf2Score += scissorsDrawScore
    # -------------------- ^^^ END OF HANDLING DRAWS ^^^ --------------------

    # --------------------- START OF HANDLING ELF1 WINS --------------------
    # if elf1 plays rock and elf2 plays scissors
    # rock = 1 point
    # scissor = 3 point
    # draw = 3 points
    # elf1 one wins (=7points) and elf2 losses(=3points)
    if elf1Choices[i] == 'A' and elf2Choices[i] == 'Z':
        elf1Wins_RockBeatsScissors = ROCK_SCORE + WON_ROUND_SCORE
        elf2Losses_ScissorsLossesToRock = SCISSOR_SCORE + LOSE_ROUND_SCORE
        elf1Score += elf1Wins_RockBeatsScissors
        elf2Score += elf2Losses_ScissorsLossesToRock
    # if elf1 plays scissors and elf2 plays paper
    # rock = 1 point
    # scissor = 3 point
    # draw = 3 points
    # elf1 one wins (=7points) and elf2 losses(=2points)
    elif elf1Choices[i] == 'C' and elf2Choices[i] == 'Y':
        elf1Wins_ScissorsBeatsPaper = SCISSOR_SCORE + WON_ROUND_SCORE
        elf2Losses_PaperLossesToScissors = PAPER_SCORE + LOSE_ROUND_SCORE
        elf1Score += elf1Wins_ScissorsBeatsPaper
        elf2Score += elf2Losses_PaperLossesToScissors
    # if elf1 plays paper and elf2 plays rock.
    # rock = 1 point
    # paper = 2 point
    # draw = 3 points
    # elf1 one wins (=8points) and elf2 losses (=1points)
    elif elf1Choices[i] == 'B' and elf2Choices[i] == 'X':
        elf1Wins_PaperBeatsRock = PAPER_SCORE + WON_ROUND_SCORE
        elf2Losses_RockLossesToPaper = ROCK_SCORE + LOSE_ROUND_SCORE
        elf1Score += elf1Wins_PaperBeatsRock
        elf2Score += elf2Losses_RockLossesToPaper

    # -------------------- ^^^ END OF HANDLING ELF1 WINS ^^^ --------------------

    # --------------------- START OF HANDLING ELF2 WINS --------------------
    # if elf2 plays rock and elf1 plays scissors
    # rock = 1 point
    # scissor = 3 point
    # draw = 3 points
    # elf1 one wins (=7points) and elf2 losses(=3points)
    if elf2Choices[i] == 'X' and elf1Choices[i] == 'C':
        elf2Wins_RockBeatsScissors = ROCK_SCORE + WON_ROUND_SCORE
        elf1Losses_ScissorsLossesToRock = SCISSOR_SCORE + LOSE_ROUND_SCORE
        elf2Score += elf2Wins_RockBeatsScissors
        elf1Score += elf1Losses_ScissorsLossesToRock
    # if elf2 plays scissors and elf1 plays paper
    # rock = 1 point
    # scissor = 3 point
    # draw = 3 points
    # elf2 one wins (=7points) and elf1 losses(=2points)
    elif elf2Choices[i] == 'Z' and elf1Choices[i] == 'B':
        elf2Wins_ScissorsBeatsPaper = SCISSOR_SCORE + WON_ROUND_SCORE
        elf1Losses_PaperLossesToScissors = PAPER_SCORE + LOSE_ROUND_SCORE
        elf2Score += elf2Wins_ScissorsBeatsPaper
        elf1Score += elf1Losses_PaperLossesToScissors
    # if elf2 plays paper and elf1 plays rock.
    # rock = 1 point
    # paper = 2 point
    # draw = 3 points
    # elf2 one wins (=8points) and elf1 losses (=1points)
    elif elf2Choices[i] == 'Y' and elf1Choices[i] == 'A':
        elf2Wins_PaperBeatsRock = PAPER_SCORE + WON_ROUND_SCORE
        elf1Losses_RockLossesToPaper = ROCK_SCORE + LOSE_ROUND_SCORE
        elf2Score += elf2Wins_PaperBeatsRock
        elf1Score += elf1Losses_RockLossesToPaper

    # -------------------- ^^^ END OF HANDLING ELF2 WINS ^^^ --------------------
print("Your Elf opponent Rock-Paper-Scissor Game Score is:", elf1Score)
print("Your Elf Rock-Paper-Scissor Game Score is:", elf2Score)

if elf2Score > elf1Score:
    print("You Win!")
elif elf1Score > elf2Score:
    print("You Lose")
elif elf1Score == elf2Score:
    print("Tie")
else:
    print("Tell Programmer (Aiden Peace) Something is wrong! :( ")
