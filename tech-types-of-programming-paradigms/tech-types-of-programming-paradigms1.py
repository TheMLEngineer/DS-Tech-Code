def factorial(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    return result

num = 5
print("Factorial of", num, "is", factorial(num))
