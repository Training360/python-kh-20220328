employee = {"name": "John Doe", "year_of_birth": 1980}
print(employee["name"])
print(employee["year_of_birth"])

employee["favourite_color"] = "red"
print(employee)
employee["favourite_color"] = "blue"
print(employee)
del employee["favourite_color"]
print(employee)

inventory = {"banán": 1, "körte": 2, "meggy": 100}
print(inventory["banán"])

print(len(inventory))

# Lassabb
for i in inventory:
    print(i)
    print(inventory[i])

# Az előző gyorsan
for (k, v) in inventory.items():
    print(f"A '{k}' termékből {v} darab található a raktárban.")

# Hisztogram készítése
def count_numbers(numbers):
    counts = {}
    for number in numbers:
        if number not in counts:
            counts[number] = 1
        else:
            counts[number] += 1
    return counts

result = count_numbers((1, 1, 1, 1, 2, 2))
print(result)
print(result == {1: 4, 2: 2})
print(result == {2: 2, 1: 4})

print(result.keys())
print(result.values())

employee = {"name": "John Doe", "year_of_birth": 1980, "skills": {"Java": 3, "Python": 5}}
print(employee["skills"]["Python"])

person = {"name": "John", "age": 30, "car": None}
print(person["name"])

# Írjatok egy függvényt, amely összeszámolja egy stringben, hogy melyik betű
# hányszor szerepel!

# Bónusz feladat: csak betűket, és ábécésorrendben írd ki egymás alá!
# a: 1
# b: 2

def count_charaters(text):
    counts = {}
    c: str
    for c in text:
        c = c.lower()
        if c.isalpha():
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1
    return counts

result = count_charaters("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam mattis malesuada nibh a posuere.")
print(result)
letters = list(result.keys())
letters.sort()
for letter in letters:
    print(f"{letter}: {result[letter]}")

# tuple unpack
values = ("John Doe", 1985)
name, year_of_birth = values
print(name)
print(year_of_birth)


# built-in function: enumerate()
numbers = [7, 8, 7, 8, 7, 8]
for i in range(0, len(numbers)):
    print(f"{i}: {numbers[i]}")

i = 0
for n in numbers:
    i += 1
    print(f"{i}: {n}")

print(list(enumerate(numbers,start=1)))

for i,n in enumerate(numbers,start=1):
    print(f"{i}: {n}")

doubles = {i: i**2 for i in range(10)}
print(doubles)