import pytest
from mass_sort_MIN_function import sum_of_two_min_elements


class TestSumOfTwoMinElements:
    # позитивные проверки с целыми числами
    @pytest.mark.parametrize('array', [[4, 0, 3, 19, 492, -10, 1],
                                       [0, 3, 19, 492, -10],
                                       [-5, -5, -5, -5, -5],
                                       [-4, -6],
                                       [-10, 3, 3, 3, 3, 0]])
    def test_valid_int_input(self, array):
        arr = array
        assert sum_of_two_min_elements(arr) == -10

    # позитивные проверки с числами с плавающей точкой
    @pytest.mark.parametrize('array', [[4.0, 0.0, 3.0, 19.0, 492.0, -10.0, 1.0], [4, 0.0, 3, 19.0, 492, -10, 1]])
    def test_valid_float_input(self, array):
        arr = array
        result = sum_of_two_min_elements(arr)
        assert result == -10.0 and isinstance(result, float)

    # негативные проверки, что массив должен содержать только числовые элементы
    @pytest.mark.parametrize('array', [[4, 0, "b", 19, 492.0, -10, 1], ["z", "b", "c"], [4, "0"]])
    def test_non_numeric_elements(self, array):
        arr = array
        assert sum_of_two_min_elements(arr) == "Массив должен содержать только числовые элементы"

    # негативные проверки, что массив одержать хотя бы два элемента
    @pytest.mark.parametrize('array', [["4"], []])
    def test_insufficient_elements(self, array):
        arr = array
        assert sum_of_two_min_elements(arr) == "Массив должен содержать хотя бы два элемента"