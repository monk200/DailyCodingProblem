"""
Daily Coding Problem #2

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

# SOLUTION USING DIVISION -> O(n) time
def products_division(list):
    product = 1
    for i in list:
        product *= i

    newList = []
    for i in list:
        newList.append(product/i)

    return newList

# SOLUTION NOT USING DIVISION -> O(n^2) time
def products_NOdivision(list):
    newList = []
    for index in range(0, len(list)):
        product = 1
        for index2 in range(0, len(list)):      # multiply product by number at each index EXCEPT for the current number at index
            if index != index2:
                product *= list[index2]
        newList.append(product)
    return newList


# TEST CASES USING DIVISION
assert products_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24], "Should be [120, 60, 40, 30, 24]"     # checks the given case
assert products_division([3, 2, 1]) == [2, 3, 6], "Should be [2, 3, 6]"     # checks the given case
assert products_division([3, 5, 5, 2]) == [50, 30, 30, 75], "Should be [50, 30, 30, 75]"     # checks to make sure repeated entries work

# TEST CASES NOT USING DIVISION
assert products_NOdivision([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24], "Should be [120, 60, 40, 30, 24]"     # checks the given case
assert products_NOdivision([3, 2, 1]) == [2, 3, 6], "Should be [2, 3, 6]"     # checks the given case
assert products_NOdivision([3, 5, 5, 2]) == [50, 30, 30, 75], "Should be [50, 30, 30, 75]"     # checks to make sure repeated entries work

