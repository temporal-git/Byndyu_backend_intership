import pytest
from data.py_arr import digi_list


def sum_of_two_min_elements(arr):
    if len(arr) < 2:
        raise ValueError("Массив должен содержать хотя бы два элемента")
    else:
        if not all(isinstance(e, (int, float)) for e in arr):
            raise ValueError("Массив должен содержать только числовые элементы")
        else:
            if arr[0] < arr[1]:
                min1, min2 = arr[0], arr[1]
            else:
                min1, min2 = arr[1], arr[0]

            for num in arr[2:]:
                if num < min1:
                    min2 = min1
                    min1 = num
                elif num < min2:
                    min2 = num
    return min1 + min2


class TestSumOfTwoMinElements:
    def test_valid_input(self):
        arr = [4, 0, 3, 19, 492, -10, 1]
        result = sum_of_two_min_elements(arr)
        assert result == -10

    def test_non_numeric_elements(self):
        arr = [4, 0, 'b', 19, -10, 1]
        with pytest.raises(ValueError, match="Массив должен содержать только числовые элементы"):
            sum_of_two_min_elements(arr)

    def test_insufficient_elements(self):
        arr = [4]
        with pytest.raises(ValueError, match="Массив должен содержать хотя бы два элемента"):
            sum_of_two_min_elements(arr)


print(sum_of_two_min_elements(digi_list))
