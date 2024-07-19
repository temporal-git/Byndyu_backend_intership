import pytest
from nogil import nogil as ng
import numpy as np


class TestSumOfTwoMinElementsCythonNogil:
    # позитивные проверки с целыми числами
    @pytest.mark.parametrize('array', [[4, 0, 3, 19, 492, -10, 1],
                                       [0, 3, 19, 492, -10],
                                       [-5, -5, -5, -5, -5],
                                       [-4, -6],
                                       [-10, 3, 3, 3, 3, 0]])
    def test_valid_int_input(self, array):
        arr = np.array(array, dtype=np.float64)
        assert ng.sum_of_two_min_elements_min(arr, len(arr)) == -10

    # позитивные проверки с числами с плавающей точкой
    @pytest.mark.parametrize('array', [[4.2, 0.0, 3.6, 19.0, 492.0, -10.0, 1.0], [4, 0.0, 3, 19.0, 492, -10, 1]])
    def test_valid_float_input(self, array):
        arr = np.array(array, dtype=np.float64)
        result = ng.sum_of_two_min_elements_min(arr, len(arr))
        assert result == -10.0 and isinstance(result, float)

    # # негативные проверки, что массив должен содержать только числовые элементы
    # нет проверки на литералы для nogil кода
    # @pytest.mark.parametrize('array', [[4, 0, "b", 19, 492, -10, 1], ["z", "b", "c"], [4, "0"]])
    # def test_non_numeric_elements(self, array):
    #     arr = np.array(array, dtype=np.float64)
    #     assert ng.sum_of_two_min_elements_min(arr, len(arr)) == "Массив должен содержать только числовые элементы"

    # негативные проверки, что массив одержать хотя бы два элемента
    @pytest.mark.parametrize('array', [["4"], []])
    def test_insufficient_elements(self, array):
        arr = np.array(array, dtype=np.float64)
        assert ng.sum_of_two_min_elements_min(arr, len(arr)) == float('inf')
