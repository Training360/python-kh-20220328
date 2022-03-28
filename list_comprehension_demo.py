fruits = ["apple", "banana", "cherry"]

upper_fruits = [fruit.upper() for fruit in fruits]

print(upper_fruits)

numbers = [1, 2, 5, 6, 8, 3, 7]

filtered = [number for number in numbers if number % 2 == 0]
print(filtered)

filtered = [number**2 for number in numbers if number % 2 == 0]
print(filtered)

print(numbers)
