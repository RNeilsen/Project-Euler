#-------------------------------------------------------------------------------
# Name:        problem24
# Purpose:     Project Euler problem 24
#
# Author:      Richard Neilsen
#
# Created:     14/08/2012
# Copyright:   (c) Richard Neilsen2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import itertools

def main():
    p = list(itertools.permutations(list(range(10))))[1000000-1]
    s = ""
    for i in p:
        s += str(i)
    print(s)

if __name__ == '__main__':
    main()
