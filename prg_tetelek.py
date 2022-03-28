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