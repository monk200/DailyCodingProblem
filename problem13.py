"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def substringLength(k, s):
    start = 0
    end = 1
    numUnique = 1
    longest = end - start

    while end <= len(s):
        curr = list(s[start:end])
        if s[end:end+1] in curr:     # new unique char
            if numUnique+1 > k:
                # scoot currLongest to the right
            else:
                end += 1
        longest = max(longest, end-start)       # update longest substring counter

    return longest


print(substringLength(2, "abcba"))

