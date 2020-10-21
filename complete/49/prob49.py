#-------------------------------------------------------------------------------
# Name:        prob49
# Purpose:     Project Euler problem 49
#
# Author:      Richard Neilsen
#
# Created:     13-09-2013
# Copyright:   (c) Richard Neilsen 2013
#-------------------------------------------------------------------------------

from numthry import *

def main():
    sieve(10000)
    pr = [n for n in primes if n > 1000]
    for i in range(len(pr)):
        for j in range(i+1, len(pr)):
            (p,q) = (pr[i],pr[j])
            r = 2*q - p
            if r in pr:
                if sorted(list(str(p))) == sorted(list(str(q))) == sorted(list(str(r))):
                    print(p,q,r, "-->", str(p)+str(q)+str(r))

if __name__ == '__main__':
    main()
