#-------------------------------------------------------------------------------
# Name:        prob46
# Purpose:     Project Euler problem 46
#
# Author:      Richard Neilsen
#
# Created:     13-09-2013
# Copyright:   (c) Richard Neilsen 2013
#-------------------------------------------------------------------------------

from numthry import *

squares = [1]
ssquares = set(squares)

def issquare(n):
    while squares[-1] < n:
        for i in range(len(squares) + 1, 2*(len(squares) + 1)):
            squares.append(i**2)
            ssquares.add(i**2)
    if n in ssquares: return False
    return True

def main():
    cont = True
    n = 9
    sieve(10000)

    while cont:
        if not isprime(n):
            test = False
            for p in primes:
                if not issquare((n - p)//2):
                    test = True
                    break
            if not test:
                print(n)
                cont = False
        n += 2

if __name__ == '__main__':
    main()
