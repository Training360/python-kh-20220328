def calculate_age(year_of_birth, actual_year):
    if year_of_birth < 1900:
        raise ValueError(f"Hibas szuletesi ev: {year_of_birth}, 1900-nal nagyobbnak kene lennie")
    if actual_year < 1900:
        raise ValueError(f"Hibas aktualis ev: {actual_year}, 1900-nal nagyobbnak kene lennie")
    if year_of_birth > actual_year:
        raise ValueError(f"A szuletesi ev nem lehet kisebb, mint az aktualis ev {year_of_birth} > {actual_year}")
    return actual_year - year_of_birth


print(calculate_age(1980, 2022))
# print(calculate_age(-5, -21))
#print(calculate_age(1980, -21))
try:
    print(calculate_age(1980, 1902))
except ValueError as e:
    print(e)
