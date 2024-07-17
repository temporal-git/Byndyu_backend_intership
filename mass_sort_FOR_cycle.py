def sum_of_two_min_elements_for(arr):
    if len(arr) < 2:
        return "Массив должен содержать хотя бы два элемента"
    else:
        if not all(isinstance(e, (int, float)) for e in arr):
            return "Массив должен содержать только числовые элементы"
        else:
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
