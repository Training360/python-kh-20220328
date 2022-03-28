names = ["Jane", "Jack", "John"]

# employees = names

# print(employees)

# names[1] = "JackXXX"

# print(employees)

# employees[2] = "JohnXXX"

# print(names)

# employees = names.copy()
employees = names
names[1] = "JackXXX"
print(employees)

print(id(names))
print(id(employees))
