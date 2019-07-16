import turtle


def drawMountain(points, t):
    t.up()
    t.goto(points[0][0], points[0][1])
    t.down()
    t.goto(points[1][0], points[1][1])
    t.goto(points[2][0], points[2][1])
    t.goto(points[3][0], points[3][1])
    t.goto(points[4][0], points[4][1])

def fractalMountain(points, degree, t):
    drawMountain(points, t)
    if degree > 0:
        fractalMountain(
            generateMountainPoints(points[0][0], points[1][0]), degree - 1, t
        )
        fractalMountain(
            generateMountainPoints(points[3][0], points[4][0]), degree -1 , t
        )


def pointsNewMountain(points):
    newPoints = []
    newPoints.append(points[0])


def generateMountainPoints(ini, end):
    mid = (ini + end) // 2
    if ini < 0:
        h = (abs(ini) - abs(end)) //2
    else:
        h = (end - abs(ini)) // 2
    point1 = [ini,0]
    point2 = [(ini + mid) // 2 ,0]
    point3 = [mid, h]
    x = (point3[0] - point2[0]) + point3[0]
    point4 = [x, 0 ]
    point5 = [end, 0]
    return [point1,point2,point3,point4,point5]


def main():
    t = turtle.Turtle()
    win = turtle.Screen()
    iniPoints = generateMountainPoints(-400, 400)
    fractalMountain(iniPoints, 5, t)
    win.exitonclick()

main()