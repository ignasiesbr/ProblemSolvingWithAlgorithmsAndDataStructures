# 10. Implement bubble sort using simultaneous assignment

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0 , -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

l = [2,3,4,1,5,1,9,10,2,21,2,54,12]
bubbleSort(l)
print(l)
