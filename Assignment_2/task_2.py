start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

def sum_of_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total


total_sum = sum_of_range(start, end)
print(f"The sum of numbers from {start} to {end} is: {total_sum}")