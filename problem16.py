"""
Daily Coding Problem #16

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""


class Log:
    _queue = []

    def __init__(self, N):
        self.N = N

    def record(self, order_id):
        self._queue.append(order_id)
        if len(self._queue) > self.N:        # remove oldest element once queue hits N elements
            self._queue.pop(0)

    def get_last(self, i):
        if i > self.N:      # i is guaranteed to be smaller than or equal to N
            return None

        index = len(self._queue) - i
        if index < 0:           # in case i goes beyond the start of the list
            index = 0

        return self._queue[index]


test = Log(5)
test.record("a")
assert test.get_last(2) == "a", "Should be a"      # checks when i is beyond the start of the list
assert test.get_last(1) == "a", "Should be a"      # checks when i is at the start of the list
test.record("b")
test.record("c")
test.record("d")
test.record("e")
# checks when list is full
assert test.get_last(5) == "a", "Should be a"
assert test.get_last(4) == "b", "Should be b"
assert test.get_last(3) == "c", "Should be c"
assert test.get_last(2) == "d", "Should be d"
assert test.get_last(1) == "e", "Should be e"
test.record("f")
# checks that the oldest element got removed
assert test.get_last(5) == "b", "Should be b"
assert test.get_last(4) == "c", "Should be c"
assert test.get_last(3) == "d", "Should be d"
assert test.get_last(2) == "e", "Should be e"
assert test.get_last(1) == "f", "Should be f"
# checks when i is greater than N
assert test.get_last(6) is None, "Should be None"

