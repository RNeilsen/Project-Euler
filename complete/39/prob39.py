#-------------------------------------------------------------------------------
# Name:        prob39
# Purpose:     Project Euler problem 39
#
# Author:      Richard Neilsen
#
# Created:     10/01/2013
# Copyright:   (c) p696716 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import collections

ubound = 1000

def main():
    sqs = {n**2 : n for n in range(ubound + 1)}

    perims = collections.defaultdict(set)
    # generate all possible pythagorean triples a < b < c, with a + b + c < 1000
    for a in range(1, ubound):
        for b in range(a+1, ubound - a):
            # if a, b, c are all integral:
            if a**2 + b**2 in sqs:
                c = sqs[a**2 + b**2]
                p = a + b + c
                # if p is valid, add (a,b,c) as a legit triangle
                if p < ubound:
                    perims[p].add((a,b,c))

    p = max(perims.keys(), key=lambda x: len(perims[x]))
    print("perimeter =", p, "|", perims[p])


if __name__ == '__main__':
    main()
