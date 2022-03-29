from datastructures_ex import find_all_occurrences


def test_normal():
    assert find_all_occurrences("almaalmaalma", "alma") == [0, 4, 8]

def test_overlap():
    assert find_all_occurrences("xxxx", "xx") == [0, 2]

def test_not_found():
    assert find_all_occurrences("almaalmaalma", "xxx") == []

def test_length_problem():
    assert find_all_occurrences("xxx", "almaalma") == []
