# Project Euler, problem 23
# Richard Neilsen, completed 2012-08-06

import itertools

primes = []
def sieve(ubound):
    nums = []
    top = primes[-1] if primes != [] else 0
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
            i = 2*n
            while i < ubound + 1:
                nums[i] = False
                i += n

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
    pfact = list(primefact(n).items())

    def rgenprimes(rn, rpfacts, rfacts):
        rfacts.append(rn)
        for i in range(len(rpfacts)):
            for j in range(1,rpfacts[i][1]+1):
                rgenprimes(rn * (rpfacts[i][0]**j), rpfacts[i+1:], rfacts)

    facts = []
    rgenprimes(1, pfact,facts)
    if not incn:
        facts.remove(n)

    return(facts)


sieve(10000)

abundants = []
for n in range(1,28124):
    if sum(factorsof(n,False)) > n:
        abundants.append(n)

nums = [True] * 28124
for (a,b) in itertools.combinations_with_replacement(abundants, 2):
    if a+b < 28124: nums[a+b] = False

total = 0
for n in range(len(nums)):
    if nums[n]: total += n

print(total)