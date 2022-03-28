from prg_tetelek import count_accented, sum_numbers

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