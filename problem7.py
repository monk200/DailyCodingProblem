"""
Daily Coding Problem #7

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

# SOLUTION
def decode(msg):
    return decodeHelper(msg, len(msg))

def decodeHelper(msg, pos):
    if pos-2 < 0:       # at the beginning of the string
        return 1

    numWays = 0
    if(msg[pos-2] <= "2") and (msg[pos-1] <= "6"):      # current 2 digits are within 26 characters
        numWays += 2 + decodeHelper(msg, pos-2)
    else:       # current 2 digits are greater than 26 and therefore must be 2 single-digit characters
        numWays += 1 + decodeHelper(msg, pos-1)
    return numWays

# TEST CASES
assert decode("111") == 3, "Should be 3"     # checks the given case
assert decode("1234") == 4, "Should be 4"
