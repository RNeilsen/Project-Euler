#-------------------------------------------------------------------------------
# Name:        prob43
# Purpose:     Project Euler problem 43
#
# Author:      Richard Neilsen
#
# Created:     25-07-2013
# Copyright:   (c) Richard Neilsen 2013
#-------------------------------------------------------------------------------

import itertools

def main():
    # generate all 0-9 pandigital numbers
    pans = set(int("".join(p)) for p in itertools.permutations(str(d) for d in
            range(10)))
    total = 0

    primes = [2, 3, 5, 7, 11, 13, 17]

    # test condition on all pans, and add any that satisfy all tests
    for p in pans:
        s = str(p)
        inc = True
        for i in range(7):
            if int(s[i+1:i+4]) % primes[i] != 0:
                inc = False
                break
        if inc: total += p

    print(total)

if __name__ == '__main__':
    main()
