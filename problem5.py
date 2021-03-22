"""
Daily Coding Problem #5

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.
Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""


# GIVEN CODE
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# SOLUTION
def car(pair):
    return pair[0]


def cdr(pair):
    return pair[1]


# TEST CASES
assert car(cons(3, 4)) == 3, "Should be 3"     # checks the given case
assert cdr(cons(3, 4)) == 4, "Should be 4"      # checks the given case

