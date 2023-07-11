def selection_sort(array: list) -> list:
    try:
        array = list(array)
    except TypeError:
        raise TypeError("Array is not a list and can't be casted to list")
    try:
        for i in range(len(array)):
            min_index = array.index(min(array[i:]))
            array[i], array[min_index] = array[min_index], array[i]
    except TypeError:
        raise TypeError("The types are incomparable")
    return array


list1 = [8, 9, 6, 8, 2, 1, 4, 3, 10, 56, 5]

try:
    print(selection_sort(list1))
except TypeError as te:
    print(str(te))
