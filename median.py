"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers =[float(value) for value in input().split(",")]
        numbers.sort()
        middle = len(numbers) // 2
        median = (numbers[middle] + numbers[~middle]) / 2
            
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print(f'The median of this list is: {median}')
