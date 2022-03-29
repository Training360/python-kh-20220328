
def a():
    x = "x"
    try:
        int(x)
    except ValueError as e:
        print(f"Hiba {e}")

def b():
    y = "y"
    a()


def c():
    z = "z"
    b()    


print("Start")
c()
print("End")

try:
    print(55 / 0) # ZeroDivisionError
except ZeroDivisionError:
    print("Nullával nem osztunk")

numbers = [1, 2, 3]
try:
    print(numbers[3])
except IndexError:
    print("Rosszul indexelsz!")

# import alma

try:
    "almakorte".index("x")
except ValueError:
    print("Az x nincs benne a szóban")