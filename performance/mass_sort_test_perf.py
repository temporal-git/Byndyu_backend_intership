import time
import mass_sort_FOR_cycle as msfc
import mass_sort_MIN_function as msmf
from lowlevel import mass_sort_cython as msc
from data.py_arr import digi_list


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

    # importing list of variables from .py file with 1000 units, can be easy added non digit symbols
    elif option == "1000":
        arr = digi_list
    load_end = time.time()
    load_time = load_end - load_start
    print(f'Load file time: {load_time} \n')

    return arr


# Options for choosing file length : "1m", "100m", "1000", "mixed"
arr = open_list("1m")

decorated_python_for = time_of_function(msfc.sum_of_two_min_elements_for)
decorated_python_min = time_of_function(msmf.sum_of_two_min_elements_min)
decorated_cython_for = time_of_function(msc.sum_of_two_min_elements_for)
decorated_cython_min = time_of_function(msc.sum_of_two_min_elements_min)

print(f'Result Python FOR: {decorated_python_for(arr)}')
print(f'Result Python MIN: {decorated_python_min(arr)}')
print(f'Result Cython FOR: {decorated_cython_for(arr)}')
print(f'Result Cython MIN: {decorated_cython_min(arr)}')
