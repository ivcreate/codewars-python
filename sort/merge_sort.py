def merge(left, right):
    result = [0] * (len(left) + len(right))
    i = k = n = 0

    while i < len(left) and k < len(right):
        if left[i] <= right[k]:
            result[n] = left[i]
            i += 1
        else:
            result[n] = right[k]
            k += 1
        n += 1

    while i < len(left):
        result[n] = left[i]
        i += 1
        n += 1

    while k < len(right):
        result[n] = right[k]
        k += 1
        n += 1

    return  result


def merge_sort(arr):
    if len(arr) <= 1:
        return

    middle = len(arr) // 2

    left = arr[:middle]
    right = arr[middle:]

    merge_sort(left)
    merge_sort(right)

    merging_arr = merge(left, right)

    for i in range(len(arr)):
        arr[i] = merging_arr[i]



def tests():
    arr = [5, 3, 2, 4, 1]
    print("test #1: ", end="")
    merge_sort(arr)
    if arr == [1, 2, 3, 4, 5]:
        print("OK")
    else:
        print("Fail")

    arr = [4, 4, 4, 4, 4, 5, 5, 3, 3, 2, 2, 2, 1, 1, 2, 3, 4]
    print("test #2: ", end="")
    merge_sort(arr)
    if arr == [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5]:
        print("OK")
    else:
        print("Fail")

tests()