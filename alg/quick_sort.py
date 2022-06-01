def quick_sort(arr):
    if len(arr) <= 1:
        return

    barrier = arr[0]

    left = []
    right = []
    middle = []

    for x in arr:
        if x < barrier:
            left.append(x)
        elif x == barrier:
            middle.append(x)
        else:
            right.append(x)

    quick_sort(left)
    quick_sort(right)

    k = 0
    for x in left + middle + right:
        arr[k] = x
        k += 1




def tests():
    arr = [5, 3, 2, 4, 1]
    print("test #1: ", end="")
    quick_sort(arr)
    if arr == [1, 2, 3, 4, 5]:
        print("OK")
    else:
        print("Fail")

    arr = [4, 4, 4, 4, 4, 5, 5, 3, 3, 2, 2, 2, 1, 1, 2, 3, 4]
    print("test #2: ", end="")
    quick_sort(arr)
    if arr == [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5]:
        print("OK")
    else:
        print("Fail")

tests()