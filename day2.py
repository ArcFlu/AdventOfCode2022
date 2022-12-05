# Rock, Paper, Scissors
winningChoice = {"A":"Y", "B":"Z", "C":"X"}
tieChoice = {"A":"X", "B":"Y", "C":"Z"}
losingChoice = {"A":"Z", "B":"X", "C":"Y"}

shapeScore = {"X":1, "Y":2, "Z":3}

score = 0

# Pt 1
# with open('day2pt1.in') as f:
#     for line in f:
#         line = line.rstrip()

#         elfChoice = line[0]
#         playerChoice = line[2]

#         if (winningChoice[elfChoice] == playerChoice):
#             score += shapeScore[playerChoice] + 6
#         elif (tieChoice[elfChoice] == playerChoice):
#             score += shapeScore[playerChoice] + 3
#         else:
#             score += shapeScore[playerChoice]

# Pt 2
with open('day2pt1.in') as f:
    for line in f:
        line = line.rstrip()

        elfChoice = line[0]
        outcome = line[2]
        playerChoice = ""

        # X = Lose, Y = Draw, Z = Win

        if outcome == "X":
            playerChoice = losingChoice[elfChoice]
            score += 0
        elif outcome == "Y":
            playerChoice = tieChoice[elfChoice]
            score += 3
        else:
            playerChoice = winningChoice[elfChoice]
            score += 6
        
        score += shapeScore[playerChoice]

print(score)