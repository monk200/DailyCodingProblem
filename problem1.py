"""
Daily Coding Problem #1

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
"""

# SOLUTION
def doTheyAdd(list, k):
    pairs = []
    for num in list:        # this technically only passes the list once, even though it passes through pairs every iteration
        if num in pairs:        # if we have already passed the number that makes current num add to k
            return True                 # return True
        pairs.append(k - num)       # append at the end to avoid edge case list = [x, y, 5, z], k = 10
    return False

# TEST CASES
assert doTheyAdd([10, 15, 3, 7], 17) == True, "Should be True"     # checks the given case
assert doTheyAdd([2, 9, 5, 4], 10) == False, "Should be False"      # makes sure it doesn't count 5 twice
assert doTheyAdd([], 0) == False, "Should be False"     # an empty list should not add to any numbers (even zero)
assert doTheyAdd([-1, -2, 5, 8], -3) == True, "Should be True"      # works with negatives

