"""
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""


import random


def chooseElement(stream):
    rand = stream[0]        # default for if stream is just one element

    for index, elem in enumerate(stream):
        if random.randint(0, index) == 0:       # every element up to this index has 1/n chance of being chosen
            rand = elem

    return rand


s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("chooseELement(s[0:1]): ", chooseElement(s[0:1]))
print("chooseELement(s[0:2]): ", chooseElement(s[0:2]))
print("chooseELement(s[0:6]): ", chooseElement(s[0:6]))
print("chooseELement(s[0:9]): ", chooseElement(s[0:9]))
print("chooseELement(s[0:10]): ", chooseElement(s[0:10]))

