# 11. Implement bubbleSort so it bubbles in both directions.

def bubbleSort(alist):
    swapped = True
    start = 0
    end = len(alist) - 1
    while swapped:
        swapped = False
        for i in range(start,end):
            if (alist[i] > alist[i+1]):
                alist[i], alist[i+1] = alist[i+1], alist[i]
                swapped = True
        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end,start - 1, -1):
            if (alist[i] > alist[i+1]):
                alist[i], alist[i+1] = alist[i+1], alist[i]
                swapped = True

        start = start + 1


