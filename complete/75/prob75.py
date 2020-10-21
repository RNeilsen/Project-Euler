"""Finds the number of Pythagorean triples
with a UNIQUE sum less than UBOUND"""

UBOUND = 1500000

from sympy.core.numbers import igcd
from math import ceil, sqrt

# Algorithm to generate primitive Pythagorean triples:
# Take m > n > 0
# Set a = m^2 - n^2, b = 2mn, c = m^2 + n^2
# If m & n are coprime, and not both odd, then (a,b,c) is a primitive Pythag triple

def main():
    # sums = dict()
    sums = [0 for i in range(UBOUND)]
    mb = ceil(sqrt(UBOUND / 2)) + 1
    for m in range(2, mb):
        nb = min(m, ceil((UBOUND - (2 * m * m)) / (2*m)))
        for n in range(1, nb):
            if igcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0):
                # primitive found!

                # No need to actually calculate a, b, c, but this will do it
                # a = m * m - n * n
                # b = 2 * m * n
                # c = m * m + n * n

                s = 2*m*(m+n)
                if s > UBOUND:
                    break

                # Find all multiples of this primitive triple
                k = 1
                while s * k < UBOUND:
                    sums[s*k] += 1
                    k += 1

    count = sums.count(1)
    print("count =", count)

from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")
