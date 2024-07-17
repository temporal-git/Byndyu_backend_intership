from lowlevel import mass_sort_cython
import time


with open('../data/gen_arr_100m.txt', 'r') as file:
    digi_list = [int(x) for x in file.read().splitlines()]

start = time.time()
print(mass_sort_cython.sum_of_two_min_elements_min(digi_list))
end = time.time()
cy_time = end - start

start2 = time.time()
print(mass_sort_cython.sum_of_two_min_elements_for(digi_list))
end2 = time.time()
cy_time2 = end2 - start2


print(cy_time)
print(cy_time2)
