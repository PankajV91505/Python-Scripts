num = int(input("Enter a number: "))

def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(f"{num} is an {even_or_odd(num) } number.")