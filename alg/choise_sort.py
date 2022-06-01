def choise_sort(arr):
    for i in range(len(arr) - 1):
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[i]:
                arr[i], arr[k] = arr[k], arr[i]

    return arr


def tests():
    arr = [5, 3, 2, 4, 1]
    print("test #1: ", end="")
    if choise_sort(arr) == [1, 2, 3, 4, 5]:
        print("OK")
    else:
        print("Fail")

    arr = [4, 4, 4, 4, 4, 5, 5, 3, 3, 2, 2, 2, 1, 1, 2, 3, 4]
    print("test #2: ", end="")
    if choise_sort(arr) == [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5]:
        print("OK")
    else:
        print("Fail")


tests()
