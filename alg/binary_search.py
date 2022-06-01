def left_bount(arr, key):
    left = -1
    right = len(arr)

    while right - left > 1:
        middle = (right + left) // 2

        if arr[middle] < key:
            left = middle
        else:
            right = middle

    return left

def right_bount(arr, key):
    left = -1
    right = len(arr)

    while right - left > 1:
        middle = (right + left) // 2

        if arr[middle] <= key:
            left = middle
        else:
            right = middle

    return right

def binary_search(arr, key):
    return left_bount(arr, key), right_bount(arr, key)

def test():
    arr = [1,1,1,1,2,2,2,2,3,3,3,4,5,6,7,8,8,8,8,9,9,9,10]
    left, right = binary_search(arr, 1)
    arr.index(8)
    print("First case ", end='')

    if left == -1 and right == 4:
        print("OK")
    else:
        print("FALSE")

    left, right = binary_search(arr, 8)

    print("Second case ", end='')

    if left == 14 and right == 19:
        print("OK")
    else:
        print("FALSE")

test()