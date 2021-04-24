"""
Daily Coding Problem #13

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
        if s[end:end+1] not in curr:     # new unique char
            if numUnique+1 > k:     # scoot curr to the right
                start += 1
                if curr.count(curr[0]) == 1:
                    numUnique -= 1
            else:       # expand curr to this char
                end += 1
                numUnique += 1
                longest = max(longest, end-start)       # update longest substring counter
        else:       # not unique char
            end += 1
            longest = max(longest, end-start)

    return longest


assert substringLength(2, "abcba") == 3, "Should be 3"      # checks the given case
assert substringLength(4, "jkhkuioiu") == 6, "Should be 6"

