import timeit
import random

#devise an experiment that compares the performance of del operator in lists and dictionaries.

tlist = timeit.Timer("del l[random.randint(0,len(l)) -1 ]", "from __main__ import random, l")



resultsList = []
resultsDict = []
for i in range(1000, 1000000, 100000):
    l = list(range(i))
    time1 = tlist.timeit(number=1000)
    resultsList.append(time1)
    l = []





print(resultsList)

