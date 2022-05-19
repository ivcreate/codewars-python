def insert_sort(arr):
    for i in range(1, len(arr)):
        k = i
        while k > 0 and arr[k - 1] > arr[k]:
            arr[k - 1], arr[k] = arr[k], arr[k - 1]
            k -= 1

    return arr


def tests():
    arr = [5, 3, 2, 4, 1]
    print("test #1: ", end="")
    if insert_sort(arr) == [1, 2, 3, 4, 5]:
        print("OK")
    else:
        print("Fail")

    arr = [4, 4, 4, 4, 4, 5, 5, 3, 3, 2, 2, 2, 1, 1, 2, 3, 4]
    print("test #2: ", end="")
    if insert_sort(arr) == [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5]:
        print("OK")
    else:
        print("Fail")

tests()