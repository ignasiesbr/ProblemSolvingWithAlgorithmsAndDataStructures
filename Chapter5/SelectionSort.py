def selectionSort(lon):
    for x in range(len(lon) - 1, 0, -1):
        posmax = 0
        for y in range(1,x+1):
            if lon[y] > lon[posmax]:
                posmax = y
        temp = lon[x]
        lon[x] = lon[posmax]
        lon[posmax] = temp

lon = [2,3,5,1,3,6,2,8,10,12,3,19]

selectionSort(lon)
print(lon)
