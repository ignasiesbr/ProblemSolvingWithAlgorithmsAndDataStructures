# 12. Modify the tower of hanoi using turtle.
import turtle


# Positions relatives to pole: A = 100, B = 200, C = 300


lotA = []
lotB = []
lotC = []
turtles = [lotA,lotB,lotC]
val = [100, 200, 300]
poles = ["A", "B", "C"]

def moveTower(height, frompole, topole, withPole):
    if height >= 1:
        moveTower(height - 1, frompole, withPole, topole)
        moveDisk(frompole,topole)
        moveTower(height - 1, withPole, topole, frompole)

def moveDisk(fromPole, toPole):
    #Extract the index from the fromPole and the toPole
    indexFrom = poles.index(fromPole)
    indexTo = poles.index(toPole)
    # Get the value (y. coord) associated with the toPole
    v = val[indexTo]
    # get the list of which we will get the turtle (disk).
    l = turtles[indexFrom]
    # Retrieve the disk that is about to be moved and insert it into the list (pole) where it is going.
    t = l.pop()
    lto = turtles[indexTo]
    lto.append(t)
    # Move graphically the turtle (disk)
    t.goto(v, len(lto) * 10 - 10)

def ini(h):
    for i in range(h):
        t = turtle.Turtle()
        t.up()
        t.speed(1)
        t.shape("square")
        t.shapesize(0.25,1,None)
        t.goto(100, 10*i)
        lotA.append(t)

def hanoi(h,pole1,pole2,pole3):
    ini(h)
    moveTower(h,pole1,pole2,pole3)

win = turtle.Screen()
hanoi(4,"A","B","C")
win.exitonclick()