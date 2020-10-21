#-------------------------------------------------------------------------------
# Name:    numthry
# Purpose:   Useful functions for basic number theory
#
# Author:   Richard Neilsen
#
# Created:   02/08/2012
# Copyright:  (c) Richard Neilsen 2012
# Licence:   None
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import itertools

primes = []
sprimes = set()

def sieve(ubound):
    nums = []
    top = primes[-1] if primes != [] else 1
    nums = [False] * top + [True] * (ubound - top + 1)
    for p in primes:
        nums[p] = True
        i = top
        while i%p != 0:
            i += 1
        while i < ubound + 1:
            nums[i] = False
            i += p

    for n in range(max(2,top), ubound + 1):
        if nums[n] == True:
            primes.append(n)
            sprimes.add(n)
            i = 2*n
            while i < ubound + 1:
                nums[i] = False
                i += n

def isprime(n):
    if primes == []: sieve(2*n)
    elif primes[-1] < n: sieve(2*n)
    if n in sprimes: return True
    return False

def primefact(n):
    if n <= 1: return {}
    if primes == []: sieve(2*n)
    elif primes[-1] < n: sieve(2*n)
    pfact = {}
    for p in primes:
        if p > n // 2 + 1:
            break
        multiplicity = 0
        nptest = n
        while nptest%p == 0:
            multiplicity += 1
            nptest = nptest // p
        if multiplicity != 0: pfact[p] = multiplicity

    return (pfact if pfact else {n: 1})

def factorsof(n, incn=True):
    if n <= 1: return {}
    if primes == []: sieve(2*n)
    elif primes[-1] < n: sieve(2*n)
    pfact = primefact(n)
    pfactcopy = pfact.keys()

    for p in pfactcopy:
        mult = pfact[p]
        del pfact[p]

def gcd(m,n):
    if m == n: return m
    if n < m: (m,n) = (n,m)
    # now assume m < n
    if n % m == 0: return m
    pfact = primefact(m)
    g = 1
    for p in pfact.keys():
        # find gcd here
        pass

def main():
    pass

if __name__ == '__main__':
    main()
