import math
num = int(input("Enter a number: "))

def square_root(n):
    return math.sqrt(n)
print(f"Square root of {num} is: {square_root(num)}")

def natural_log(n):
    return math.log(n)
print(f"logarithm of {num} is: {natural_log(num)}")

def sine_radians(n):
    return math.sin(n)
print(f"Sine of {num} is: {sine_radians(num)}")

def cosine_radians(n):
    return math.cos(n)
print(f"Cosine of {num} is: {cosine_radians(num)}")