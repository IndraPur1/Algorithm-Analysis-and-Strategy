import math

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

def factorial(n, arr, p):
    if p == 1:
        return sum(fibonacci(x) for x in arr)
    elif p == 2:
        return sum(math.factorial(x) for x in arr)
    else:
        return 0


n = int(input())
arr = list(map(int, input().split()))
p = int(input())
print(factorial(n, arr, p))