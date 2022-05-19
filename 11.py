# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

import string

def is_pangram(s):
    s = s.lower()

    for symbol in list(string.ascii_lowercase):
        if s.find(symbol) == -1:
            return False

    return True

import codewars_test as test

@test.describe("in_array")
def tests():
    pangram = "The quick, brown fox jumps over the lazy dog!"
    test.assert_equals(is_pangram(pangram), True)