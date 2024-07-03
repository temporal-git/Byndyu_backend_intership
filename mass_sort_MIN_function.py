def sum_of_two_min_elements(arr):
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
