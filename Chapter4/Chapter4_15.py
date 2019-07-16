# 15. edit distance word.

# non dynamic approach.
# if insert = + 20, if delete = + 20, if same = + 5
# transform s1 into s2
# m = len s1, n = len s2

# def strDistance(s1, s2, m, n):
#     # if either of the two strings is empty, insert all the letters at a cost of 20.
#     if m == 0:
#         return (20 * n)
#     if n == 0:
#         return (20 * m)
#     #if the last char is the same, ignore this char and continue the algorithm
#     if s1[m-1] == s2[n-1]:
#         return strDistance(s1,s2, m-1,n-1)
#     else:
#         return min((20 + strDistance(s1,s2,m,n-1)), #insert
#                    (20 + strDistance(s1,s2,m-1,n)), #delete
#                    (5 + strDistance(s1,s2,m-1,n-1)))#replace

def strDistance(s1,s2):
    if len(s1) == 0:
        return (20 * len(s2))
    if len(s2) == 0:
        return (20 * len(s1))
    if s1[0] == s2[0]:
        return strDistance(s1[1:], s2[1:])
    else:
        return min( (20 + strDistance(s1[1:], s2)),     #delete
                    (20 + strDistance(s2[0] + s1,s2)),  #insert
                    (5 + strDistance(s1[1:], s2[1:])))  #replace

print(strDistance("hola", "holi"))
#expected : 5

# with dp approach.


def strDistanceDP(s1, s2, m, n):
    values = [[0 for x in range(m + 1)] for x in range(n + 1)]
    # for all values of m and n (str lengths), fill up the table
    for i in range(m + 1):
        for j in range(n + 1):
            # if the length of s1 is 0, the cost will be insert all the chars of the str objective
            if i == 0:
                values[i][j] = (20 * j)
            # if s2 is "", the cost will be delete all the chars at cost 20 each.
            elif j == 0:
                values[i][j] = (20 * i)
            #if the val of the last char is the same in both strings, we omit this last char and the cost will be the
            # cost without this car
            elif s1[i-1] == s2[j- 1]:
                values[i][j] = values[i - 1][j - 1]
            # else: we calculate the minimum of inserting, deleting and replacing operations.
            else:
                values[i][j] = min( (values[i][j - 1] + 20),# insert
                                    (values[i-1][j] + 20),  # delete
                                    (values[i-1][j-1] + 5)) # replace
    return values[m][n]

print(strDistanceDP("hola", "holi", len("hola"), len("holi")))
#exp: 5


