from random import Random, choices


def generate_lotto_numbers(random=Random()):
    numbers = list(range(1, 91))
    random.shuffle(numbers)
    return numbers[:5]


print(generate_lotto_numbers())
print(generate_lotto_numbers(Random(5)))