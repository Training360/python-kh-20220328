def is_invalid_input(text: str):
    return not text.isnumeric()


value = "abc"
if is_invalid_input(value):
    print("Ez nem szám")

def is_even(number):
    return number % 2 == 0

if is_even(number):
    print("Paros")