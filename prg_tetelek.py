# Programozási tételek

# Hozzatok létre egy sum függvényt, ami paraméterül egész számok listáját
# kapja, és összegzi ezeket, és az összeggel tér vissza!

# Összegzés tétele

def sum_numbers(numbers):
    """Összeadja a listában szereplő számokat"""
    result = 0
    for number in numbers:
        result += number
    return result

# Számlálás tétele
# Írjatok egy olyan függvényt, ami paraméterül kap
# egy stringet, és visszaadja, hogy hány magyar ékezetes
# karakter van benne!


def count_accented(text):
    counter = 0
    for c in text.lower():
        if c in "áéíóöőúüű":
            counter += 1
    return counter

# Szélsőérték keresés tétele
# Írj egy függvényt, ami visszaadja a leghosszabb szót
# a paraméterként átadott szövegből. A szövegben
# a szavakat space-ek választják el egymástól.

# "indulnak a kutyák és a tyúk" -> "indulnak"


def find_longest_word(text):
    if text == "":
        return ""
    max_length = 0
    for word in text.split():
        actual_length = len(word)
        if actual_length > max_length:
            max_length = actual_length
            result = word
    return result

# Eldöntés tétele
# Írj egy függvényt, mely egy listáról eldönti, hogy csak
# pozitív számokat tartalmaz-e! Ha egy 0 vagy negatív szám
# is van benne, térjen vissza False értékkel!


def contains_only_positives(numbers: list[int]) -> bool:
    for number in numbers:
        if number <= 0:
            return False
    return True

# Szűrés
# Írjatok egy olyan függvényt, ami paraméterül kap neveket listában,
# és csak a "j" betűvel kezdődő neveket adja vissza.


def filter_names_starts_with(names: list[str]) -> list[str]:
    # result = []
    # for name in names:
    #     if name.lower().startswith("j"):
    #         result.append(name)
    # return result

    return [name for name in names if starts_with_j(name)]


def starts_with_j(text):
    return text.lower().startswith("j")

# Transzformáció
# Írjatok egy olyan függvényt, mely paraméterül kap
# számok listáját, és visszaad egy listát a számok
# abszolútértékével!
# [1, 2, -3, 4, -5] -> [1, 2, 3, 4, 5]


def transform_absolute(numbers: list[int]) -> list[int]:
    # result = []
    # for number in numbers:
    #     result.append(abs(number))
    # return result
    return [abs(number) for number in numbers]


def abs(number):
    if number < 0:
        return -number
    else:
        return number

# print("hello modul")
# print(f"a __name__ valtozo erteke: {__name__}")


if __name__ == "__main__":
    numbers = [1, 3, 2, 3, 2, 1]
    print(sum_numbers(numbers))

# Konvenciók
# snake case name_of_employee
# csak akkor használjatok rövidítést, ha triviális
# óvakodjunk a Hungarian notation numbers, NE: list_of_numbers
# magyar vagy angol? mindegy!
