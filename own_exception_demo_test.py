from own_exeception_demo import calculate_age
import pytest


def test_calculate_age():
    assert calculate_age(1980, 2022) == 42

def test_calculate_age_where_year_of_birth_larger_than_actual_year():
    # try:
    #     calculate_age(1980, 1970)
    #     assert False
    # except ValueError as elkapott_kivetel:        
    #     assert str(elkapott_kivetel) == "A szuletesi ev nem lehet kisebb, mint az aktualis ev 1980 > 1970"

    with pytest.raises(ValueError) as exception_info:
        calculate_age(1980, 1970)
    assert str(exception_info.value) == "A szuletesi ev nem lehet kisebb, mint az aktualis ev 1980 > 1970"