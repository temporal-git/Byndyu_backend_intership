import time
import mass_sort_FOR_cycle
import mass_sort_MIN_function
from lowlevel import mass_sort_cython

start0 = time.time()
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

end0 = time.time()
cy_time0 = end0 - start0


start = time.time()
print(f'Result Python FOR: {mass_sort_FOR_cycle.sum_of_two_min_elements_for(digi_list)}')
end = time.time()
cy_time = end - start

start2 = time.time()
print(f'Result Python MIN: {mass_sort_MIN_function.sum_of_two_min_elements_min(digi_list)}')
end2 = time.time()
cy_time2 = end2 - start2

start3 = time.time()
print(f'Result Cython FOR: {mass_sort_cython.sum_of_two_min_elements_for(digi_list)}')
end3 = time.time()
cy_time3 = end3 - start3

start4 = time.time()
print(f'Result Cython MIN: {mass_sort_cython.sum_of_two_min_elements_min(digi_list)} \n')


end4 = time.time()
cy_time4 = end4 - start4

print(f'Load  file time: {cy_time0}')
print(f'Python FOR time: {cy_time}')
print(f'Python MIN time: {cy_time2}')
print(f'Cython FOR time: {cy_time3}')
print(f'Cython MIN time: {cy_time4}')


