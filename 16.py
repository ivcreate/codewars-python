# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def process_calc(number, res):
    if res:
        return int(eval(number + res))
    return number

def zero(res=''):
    return process_calc('0', res)

def one(res=''):
    return process_calc('1', res)

def two(res=''):
    return process_calc('2', res)

def three(res=''):
    return process_calc('3', res)

def four(res=''):
    return process_calc('4', res)

def five(res=''):
    return process_calc('5', res)

def six(res=''):
    return process_calc('6', res)

def seven(res=''):
    return process_calc('7', res)

def eight(res=''):
    return process_calc('8', res)

def nine(res=''):
    return process_calc('9', res)

def plus(num):
    return "+" + num

def minus(num):
    return "-" + num

def times(num):
    return "*" + num

def divided_by(num):
    return "/" + num

import codewars_test as test


@test.describe("in_array")
def tests():
    test.describe('Basic Tests')
    test.assert_equals(seven(times(five())), 35)
    test.assert_equals(four(plus(nine())), 13)
    test.assert_equals(eight(minus(three())), 5)
    test.assert_equals(six(divided_by(two())), 3)
