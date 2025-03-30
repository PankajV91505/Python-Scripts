# using loop 

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")


# using recursion

def factorial(n):
    if n<2:
        return 1
    else:
        return n * (factorial(n-1))

num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is: {result}")
    