class TargetNotFoundException(Exception):
    pass


def binary_search(ls, target):
    try:
        target = float(target)
    except ValueError:
        raise ValueError("Target is not a valid number")

    low = 0
    high = len(ls) - 1
    try:
        while low <= high:
            mid = (low + high) // 2
            if target > ls[mid]:
                low = mid + 1
            elif target < ls[mid]:
                high = mid - 1
            else:
                return mid
        raise TargetNotFoundException("Target not found in the list")

    except Exception:
        raise TargetNotFoundException("Target not found in the list")


list1 = [1, 2, 4, 5, 9, 45, 155]
try:
    print(binary_search(list1, "s"))
except ValueError as ve:
    print(str(ve))
except TargetNotFoundException as tnf:
    print(str(tnf))
