"""
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""


import time


def schedule(f, n):
    time.sleep(n/1000)      # convert ms to s
    f


def function(s):
    print(s)


startTime = time.time()
schedule(function("hi"), 100)
totalTime = (time.time() - startTime) * 1000        # convert s to ms
print(totalTime)
assert (totalTime >= 95) and (totalTime <= 105), "Should be roughly 100ms"      # gave a 10ms region for error but it seems to always be within 1ms

startTime = time.time()
schedule(function("sup"), 10)
totalTime = (time.time() - startTime) * 1000        # convert s to ms
print(totalTime)
assert (totalTime >= 5) and (totalTime <= 15), "Should be roughly 10ms"      # also seems to always be within 1ms

