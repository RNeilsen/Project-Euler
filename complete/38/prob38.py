#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      p696716
#
# Created:     09/01/2013
# Copyright:   (c) p696716 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import itertools

def main():
    # generate set of pandigitals
    pans = [int("".join(p)) for p in itertools.permutations(str(d) for d in range(1,10))]
    pans.sort()
    pans.reverse()
    for p in pans:
        if isconcprod(p):
            print("largest:", p)
            return True

# this function not actually needed
def concprod(a,n):
    l = [str(a*i) for i in range(1,n+1)]
    return "".join(l)

def isconcprod(n):
    s = str(n)
    # concatenated product must start with 1*a so try a's from the head of n
    for a in [int("".join(s[:i])) for i in range(1,len(s))]:
        test = ''
        i = 1
        while len(test) < len(s):
            test += str(i*a)
            i += 1
        if test == s:
            return True
    return False

if __name__ == '__main__':
    main()
