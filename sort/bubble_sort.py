def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for k in range(1, len(arr)):
            if arr[k] < arr[k - 1]:
                arr[k - 1], arr[k] = arr[k], arr[k - 1]

    return arr


def tests():
    arr = [5, 3, 2, 4, 1]
    print("test #1: ", end="")
    if bubble_sort(arr) == [1, 2, 3, 4, 5]:
        print("OK")
    else:
        print("Fail")

    arr = [4, 4, 4, 4, 4, 5, 5, 3, 3, 2, 2, 2, 1, 1, 2, 3, 4]
    print("test #2: ", end="")
    if bubble_sort(arr) == [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5]:
        print("OK")
    else:
        print("Fail")


tests()
