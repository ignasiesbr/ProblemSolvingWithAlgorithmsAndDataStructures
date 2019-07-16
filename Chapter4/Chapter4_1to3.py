# 1. factorial

def fact(n):
    if n <= 1:
         return 1
    else:
        return n * fact(n - 1)

print(fact(5))

# 2. reverse a list

def reverse(l):
    if len(l) == 1:
        return [l[0]]
    else:
        return reverse(l[1:]) + [l[0]]

print(reverse([1,2,3,4,5]))

# 3.

# Done in Self_Check 4.5

