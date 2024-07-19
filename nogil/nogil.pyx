import cython
from libc.math cimport INFINITY

cpdef double sum_of_two_min_elements_min(double[:] arr, int n) nogil:
    cdef int i
    cdef double min1, min2

    if n < 2:
        return INFINITY  # Используем INFINITY для указания ошибки

    min1 = INFINITY
    min2 = INFINITY

    for i in range(n):
        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    return min1 + min2
