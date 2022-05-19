# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

HEXDECIMAL = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

def generate_hexadecimal(number):
    if number < 1:
        return

    int_part = number//16
    decimal_part = number % 16

    return HEXDECIMAL[int_part] + HEXDECIMAL[decimal_part]


def get_hexadecimal_number(number):
    if number >= 255:
        result = 'FF'
    elif number <= 0:
        result = '00'
    else:
        result = generate_hexadecimal(number)

    return result

def rgb(r, g, b):
    r_res = get_hexadecimal_number(r)
    g_res = get_hexadecimal_number(g)
    b_res = get_hexadecimal_number(b)

    return r_res + g_res + b_res

import codewars_test as test

@test.describe("in_array")
def tests():
    test.assert_equals(rgb(10 ,10 ,10), "0A0A0A", "testing zero values")
    test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
    test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
    test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
    test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")