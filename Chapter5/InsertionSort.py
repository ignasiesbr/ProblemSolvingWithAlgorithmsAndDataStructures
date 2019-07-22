def insertionSort(lon):
    for index in range(1,len(lon)):
        val = lon[index]
        pos = index
        while pos > 0 and lon[pos - 1] > val:
            lon[pos] = lon[pos - 1]
            pos = pos - 1
        lon[pos] = val

lon = [1,10,2,19,3,3,8,2,5,6,7,21,0]
insertionSort(lon)
print(lon)
