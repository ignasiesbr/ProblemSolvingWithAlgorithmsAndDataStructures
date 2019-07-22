import random
import timeit

from MergeSort import mergeSort
from InsertionSort import insertionSort
from SelectionSort import selectionSort
from BubbleSort import shortBubbleSort
from ShellSort import shellSort
from QuickSort import quickSort

# list of 500 random integers.
l = []
for i in range(500):
    l.append(random.randint(1,500))


g = l.copy()

tMerge = timeit.Timer("mergeSort(g)" , "from __main__ import g, mergeSort" )
rMerge = tMerge.timeit(number=1)
print("Time to sort using MergeSort = "  + str(rMerge))

g = l.copy()
tInsert = timeit.Timer("insertionSort(g)", "from __main__ import g, insertionSort")
rInsert = tInsert.timeit(number=1)
print("Time to sort using InsertionSort= " + str(rInsert))

g = l.copy()
tSelect = timeit.Timer("selectionSort(g)", "from __main__ import g, selectionSort")
rSelect = tSelect.timeit(number=1)
print("Time to sort using SelectionSort= " + str(rSelect))

g = l.copy()
tBubble = timeit.Timer("shortBubbleSort(g)", "from __main__ import g, shortBubbleSort")
rBubble = tBubble.timeit(number=1)
print("Time to sort using shortBubbleSort= " + str(rBubble))

g = l.copy()
tShell = timeit.Timer("shellSort(g)" , "from __main__ import g, shellSort")
rShell = tShell.timeit(number=1)
print("Time to sort using ShellSort= "+ str(rShell))

g = l.copy()
tQuick = timeit.Timer("quickSort(g)" , "from __main__ import g, quickSort")
rQuick = tQuick.timeit(number=1)
print("Time to sort using QuickSort= " + str(rQuick))


# Results:
# Time to sort using MergeSort = 0.0035496800000001105
# Time to sort using InsertionSort= 0.023419351000000033
# Time to sort using SelectionSort= 0.020853787000000068
# Time to sort using shortBubbleSort= 0.04546780499999992
# Time to sort using ShellSort= 0.002926839999999986
# Time to sort using QuickSort= 0.002063303999999988
