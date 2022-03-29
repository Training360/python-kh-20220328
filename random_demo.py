import numbers
from random import choices, randint, random, randrange, shuffle
from secrets import choice


print(randint(0, 10)) # [0, 10]
print(randrange(0, 10)) # [0, 10)
print(random()) # [0, 1.0)

names = ["Jack", "Jane", "Joe", "John"]

print(choice(names))
print(choices(names, k=2))

shuffle(names)
print(names)

# Írjatok egy olyan függvényt, ami a 5-ös lottó húzást szimulálja.
# 90-ből kell 5 számot kihúzni. Nem lehet ismétlés!

# Void függvény
def print_name() -> None:
    print("Hello Void")

name = print_name()
print(name)

def generate_lotto_numbers():
    return choices(range(1, 91), k=5)

def generate_lotto_numbers1():
    #numbers = list(range(1, 91))
    numbers = [i for i in range(1, 91)]
    shuffle(numbers)
    return numbers[:5]

print(generate_lotto_numbers1())