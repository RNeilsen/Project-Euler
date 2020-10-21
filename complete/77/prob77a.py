"""Finds the smallest number expressible as a sum of primes in at least TARG ways"""
# see sequence A000607 on OEIS

TARG = 5000
ubound = 105 * TARG // 43 + 1   # upper bound based on making sums with 2s, 3s, 5s and 7s

from sympy import sieve

def main():
    best = 2
    i = 0
    sums = dict()

    cont = True
    while cont:
        # take the next prime, p
        i += 1
        p = sieve[i]

        # add all viable multiples of p to all sums we can already create
        l = [0] + sorted(list(sums))    # start with zero to include pure multiples of p
        tempsums = sums.copy()  # necessary to avoid getting confused as we update the sums dict
        for s in l:
            x = (tempsums[s] if s in tempsums else 1)   # num. of ways to create s using other primes
            t = s + p

            while t < ubound:
                if t in sums:
                    sums[t] += x
                    # if we've found a lower sum that satisfies, or a sum with more ways
                    # and we haven't yet reached TARG, update best
                    if (sums[t] >= TARG and t < best) or (sums[t] > sums[best] and sums[best] < TARG):
                        best = t
                else:
                    sums[t] = x
                t += p

        if p > best and sums[best] >= TARG:
            # p > best implies we will not find any lower bests
            # this condition could maybe be tightened up to stop evaluation earlier!
            cont = False

    print(best, "expressible in", sums[best], "ways")

from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")