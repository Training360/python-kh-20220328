names = ("John", "Jack", "Jane")  # tuple - NEM MÓDOSÍTHATÓ
# Veszélyes!
employee = ("John", 1980)

print(names[1])
#names[1] = "Joe" # TypeError 
numbers_tuple = (1, 2, 3) 
numbers = list(numbers_tuple)
numbers[1] = 5
print(numbers)

numbers_ro = tuple(numbers)
#numbers_ro[1] = 5

employee = ("John Doe", 1980, ("Java", "Python", ("JavaScript 2", "JavaScript 3")))

matrix = ([1, 2], [3, 4])
#matrix[0] = [11, 11]
matrix[0][0] = 11
print(matrix)

colors: tuple = ("red", "green", "blue")
for color in colors:
    print(color)


def find_max_min(numbers):
    max = numbers[0]
    min = numbers[0]
    for number in numbers:
        if number > max:
            max = number
        if number < min:
            min = number
    return (min, max)

print(find_max_min((1, 2, 3, 4, 3, 1, 2, 1)))
valid = ("01-01", "01-05")
valid = ("02-01", "02-05")