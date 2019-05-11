def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        recurse = n * recurse
        return recurse


print(factorial(3))