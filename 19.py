# How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
#
# I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.
#
# Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.

import string


def rot13(message):
    result = ''
    symbols = string.ascii_letters
    for sym in message:
        right_sym = sym
        symbol_pos = symbols.find(sym)

        if symbol_pos != -1:
            right_sym = symbols[symbol_pos + 13 if symbol_pos + 13 < len(symbols) else symbol_pos + 13 - len(symbols)]
            right_sym = right_sym.lower() if sym.islower() else right_sym.upper()

        result += right_sym

    return result

#
#   or return message.encode('rot13')
#

import codewars_test as test

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(rot13("EBG13 rknzcyr."), "ROT13 example.")
    test.assert_equals(rot13(
        "How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."),
                       "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
    test.assert_equals(rot13("123"), "123")
    test.assert_equals(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"),
                       "This is actually the first kata I ever made. Thanks for finishing it! :)")
    test.assert_equals(rot13("@[`{"), "@[`{")