import pytest
from mass_sort_FOR_cycle import sum_of_two_min_elements


class TestSumOfTwoMinElements:
    def test_valid_int_input(self):
        arr = [4, 0, 3, 19, 492, -10, 1]
        result = sum_of_two_min_elements(arr)
        assert result == -10

    def test_valid_float_input(self):
        arr = [-10.0, 3, 3, 3, 3, 0]
        result = sum_of_two_min_elements(arr)
        assert result == -10.0 and isinstance(result, float)

    def test_non_numeric_elements(self):
        arr = [4, 0, 'b', 19, -10, 1]
        with pytest.raises(ValueError, match="Массив должен содержать только числовые элементы"):
            sum_of_two_min_elements(arr)

    def test_insufficient_elements(self):
        arr = [4]
        with pytest.raises(ValueError, match="Массив должен содержать хотя бы два элемента"):
            sum_of_two_min_elements(arr)
