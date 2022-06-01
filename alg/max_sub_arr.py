def max_sub_arr(arr, arr2):
    res = [[0] * (len(arr2) + 1) for n in range(len(arr) + 1)]
    for i in range(1, len(arr) + 1):
        for j in range(1, len(arr2) + 1):
            if arr[i-1] == arr2[j-1]:
                res[i][j] = 1 + res[i-1][j-1]
            else:
                res[i][j] = max(res[i-1][j],res[i][j-1])
    return res[-1][-1]


def tests():
    arr = [5, 3, 2, 4, 1]
    arr2 = [5, 3, 2, 4, 1,4,5,67,8]
    print("test #1: ", end="")
    if max_sub_arr(arr,arr2) == 5:
        print("OK")
    else:
        print("Fail")

    arr = [5, 3, 2, 4, 1]
    arr2 = [5, 3, 2, 4, 1]
    print("test #2: ", end="")
    if max_sub_arr(arr,arr2) == 5:
        print("OK")
    else:
        print("Fail")

    arr = [5, 3, 2, 4, 1]
    arr2 = [1,20,33,42,64,75,65,4]
    print("test #2: ", end="")
    if max_sub_arr(arr,arr2) == 1:
        print("OK")
    else:
        print("Fail")

tests()