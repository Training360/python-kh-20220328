def mod_names(names):
    names[1] = "JackXXX"


employees = ["John", "Jack", "Jane"]
mod_names(employees)
print(employees)

# ---


def mod_name(name):
    name = "John Doe"


employee = "Jack Doe"
mod_name(employee)
print(employee)


# ---

def remove_last(names: list):
    #names = names[0:-1]
    #names.remove(names[-1])
    #names = [name for name in names if name.startswith("J")]
    for name in names:
        if name.startswith("S"):
            names.remove(name)


employees = ["Jonh", "Jack", "Jane", "Steve"]
remove_last(employees)
print(employees)

