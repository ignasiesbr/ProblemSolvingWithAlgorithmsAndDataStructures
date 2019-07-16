# 14. Art thief problem
#loi is a list of items
# an item is an structure [Item, Weight, Value]

loi = [[1,2,3], [2,3,4], [3,4,8], [4,5,8], [5,9,10]]

# Max Weight = 20
# haul?

#normal recursive solution

def knapsack(loi, weight):
    if len(loi) == 0:
        return 0
    elif loi[0][1] > weight:
        return knapsack(loi[1:], weight)
    else:
        return max((loi[0][2] + knapsack(loi[1:], weight - loi[0][1])), knapsack(loi[1:], weight))

#print(knapsack(loi, 20))

#dynamic solution
#loi = list of items, w = weight, low = list of weights, n = aux to traverse the lists
def dynKnapsack(loi, w, low):
    if len(loi) == 0:
        return 0
    elif low[w] is not 0:
        return low[w]
    elif loi[0][1] > w:
        return dynKnapsack(loi[1:], w, low)
    else:
        res = max(loi[0][2] + dynKnapsack(loi[1:], w - loi[0][1], low), dynKnapsack(loi[1:], w, low))
        low[w] = res
        return res

low = [0] * 21
print(dynKnapsack(loi, 20 , low))