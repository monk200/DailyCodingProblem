"""
Daily Coding Problem #4

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.
"""

# SOLUTION
def findNextInt(array):     # total time complexity would be O(n+1_+ n + n+1) -> O(3n+2) -> O(n), not constant space!
    potentials = [1]*(len(array)+1)     # O(n+1)

    for i in range(0, len(array)):      # O(n)
        if array[i] > len(array):       # anything larger than the size of the array can be ignored
            continue
        if array[i] > 0:
            potentials[array[i]-1] = 0       # eliminate this index from being the potential missing number

    for j in range(0, len(potentials)):     # O(n+1)
        if potentials[j] == 1:      # has not been eliminated
            return j+1

    return len(array)       # no gaps in the array mean that the next smallest int is the size of the array


# TEST CASES
assert findNextInt([3, 4, -1, 1]) == 2, "Should be 2"     # checks the given case
assert findNextInt([1, 2, 0]) == 3, "Should be 3"     # checks the given case
assert findNextInt([]) == 1, "Should be 1"      # checks an empty array
assert findNextInt([1, 2, 5]) == 3, "Should be 3"       # checks a double gap
assert findNextInt([1, 3, 4, 6]) == 2, "Should be 2"        # checks when there are multiple spaced out gaps
assert findNextInt([-1, -3]) == 1, "Should be 1"        # checks for all negative array
assert findNextInt([1, 2, 3, 4]) == 5, "Should be 5"        # checks for no gaps

