def moveTower(height, frompole, topole, withPole):
    if height >= 1:
        moveTower(height - 1, frompole, withPole, topole)
        moveDisk(frompole,topole)
        moveTower(height - 1, withPole, topole, frompole)

def moveDisk(fromPole, toPole):
    print("moving disk " + fromPole + " to " + toPole)


