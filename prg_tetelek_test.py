from prg_tetelek import contains_only_positives, count_accented, filter_names_starts_with, find_longest_word, sum_numbers, transform_absolute

# teszteset == teszt függvény


def test_sum():
    # given
    numbers = [1, 3, 2, 3, 2, 1] # input
    # when
    result = sum_numbers(numbers)
    # then
    # összehasonlítjuk az elvárt értéket a kapott értékkel
    assert result == 12 # output

def test_sum_short():
    assert sum_numbers([1, 3, 2, 3, 2, 1]) == 12

def test_count_accented():
    assert count_accented("árvíztűrőtükörfúrógép") == 9

def test_find_longest_word():
    assert find_longest_word("indulnak a kutyák és a tyúk") == "indulnak"

def test_find_longest_word_with_empty_string():
    assert find_longest_word("") == ""

def test_find_longest_word_with_one_word():
    assert find_longest_word("alma") == "alma"

def test_contains_only_positive():
    assert contains_only_positives([1, 2, 3]) == True

def test_contains_only_positive_with_zero():
    assert contains_only_positives([1, 0, 3]) == False

def test_contains_only_positive_negative():
    assert contains_only_positives([1, -2, 3]) == False

def test_filter_names_starts_with():
    assert filter_names_starts_with(["Jack", "Steven", "Joe"]) == ["Jack", "Joe"]

def test_transform_absolute():
    assert transform_absolute([1, 2, -3, 4, -5]) == [1, 2, 3, 4, 5]