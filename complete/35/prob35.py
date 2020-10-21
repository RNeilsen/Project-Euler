#-------------------------------------------------------------------------------
# Name:        prob35
# Purpose:     Project Euler problem 35
#
# Author:      Richard Neilsen
#
# Created:     03/01/2013
# Copyright:   (c) p696716 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import numthry
ubound = 1000000

def main():
    numthry.sieve(ubound)
    p = set(numthry.primes)
    count = 0
    for n in numthry.primes:
        l = [d for d in list(str(n))]
        # check if all rotations of n are prime and, if so, increment count
        if all([(int(''.join(l[i:] + l[:i])) in p) for i in range(len(l))]):
            count += 1
##            print("n:", n, "| rotations:", [int(''.join(l[i:] + l[:i]))
##                    for i in range(len(l))])

    print(count)

if __name__ == '__main__':
    main()
