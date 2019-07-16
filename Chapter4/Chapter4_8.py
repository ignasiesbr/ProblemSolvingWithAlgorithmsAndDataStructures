# Koch snowflake
import turtle


def koch(degree, length, t):
    if degree == 0:
        t.forward(length)
    else:
        koch(degree - 1, length/3, t)
        t.right(60)
        koch(degree - 1, length/3, t)
        t.left(120)
        koch(degree - 1, length / 3, t)
        t.right(60)
        koch(degree - 1, length / 3, t)

t = turtle.Turtle()
win = turtle.Screen()
for i in range(6):
    koch(3,50,t)
    t.right(60)

win.exitonclick()
