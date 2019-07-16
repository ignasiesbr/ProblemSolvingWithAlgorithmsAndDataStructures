# 9. Two jugs problem
# 10.
#A Jug is a list [Liters , Cap, label]

# Assume jug1 is larger than jug2
def jugProblem(jug1, jug2, res):
    # If we have the res liters in the larger jug -> Solution
    if jug1[0] == res:
        return jug1
    #if we have the res liters in the smaller jug -> Solution, empty the first jug and fill the largest with the other
    elif jug2[0] == res:
        empty(jug1)
        fill(jug2,jug1)
        return jug1
    # if we can get the solution adding the liters in the smaller jug and its capacity -> Solution
    elif jug2[1] + jug2[0] == res:
        empty(jug1)
        fill(jug2,jug1)
        pump(jug2)
        fill(jug2,jug1)
    else:
        pump(jug2)
        fill(jug2,jug1)
        return jugProblem(jug1,jug2,res)

def pump(jug):
    jug[0] = jug[1]
    print("Pumping " + jug[2])

def fill(fromJug, toJug):
    print("Filling " + toJug[2] + " with " + fromJug[2])
    for i in range(fromJug[0]):
        if toJug[0] < toJug[1]:
            toJug[0] = toJug[0] + 1
            fromJug[0] = fromJug[0] - 1

def empty(jug):
    print("Emptying the " + jug[2])
    jug[0] = 0


jug4l = [0, 4, "Jug 4L"]
jug3l = [0, 3, "Jug 3L"]


jugProblem(jug4l,jug3l,2)

#Another example, with 5L and 2L get 3L in jug of 5L

jug5 = [0 , 5, "Jug 5L."]
jug2 = [0,2,"Jug 2L."]

jugProblem(jug5,jug2,3)

