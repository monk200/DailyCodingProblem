"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.
"""


import random


def estimate(iterations):
    inUnitCircle = 0
    total = 0

    while iterations > 0:
        x = random.random()
        y = random.random()
        if (x**2 + y**2) <= 1:      # within/on edge of unit circle
            inUnitCircle += 1
        total += 1
        iterations -= 1

    return 4 * (inUnitCircle/total)


for i in range(0, 10):
    est = round(estimate(30000000), 4)      # rounds to first 4 decimal places
    print(est)
    assert  3.140 <= est and est <= 3.142, "Should be 3.141"        # test allows for some wiggle room