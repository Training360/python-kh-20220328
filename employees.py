class Employee:
    
    def __init__(self, name, year_of_birth=1960) -> None:
        self.name = name
        self.year_of_birth = year_of_birth

    def get_age(self, actual_year):
        return actual_year - self.year_of_birth

    def __str__(self) -> str:
        return f"Employee({self.name}, {self.year_of_birth})"


john = Employee("John Doe", 1980)
print(john)
print(john.name)
print(john.year_of_birth)
print(john.get_age(2022))

jack = Employee("Jack Smith", 1970)
print(jack)
print(jack.name)
print(jack.year_of_birth)
print(jack.get_age(2022))

joe = Employee("Joe")
print(joe.year_of_birth)

employees = []
employees.append(john)
employees.append(jack)
employees.append(joe)

sum = 0
for employee in employees:
    sum += employee.get_age(2022)
print(sum / len(employees))

e1 = Employee("Jack Xxx")
del e1