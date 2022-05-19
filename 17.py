# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    end = len(arr)
    start = -1
    sums = []
    sums.append(sum(arr))
    for i in range(len(arr)):
        print('start = ' + str(start), 'end = ' + str(end), 'sum_up_end = ' + str(sum(arr[start:end - 1])), 'sum_down_end = ' + str(sum(arr[start + 1:end])))
        sum_up_end = sum(arr[start:end - 1])
        sum_down_end = sum(arr[start + 1:end])
        if sum_up_end < sum_down_end:
            print("start up")
            start += 1
            sums.append(sum_down_end)
        else:
            print("end down")
            end -= 1
            sums.append(sum_up_end)

    return max(sums)

import codewars_test as test

@test.describe("in_array")
def tests():
    test.describe("Tests")
    test.it('should work on an empty array')
    # test.assert_equals(max_sequence([]), 0)
    # test.it('should work on the example')
    # test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
    test.assert_equals(max_sequence([-14, 13, 19, -2, -30, -18, 19, 21, -14, 11, 14, 19, 0, -1, 7, 18, -5, 5, -27, 17, 3, -24, -8, 2, 24, -23, -9, 27, -19, 16, 29, -15, -23, 24, -4, 0, -26, 5, -29, -11, -5, -25, -18, 13, 15, 30, 25, 0, 14, 2]), 102)
