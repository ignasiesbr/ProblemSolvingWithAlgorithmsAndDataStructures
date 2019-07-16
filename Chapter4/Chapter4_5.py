# 5. Write a function that computes the fib sequence.

def fibo(n):
    if n<=2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

