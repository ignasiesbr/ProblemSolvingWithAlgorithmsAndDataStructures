# Implement mergeSort without the slice operator.
import random

def merge(list, l, m, r):

    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(n1):
        L[i] = list[l + i]
    for j in range(n2):
        R[j] = list[m + 1 + j]
    i = 0
    j = 0
    k = l
    while (i < n1) and (j < n2):
        if (L[i] <= R[j]):
            list[k] = L[i]
            i = i + 1
            k = k + 1
        else:
            list[k] = R[j]
            j = j + 1
            k = k + 1
    while (i < n1):
        list[k] = L[i]
        i = i + 1
        k = k + 1
    while (j < n2):
        list[k] = R[j]
        j = j + 1
        k = k + 1

def mergeSort(l, start, end):
    if start < end:
        mid = (start + end) // 2
        mergeSort(l, start, mid)
        mergeSort(l, mid + 1, end)
        #Merge the two halves.
        merge(l, start, mid, end)




l = [random.randint(1,100) for i in range(100)]
mergeSort(l,0,len(l) -1)
