"""Finds the smallest number expressible as a sum of primes in at least TARG ways"""

TARG = 50
ubound = 5*TARG     # you can make 5*TARG as a sum of 5s, and as a sum of (2+3)s, and
                    # by changing each 5 to a (2+3) you can make it in TARG+1 ways

from sympy import sieve

def main():
    best = 2
    i = 0
    sums = dict()
    for n in range(ubound):
        sums[n] = 0

    cont = True
    while cont:
        # take the next prime, p
        i += 1
        p = sieve[i]

        # add all viable multiples of p to all sums already known
        l = sorted(list(sums))
        for s in l:
            t = s + p
            while t < ubound:
                sums[t] += 1

                # if we've found a lower sum with the same number of ways, or a sum with more ways
                # and we haven't yet reached TARG, update best
                if (sums[t] == sums[best] and t < best) or (sums[t] > sums[best] and sums[best] < TARG):
                    best = t

                t += p

        # add all multiples of p
        # t = p
        # while t < ubound:
        #     sums[t] = 1
        #     t += p

        if p > best and sums[best] >= TARG:
            cont = False



    print(best, sums[best])

from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")