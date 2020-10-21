#-------------------------------------------------------------------------------
# Name:        prob50
# Purpose:     Project Euler problem 50
#
# Author:      Richard Neilsen
#
# Created:     13-09-2013
# Copyright:   (c) Richard Neilsen 2013
#-------------------------------------------------------------------------------

from numthry import *

def main():
    sieve(10**6)
    best = 1
    for i in range(len(primes)):
        j = i+best
        while sum(primes[i:j]) < primes[-1]:
            s = sum(primes[i:j])
            if isprime(s):
                if j-i+1 > best:
                    best = j-i+1
                    print(s, "is the sum of", best, "primes")
            j += 1

if __name__ == '__main__':
    main()
