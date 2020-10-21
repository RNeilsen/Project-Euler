#-------------------------------------------------------------------------------
# Name:        prob37
# Purpose:     Project Euler problem 37
#
# Author:      Richard Neilsen
#
# Created:     09/01/2013
# Copyright:   (c) p696716 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import numthry

def main():
    numthry.sieve(1000000)
    count = 0
    total = 0
    n = 10

    while count < 11:
        if numthry.isprime(n):
            s = str(n)
            truncs = [s[i:] for i in range(len(s))] + [s[:i+1] for i in range(len(s)-1)]
            if all(numthry.isprime(int(t)) for t in truncs):
                total += n
                count += 1
        n += 1
    print(total)


if __name__ == '__main__':
    main()
