import pytest
from data.py_arr import digi_list


def sum_of_two_min_elements(arr):
    if len(arr) < 2:
        return "Массив должен содержать хотя бы два элемента"
    else:
        if not all(isinstance(e, (int, float)) for e in arr):
            return "Массив должен содержать только числовые элементы"
        else:
            min1 = min(arr)
            arr.remove(min1)
            min2 = min(arr)
    return min1 + min2


class TestSumOfTwoMinElements:
    def test_valid_int_input(self):
        arr = [4, 0, 3, 19, 492, -10, 1]
        assert sum_of_two_min_elements(arr) == -10

    def test_valid_float_input(self):
        arr = [4.0, 0.0, 3.0, 19.0, 492.0, -10.0, 1.0]
        assert sum_of_two_min_elements(arr) == -10.0

    def test_valid_mixed_input(self):
        arr = [4, 0.0, 3, 19.0, 492, -10, 1]
        assert sum_of_two_min_elements(arr) == -10.0

    @pytest.mark.parametrize('array', [[4, 0, "b", 19, 492.0, -10, 1], ["z", "b", "c"], [4, "0"]])
    def test_non_numeric_elements(self, array):
        arr = array
        assert sum_of_two_min_elements(arr) == "Массив должен содержать только числовые элементы"

    @pytest.mark.parametrize('array', [["4"], []])
    def test_insufficient_elements(self, array):
        arr = array
        assert sum_of_two_min_elements(arr) == "Массив должен содержать хотя бы два элемента"


print(sum_of_two_min_elements(digi_list))
