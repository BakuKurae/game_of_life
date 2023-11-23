def factorial(n):
    Total = 1
    for i in range(1,n + 1):
        Total = Total * i
    return Total

def factorialII(n):
    if n < 1:
        return 1
    return n * factorialII(n-1)

print(factorialII(7))