from random import shuffle


print("fúró" in "árvíztűrőtökörfúrógép")
print(5 in [1, 2, 4, 5, 6])

print("árvíztűrőtökörfúrógép".index("fúró"))
print("árvíztűrőtökörfúrógép".find("fúró"))

# print("árvíztűrőtökörfúrógép".index("xx")) # ValueError
print("árvíztűrőtökörfúrógép".find("xxx")) # -1

print("xyxyxyx".count("x"))

print([1, 2, 3].index(2))
# print([1, 2, 3].index(6)) # ValueError

print("almaalmaalma".find("a", 2))

# Írj egy olyan függvényt, ami egy stringben megkeresi egy substring
# összes előfordulását! És visszaadja a pozíciókat egy listában.
# "almaalmaalma", "alma" -> [0, 4, 8]
# Nem érdekelnek az átlapoló találatok!

# Írjatok tesztesetet AHOL:
#  egyszer van benne
#  kétszer van benne
#  átlapova van benne
#  nincs benne
#  a keresett szó hosszabb, mint amiben keresünk!

numbers = [65, 3, 23, 2, 1, 5, 3]

print(sorted(numbers))
print(numbers)
print("***")
numbers.sort()
print(numbers)
