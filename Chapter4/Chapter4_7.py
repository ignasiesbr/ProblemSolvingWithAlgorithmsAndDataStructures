# 7. Hilbert curve
import turtle

def hilbert(degree, size, t, angle):
    if degree > 0:
        t.right(angle)
        hilbert(degree - 1, size,t, -angle)
        t.forward(size)
        t.left(angle)
        hilbert(degree - 1,size, t, angle)
        t.forward(size)
        hilbert(degree - 1, size, t, angle)
        t.left(angle)
        t.forward(size)
        hilbert(degree - 1, size, t, -angle)
        t.right(angle)



def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    hilbert(4,10,t,90)
    win.exitonclick()

main()