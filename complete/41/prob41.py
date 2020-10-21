#-------------------------------------------------------------------------------
# Name:        prob41
# Purpose:     Project Euler problem 41
#
# Author:      Richard Neilsen
#
# Created:     10/01/2013
# Copyright:   (c) p696716 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import numthry, itertools

# 8- and 9-digit pandigitals are necessarily composite (divisible by 3)
ubound = 7

def main():
    numthry.sieve(10**ubound)
    pans = set(int("".join(p)) for p in itertools.permutations(str(d)
            for d in range(1,ubound + 1)))
    panprimes = numthry.sprimes & pans
    print(max(panprimes))

if __name__ == '__main__':
    main()
