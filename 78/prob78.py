"""This module finds the smallest value n such that p(n) is divisible by DIV,
where p is the partition function"""

from functools import lru_cache

DIV = 1000000

def main():
    cont = True
    n = 1
    while cont:
        if p(n) % DIV == 0:
            print(n, p(n))
            cont = False
        n += 1

@lru_cache(maxsize=DIV**2)
def p(n):
    return ways(n,n)

@lru_cache(maxsize=DIV**2)
def ways(n, m): # number of ways to make n as a sum of numbers each at most m
    if n in {0,1} or m in {0,1}:
        # there's only one way to make 1, and only one way to make anything with just 1s
        return 1
    count = 0
    for i in range(1, m+1):
        count += ways(n-i,min(n-i,i))
    return count


    # for i in range(2, n):
    #     count += 1
    #     if i < n-1: # still room to add 2s to this
    #         for j in range(2, i+1):
    #             count += ways(n - i - j)
    #             # the problem is you get to here having counted 2,2 and then you start looking
    #             # at all the ways to make 6, which includes 3,3 so now you have counted 2,2,3,3
    #             # which will be counted again later as part of 3,3,2,2
    #             # Perhaps ways() needs a 'max' argument, but then caching won't work... argh
    # return count

from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")