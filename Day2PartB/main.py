# Programmer: Aiden Peace
# Date: Dec, 6th 2022
# Program : Day 2: Rock Paper Scissors PART 2
# website URL: https://adventofcode.com/2022/day/2#part2
# -------------------------------------------------------------------------------------------------------
# Prompt:
# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column
# says how the round needs to end: X means you need to lose, Y means you need to end the round
# in a draw, and Z means you need to win. Good luck!"
#
# The total score is still calculated in the same way, but now you need to figure out what shape to
# choose so the round ends as indicated. The example above now goes like this:
#
#   - In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y),
#     so you also choose Rock. This gives you a score of 1 + 3 = 4.
#   - In the second round, your opponent will choose Paper (B), and you choose Rock, so you lose (X) with
#     a score of 1 + 0 = 1.
#   - In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
#
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.
#
# Following the Elf's instructions for the second column, what would your total score be if
# everything goes exactly according to your strategy guide?
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
    roundOptions = characters[2::4]

    # we do not need this list, but it may
    # be helpful for the future programmer
    # to have a list of elf2 Plays during
    # the game keep in mind elf 2 is Y
    # OUR plays during game!
    elf2Choices = []

for i in (range(len(elf1Choices))):
    # ------------------------ START OF HANDLING DRAWS ------------------------
    # if elf1 and elf2 BOTH play rock during any round
    # rock = 1 point
    # draw = 3 points
    # each player gets 4 points in this case
    if elf1Choices[i] == 'A' and roundOptions[i] == 'Y':
        elf2Choices.append(elf1Choices[i])
        rockDrawScore = ROCK_SCORE + DRAW_ROUND_SCORE
        elf1Score += rockDrawScore
        elf2Score += rockDrawScore
    # if elf1 and elf2 BOTH play paper during any round
    # paper = 2 point
    # draw = 3 points
    # each player gets 5 points in this case
    elif elf1Choices[i] == 'B' and roundOptions[i] == 'Y':
        elf2Choices.append(elf1Choices[i])
        paperDrawScore = PAPER_SCORE + DRAW_ROUND_SCORE
        elf1Score += paperDrawScore
        elf2Score += paperDrawScore
    # if elf1 and elf2 play scissor during any round
    # scissor = 3 point
    # draw = 3 points
    # each player gets 5 points in this case
    elif elf1Choices[i] == 'C' and roundOptions[i] == 'Y':
        elf2Choices.append(elf1Choices[i])
        scissorsDrawScore = SCISSOR_SCORE + DRAW_ROUND_SCORE
        elf1Score += scissorsDrawScore
        elf2Score += scissorsDrawScore
    # -------------------- ^^^ END OF HANDLING DRAWS ^^^ --------------------

    # --------------------- START OF HANDLING ELF2 LOSSES --------------------
    # if elf1 plays rock and elf2 plays scissors
    # rock = 1 point
    # scissor = 3 point
    # draw = 3 points
    # elf1 one wins (=7points) and elf2 losses(=3points)
    if elf1Choices[i] == 'A' and roundOptions[i] == 'X':
        elf2Choices.append('C')
        elf1Wins_RockBeatsScissors = ROCK_SCORE + WON_ROUND_SCORE
        elf2Losses_ScissorsLossesToRock = SCISSOR_SCORE + LOSE_ROUND_SCORE
        elf1Score += elf1Wins_RockBeatsScissors
        elf2Score += elf2Losses_ScissorsLossesToRock
    # if elf1 plays scissors and elf2 plays paper
    # rock = 1 point
    # scissor = 3 point
    # draw = 3 points
    # elf1 one wins (=7points) and elf2 losses(=2points)
    elif elf1Choices[i] == 'C' and roundOptions[i] == 'X':
        elf2Choices.append('B')
        elf1Wins_ScissorsBeatsPaper = SCISSOR_SCORE + WON_ROUND_SCORE
        elf2Losses_PaperLossesToScissors = PAPER_SCORE + LOSE_ROUND_SCORE
        elf1Score += elf1Wins_ScissorsBeatsPaper
        elf2Score += elf2Losses_PaperLossesToScissors
    # if elf1 plays paper and elf2 plays rock.
    # rock = 1 point
    # paper = 2 point
    # draw = 3 points
    # elf1 one wins (=8points) and elf2 losses (=1points)
    elif elf1Choices[i] == 'B' and roundOptions[i] == 'X':
        elf2Choices.append('A')
        elf1Wins_PaperBeatsRock = PAPER_SCORE + WON_ROUND_SCORE
        elf2Losses_RockLossesToPaper = ROCK_SCORE + LOSE_ROUND_SCORE
        elf1Score += elf1Wins_PaperBeatsRock
        elf2Score += elf2Losses_RockLossesToPaper

    # -------------------- ^^^ END OF HANDLING ELF2 LOSSES ^^^ --------------------

    # --------------------- START OF HANDLING ELF2 WINS --------------------
    # if elf2 plays rock and elf1 plays scissors
    # rock = 1 point
    # scissor = 3 point
    # draw = 3 points
    # elf1 one wins (=7points) and elf2 losses(=3points)
    if elf1Choices[i] == 'C' and roundOptions[i] == 'Z':
        elf2Choices.append('A')
        elf2Wins_RockBeatsScissors = ROCK_SCORE + WON_ROUND_SCORE
        elf1Losses_ScissorsLossesToRock = SCISSOR_SCORE + LOSE_ROUND_SCORE
        elf2Score += elf2Wins_RockBeatsScissors
        elf1Score += elf1Losses_ScissorsLossesToRock
    # if elf2 plays scissors and elf1 plays paper
    # rock = 1 point
    # scissor = 3 point
    # draw = 3 points
    # elf2 one wins (=7points) and elf1 losses(=2points)
    elif elf1Choices[i] == 'B' and roundOptions[i] == 'Z':
        elf2Choices.append('C')
        elf2Wins_ScissorsBeatsPaper = SCISSOR_SCORE + WON_ROUND_SCORE
        elf1Losses_PaperLossesToScissors = PAPER_SCORE + LOSE_ROUND_SCORE
        elf2Score += elf2Wins_ScissorsBeatsPaper
        elf1Score += elf1Losses_PaperLossesToScissors
    # if elf2 plays paper and elf1 plays rock.
    # rock = 1 point
    # paper = 2 point
    # draw = 3 points
    # elf2 one wins (=8points) and elf1 losses (=1points)
    elif elf1Choices[i] == 'A' and roundOptions[i] == 'Z':
        elf2Choices.append('B')
        elf2Wins_PaperBeatsRock = PAPER_SCORE + WON_ROUND_SCORE
        elf1Losses_RockLossesToPaper = ROCK_SCORE + LOSE_ROUND_SCORE
        elf2Score += elf2Wins_PaperBeatsRock
        elf1Score += elf1Losses_RockLossesToPaper

    # -------------------- ^^^ END OF HANDLING ELF2 WINS ^^^ --------------------
print("Your Elf opponent Rock-Paper-Scissor Game Score is: ", elf1Score)
print("Your Elf Rock-Paper-Scissor Game Score is:", elf2Score)

if elf2Score > elf1Score:
    print("You Win!")
elif elf1Score > elf2Score:
    print("You Lose")
elif elf1Score == elf2Score:
    print("Tie")
else:
    print("Tell Programmer (Aiden Peace) Something is wrong! :( ")

# ------------- MERRY CHRISTMAS DAY 2 FROM AIDEN PEACE -------------
#   *    *     *      *      *    *   *    *    *     *        *
#  *       *   * *        *    *      *        *       *      *
#   * |,\/,| |[_' |[_]) |[_]) \\// *     *       *     *    *
#  *  ||\/|| |[_, ||'\, ||'\,  ||    *      *   *    *    *     *
#   *   *     *    *      *    *      *     *     *      *   *
#     *    *  ___ __ __ ____  __  __  ____  _  _    __    __     *
#  *    *    // ' |[_]| |[_]) || ((_' '||' |,\/,|  //\\  ((_'  *
#     *    * \\_, |[']| ||'\, || ,_))  ||  ||\/|| //``\\ ,_))
#   *    *     *      *      *    *   *    *    *     *        *
# *       *   * *        *    *      *        *       *   *      *
# -----------------------------------------------------------------
