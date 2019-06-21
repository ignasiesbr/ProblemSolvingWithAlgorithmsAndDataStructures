import random


# SelfCheck
# Infinite Monkey theorem


def generateRandomString(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for i in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res


def generateScore(rand):
    goal = "methinks it is like a weasel"
    score = 0
    for i in range(len(rand)):
        if rand[i] == goal[i]:
            score = score + 1
    return score


def trials(nOfTrials):
    bestScore = 0
    bestResult = ""
    for i in range(nOfTrials):
        randomString = generateRandomString(27)
        current = generateScore(randomString)
        if current > bestScore:
            bestScore = current
            bestResult = randomString

    return bestResult, bestScore


def generateStringHillClimbing(strlen, word):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    goal = "methinks it is like a weasel"
    for i in range(strlen):
        if word[i] != goal[i]:
            res = res + alphabet[random.randrange(27)]
        else:
            res = res + word[i]
    return res


def trials2():
    bestScore = 0
    bestResult = ""
    current = generateRandomString(28)
    trials = [0, current]
    while generateScore(current) != 28:
        current = generateStringHillClimbing(28, current)
        trials[0] = trials[0] + 1
        trials[1] = current

    return trials

#return the number of trials needed to accomplish the word keeping the good results
trials2()