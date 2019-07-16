import turtle
import random


def tree(branchLen,t):
    if branchLen > 5:
        if branchLen < 20:
            t.color("green")
        else:
            t.color("brown")
        t.width(branchLen*0.08)
        t.forward(branchLen)
        n = random.randint(15,35)
        t.right(n)
        tree(branchLen - random.randint(5 ,20),t)
        t.left(2*n)
        tree(branchLen-random.randint(5, 20) ,t)
        t.right(n)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("brown")
    tree(75,t)
    myWin.exitonclick()


main()