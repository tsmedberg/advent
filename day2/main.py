file = open('day2/input')
lines = file.readlines()

def getScore(char):
    char = char.replace('X','A').replace('Y','B').replace('Z','C')
    return ord(char)-64
def calculateWin(me,opponent):
    win = me - opponent
    if win == -2:
        return 1
    elif win == 2:
        return -1
    return win
def calculateMe(opponent, outcome):
    me = opponent + outcome
    if me == 0:
        return 3
    if me == 4:
        return 1
    return me

scoreWin = 0
for line in lines:
    opponent = getScore(line[0])
    me = getScore(line[2])
    win = calculateWin(me, opponent)
    if(win == 1):
        scoreWin = scoreWin + 6 + me
    elif(win == -1):
        scoreWin = scoreWin + me
    elif win == 0:
        scoreWin = scoreWin + 3 + me

scoreOutcome = 0
for line in lines:
    opponent = getScore(line[0])
    outcome = 0
    if line[2] == 'X':
        outcome = -1
    elif line[2] == 'Z':
        outcome = 1
    me = calculateMe(opponent, outcome)
    if(outcome == 1):
        scoreOutcome = scoreOutcome + 6 + me
    elif(outcome == -1):
        scoreOutcome = scoreOutcome + me
    elif outcome == 0:
        scoreOutcome = scoreOutcome + 3 + me

print('Win',scoreWin)
print('Outcome',scoreOutcome)