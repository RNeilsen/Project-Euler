#-------------------------------------------------------------------------------
# Name:        prob27
# Purpose:     Project Euler problem 27
#
# Author:      Richard Neilsen
#
# Created:     13/12/2012
# Copyright:   (c) p696716 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

bound = 1000

import numthry

def main():
    numthry.sieve(100^2+bound*100+bound)
    best = (0,0,0)
    for a in range(-bound,bound+1):
        for b in range(-bound,bound+1):
            if numthry.isprime(b):
                n = 0
                while numthry.isprime(n*n + a*n + b):
                    n += 1
                if n > best[2]:
                    best = (a, b, n)
    print(best)

if __name__ == '__main__':
    main()
