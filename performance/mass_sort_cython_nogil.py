import time
from nogil import nogil as ng
import numpy as np


def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        result = function(*args)
        end_time = time.time()
        func_time = end_time - start_time
        return result, f'Time: {func_time}'
    return wrapped


def open_list(option: str = "1m"):
    global arr
    load_start = time.time()
    # importing 1 million lines file with digits. "gen_arr_1m.txt" for 1 mil or "gen_arr_100m.txt"
    if option == "1m":
        with open('../data/gen_arr_1m.txt', 'r') as file:
            arr = [int(x) for x in file.read().splitlines()]

    elif option == "100m":
        with open('../data/gen_arr_100m.txt', 'r') as file:
            arr = [int(x) for x in file.read().splitlines()]

    # importing mixed int + float numbers
    elif option == "mixed":
        with open('../data/int_float_array.txt', 'r') as file:
            arr = []
            for line in file:
                line = line.strip()
                if '.' in line:
                    arr.append(float(line))
                else:
                    arr.append(int(line))
    load_end = time.time()
    load_time = load_end - load_start
    print(f'Load file time: {load_time} \n')
    return arr


# Options for choosing file length : "1m", "100m", "mixed"
open_list("1m")
decorated_cython_nogil = time_of_function(ng.sum_of_two_min_elements_min)
arr = np.array(arr, dtype=np.float64)

print(f'Result Cython MIN: {decorated_cython_nogil(arr, len(arr))}')

result = ng.sum_of_two_min_elements_min(arr, len(arr))
if result == float('inf'):
    print("Массив должен содержать хотя бы два элемента")
else:
    print(f"Сумма двух минимальных элементов: {result}")
