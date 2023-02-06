def fact(n):
    if n == 1:
        return 1
    
    return fact(n-1) * n

n = 10

print(n, "factorial is", fact(n))

def fib(k):
    if k == 1 or k == 2:
        return 1
    return fib(k-1) + fib(k-2)

k = 10

print("The",k,"th fibonacci number is", fib(k))