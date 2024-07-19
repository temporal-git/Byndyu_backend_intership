import time
import mass_sort_FOR_cycle as msfc
import mass_sort_MIN_function as msmf
from lowlevel import mass_sort_cython as msc

load_start = time.time()
# importing list of variables from .py file with 1000 units, can be easy added non digit symbols
# from data.py_arr import digi_list

# importing mixed int + float numbers
# with open('../data/int_float_array.txt', 'r') as file:
#     digi_list = []
#     for line in file:
#         line = line.strip()
#         if '.' in line:
#             digi_list.append(float(line))
#         else:
#             digi_list.append(int(line))

# code bellow for importing 100 million lines file with digits. "gen_arr_1m.txt" for 1 mil or "gen_arr_100m.txt"


with open('../data/gen_arr_100m.txt', 'r') as file:
    digi_list = [int(x) for x in file.read().splitlines()]

load_end = time.time()
load_time = load_end - load_start
print(f'Load file time: {load_time} \n')


def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        result = function(*args)
        end_time = time.time()
        func_time = end_time - start_time
        # print(f'Time: {func_time}')
        return result, f'Time: {func_time}'
    return wrapped


decorated_python_for = time_of_function(msfc.sum_of_two_min_elements_for)
decorated_python_min = time_of_function(msmf.sum_of_two_min_elements_min)
decorated_cython_for = time_of_function(msc.sum_of_two_min_elements_for)
decorated_cython_min = time_of_function(msc.sum_of_two_min_elements_min)

print(f'Result Python FOR: {decorated_python_for(digi_list)}')
print(f'Result Python MIN: {decorated_python_min(digi_list)}')
print(f'Result Cython FOR: {decorated_cython_for(digi_list)}')
print(f'Result Cython MIN: {decorated_cython_min(digi_list)}')
