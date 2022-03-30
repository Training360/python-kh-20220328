# Set
# Adatszerkezet = több értéket tartalmaz
# Egy érték csak egyszer szerepelhet a setben
# Elemek között nincs sorrend

numbers = {2, 3, 6, 8}
numbers.add(9)
print(numbers)
numbers.add(2)
print(numbers)
print(len(numbers))
for i in numbers:
    print(i)
numbers.remove(3)
print(numbers)

words = ["xxx", "yyy", "zzz", "xxx"]
print(words)
words_set = set(words)
print(words_set)

print("xxx" in words_set)

# Hány különböző betű van egy szóban?
print(len(set("aabbbcc")))

letters1 = set("abcefg")
print(letters1)
letters2 = set("efgxyz")
print(letters2)

print(letters1.union(letters2))
print(letters1 | letters2)

print(letters1.intersection(letters2))
print(letters1 & letters2)

print(letters1.difference(letters2))
print(letters1 - letters2)

print(set("bc").issubset(letters1))
print(set("bc") < letters1)

colors = frozenset({"green", "black", "yellow"})
print(colors)
