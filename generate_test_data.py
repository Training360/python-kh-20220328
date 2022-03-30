# Írjatok egy olyan függvényt, ami
# alkalmazottak listáját adja vissza!
# Egy alkalmazott egy tuple legyen!
# Az alkalmazottnak legyen egy neve, és legyen egy életkora!
# Az alkalmazott neve álljon össze úgy, hogy adott egy előnév és
# adott egy utónév tuple, és ezekből kell véletlenszerűen választani.
# Az életkora legyen egy 20 és 90 közötti véletlen szám!
# Lehet ismétlődés!
# Lehessen megadni paraméterül, hogy hány darabot!

from random import randint, Random
from secrets import choice


elonevek = ["Kovács", "Szabó", "Kiss", "Nagy"]
utonevek = ["György", "János", "Máté"]


def generate_employee(id, random=Random()):
    return (id, choice(elonevek) + " " + choice(utonevek), randint(20, 90))


def generate_employees(number=5, random=Random()):
    return [generate_employee(i, random) for i in range(number)]


print(generate_employee(1))
print(generate_employees())
print(generate_employees(10))

generate_employees(random=Random(), number=12)