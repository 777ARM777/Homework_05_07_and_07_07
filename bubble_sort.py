def bubble_sort(array: list) -> list:
    try:
        array = list(array)
    except TypeError:
        raise TypeError("Array is not a list and can't be casted to list")

    is_sorted = False
    for i in range(len(array)):
        if is_sorted:
            break
        try:
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    is_sorted = False
        except TypeError:
            raise TypeError("The types are incomparable")

    return array


list1 = [8, 9, 6, 8, 2, 1, 4, 3, 56, 5]
try:
    print(bubble_sort(list1))
except TypeError as te:
    print(str(te))


