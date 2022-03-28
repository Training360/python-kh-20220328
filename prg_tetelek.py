# Programozási tételek

# Hozzatok létre egy sum függvényt, ami paraméterül egész számok listáját kapja,
# és összegzi ezeket, és az összeggel tér vissza!

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