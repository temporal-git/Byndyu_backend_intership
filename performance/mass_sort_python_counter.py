import time

# importing list of variables from .py file with 1000 units, can be easy added non digit symbols
# from data.py_arr import digi_list

# code bellow for importing 100 million lines file with digits. "gen_arr_1m.txt" for 1 mil or "gen_arr_100m.txt"
with open('../data/gen_arr_1m.txt', 'r') as file:
    digi_list = [int(x) for x in file.read().splitlines()]


# importing mixed int + float numbers
# with open('../data/int_float_array.txt', 'r') as file:
#     digi_list = []
#     for line in file:
#         line = line.strip()
#         if '.' in line:
#             digi_list.append(float(line))
#         else:
#             digi_list.append(int(line))


def sum_of_two_min_elements_1(arr):
    if len(arr) < 2:
        return "Массив должен содержать хотя бы два элемента"
    else:
        if not all(isinstance(e, (int, float)) for e in arr):
            return "Массив должен содержать только числовые элементы"
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


def sum_of_two_min_elements_2(arr):
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


start = time.time()
print(sum_of_two_min_elements_1(digi_list))
end = time.time()
cy_time = end - start

start2 = time.time()
print(sum_of_two_min_elements_2(digi_list))
end2 = time.time()
cy_time2 = end2 - start2

print(cy_time)
print(cy_time2)
