import cython

cpdef sum_of_two_min_elements_min(arr):
    if len(arr) < 2:
        return "Массив должен содержать хотя бы два элемента"
    else:
        for i in arr:
            if not isinstance(i, (int, float)):
                return "Массив должен содержать только числовые элементы"

        min1 = min(arr)
        arr.remove(min1)
        min2 = min(arr)
        return min1 + min2


cpdef sum_of_two_min_elements_for(arr):
    if len(arr) < 2:
        return "Массив должен содержать хотя бы два элемента"
    else:
        for i in arr:
            if not isinstance(i, (int, float)):
                return "Массив должен содержать только числовые элементы"

        if arr[0] < arr[1]:
            min1 = arr[0]
            min2 = arr[1]
        else:
             min1 = arr[1]
             min2 = arr[0]

        for num in arr[2:]:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return min1 + min2
