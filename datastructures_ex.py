def find_all_occurrences(text, sub):
    result = []
    i = 0
    while i < len(text) - len(sub) + 1:
        if text[i:i + len(sub)] == sub:
            result.append(i)
            i += len(sub)
        else:
            i += 1
    return result

# Írj egy függvényt, ami paraméterül kap egy listát, és visszaad egy
# új listát, az eredeti lista minden második elemével!

def every_second(elements):
    return elements[::2]

# Írj egy olyan függvényt, ami kicseréli egy stringben az
# ékezetes karaktert a neki megfelelő nem ékezetes párjára.
# árvíztűrő -> arvizturo

def replace_spec_chars(text):
    chars = "áéíÁÉÍ"
    pairs = "aeiAEI"
    result = ""
    for c in text:
        if c in chars:
            result += pairs[chars.index(c)]
        else:
            result += c
    return result

# Írj egy olyan függvényt, ami a felhasználótól kér be egész számokat,
# amíg nullát nem ír be. És utána adja vissza ezeket egy listába!


def read_numbers():
    result = []
    number = -1
    while number != 0:
        value = input("Adj meg egy számot!")
        # try:            
        #     number = int(value)
        # except ValueError:
        #     print(f"Nem számot adtál meg: {value}")
        # else:            
        #     if number != 0:
        #         result.append(number)
        if value.isnumeric():
            number = int(value)
            if number != 0:
                result.append(number)
        else:
            print("Ez nem szám!")
    return result


if __name__ == "__main__":
    numbers = read_numbers()
    print(numbers)
