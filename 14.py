# Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.
#
# Example:
#
# Given an input string of:
#
# apples, pears # and bananas
# grapes
# bananas !apples
# The output expected would be:
#
# apples, pears
# grapes
# bananas
# The code would be called like so:
#
# result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# # result should == "apples, pears\ngrapes\nbananas"

def solution(string, markers):
    res = []
    for row in string.split("\n"):
        added_string = row
        for marker in markers:
            if added_string.find(marker) != -1:
                added_string = added_string.split(marker)[0].strip()
        res.append(added_string)

    return "\n".join(res)

import codewars_test as test

@test.describe("in_array")
def tests():
    # -*- coding: utf-8 -*-
    test.assert_equals(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]),
                       "apples, pears\ngrapes\nbananas")
    test.assert_equals(solution("a #b\nc\nd $e f g", ["#", "$"]), "a\nc\nd")