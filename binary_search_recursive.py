class TargetNotFoundException(Exception):
    pass


def binary_search_recursive(array, target, low, high):
    try:
        target = float(target)
    except ValueError:
        raise ValueError("Target is not a valid number")

    try:
        if low > high:
            raise TargetNotFoundException("Target not found in the list")
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search_recursive(array, target, low, mid - 1)
        else:
            return binary_search_recursive(array, target, mid + 1, high)
    except Exception:
        raise TargetNotFoundException("Target not found in the list")


list1 = [1, 2, 4, 5, 9, 45, 155]

try:
    print(binary_search_recursive(list1, "S", 0, len(list1) - 1))
except ValueError as ve:
    print(str(ve))
except TargetNotFoundException as tnf:
    print(str(tnf))
