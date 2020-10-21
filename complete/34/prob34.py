#-------------------------------------------------------------------------------
# Name:        prob34
# Purpose:     Project Euler problem 34
#
# Author:      Richard Neilsen
#
# Created:     03/01/2013
# Copyright:   (c) p696716 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import math

def main():
    nf = math.factorial(9)
    n = 1
    while n*nf > 10**n:
        n+=1
    ubound = n*nf

    total = 0
    for n in range(3,ubound):
        l = [math.factorial(int(d)) for d in list(str(n))]
        if sum(l) == n:
            total += n

    print(total)

if __name__ == '__main__':
    main()
