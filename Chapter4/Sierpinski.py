import turtle

def drawTriangle(points, color, turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0], points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()

def getMid(p1, p2):
    return [(p1[0] + p2[0]) / 2, (p1[1]+ p2[1]) / 2]

def sierpinski(points, degree, turtle):
    colormap = ['blue', 'red', 'green', 'white', 'yellow',
                'violet', 'orange']
    drawTriangle(points, colormap[degree], turtle)
    if degree > 0:
        sierpinski([points[0],
                    getMid(points[0], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, turtle)
        sierpinski([points[1],
                    getMid(points[0], points[1]),
                    getMid(points[1], points[2])],
                   degree - 1, turtle)
        sierpinski([points[2],
                    getMid(points[2], points[1]),
                    getMid(points[0], points[2])],
                   degree - 1, turtle)

def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    points = [[-200,-100], [0, 200], [200,-100]]
    sierpinski(points,6, t)
    win.exitonclick()