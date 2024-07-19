from lowlevel import mass_sort_cython as msc
import time

with open('../../data/gen_arr_1m.txt', 'r') as file:
    digi_list = [int(x) for x in file.read().splitlines()]


def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        result = function(*args)
        end_time = time.time()
        func_time = end_time - start_time
        print(f'Time: {func_time}')
        return result
    return wrapped


decorated_cython_min = time_of_function(msc.sum_of_two_min_elements_min)
decorated_cython_for = time_of_function(msc.sum_of_two_min_elements_for)
print(f'Result: {decorated_cython_min(digi_list)}')
print(f'Result: {decorated_cython_for(digi_list)}')
