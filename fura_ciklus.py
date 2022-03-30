madarak = (("cinke", "barna"), ("golya", "feher"), ("varju", "fekete"))

for madar, szin in madarak:
    print(madar)
    # print(szin)

madarak = (("cinke",), ("golya",), ("varju",))

for madar, in madarak:
    print(madar)
    print(type(madar))
    # print(szin)

print(("alma",))

number = (6,)
print(type(number))