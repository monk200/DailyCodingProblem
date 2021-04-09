"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
Follow-up: Can you do this in O(N) time and constant space?
"""


def largestSum(array):
    best = 0
    secondBest = 0

    for num in array:
        curr = max(num + secondBest, best)
        secondBest = best
        best = curr

    return best


assert largestSum([2, 4, 6, 2, 5]) == 13, "Should be 13"     # checks the given case
assert largestSum([5, 1, 1, 5]) == 10, "Should be 10"     # checks the given case
