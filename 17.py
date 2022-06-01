# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
#
# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# # should be 6: [4, -1, 2, 1]
# Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
#
# Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.

def max_sequence(arr):
    max_sum = sum(arr)

    for start in range(len(arr) + 1):
        for end in range(len(arr) + 1):
            check_sum = sum(arr[start:end])
            if check_sum > max_sum:
                max_sum = check_sum

    return max_sum

import codewars_test as test

@test.describe("in_array")
def tests():
    test.describe("Tests")
    test.it('should work on an empty array')
    test.assert_equals(max_sequence([]), 0)
    test.it('should work on the example')
    test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
    test.assert_equals(max_sequence([-14, 13, 19, -2, -30, -18, 19, 21, -14, 11, 14, 19, 0, -1, 7, 18, -5, 5, -27, 17, 3, -24, -8, 2, 24, -23, -9, 27, -19, 16, 29, -15, -23, 24, -4, 0, -26, 5, -29, -11, -5, -25, -18, 13, 15, 30, 25, 0, 14, 2]), 102)
