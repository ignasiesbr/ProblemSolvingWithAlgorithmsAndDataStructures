
#5. Make the algorithm linear
#List-Of-Number -> Number
#Find the minimum number of a LoN
#Performance: O(n)
def minimum(lon):
    min = lon[0]
    for i in lon:
        if min > i:
            min = i
    return min


#4. O(n*log(n)) algorithm
#Performance nlon(n), sort list in py have this performance

def minimum2(lon):
    lon.sort()
    return lon[0]


list = [1,2,3,4,5,6,7,8,1,2,5,8,0,2,1,5,67,8,9]
print(minimum(list))
print(minimum2(list))