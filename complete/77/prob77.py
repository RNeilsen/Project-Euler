"""Finds the smallest number expressible as a sum of primes in at least TARG ways"""

TARG = 5
ubound = 5*TARG     # you can make 5*TARG as a sum of 5s, and as a sum of (2+3)s, and
                    # by changing each 5 to a (2+3) you can make it in TARG+1 ways

from itertools import combinations_with_replacement
from sympy import sieve

def main():
    primes = [i for i in sieve.primerange(1,ubound)]
    ways = dict()

    for n in range(TARG):
        for c in combinations_with_replacement(primes,n):
            s = sum(c)
            if s in ways:
                ways[s] += 1
            else:
                ways[s] = 1

    l = list(ways)
    l.sort()
    n = 0
    for i in l:
        if ways[i] >= TARG:
            print(i, ways[i])
            print(10, ways[10])
            break
    return


from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")