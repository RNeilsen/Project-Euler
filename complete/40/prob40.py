#-------------------------------------------------------------------------------
# Name:        prob40
# Purpose:     Projec Euler problem 40
#
# Author:      Richard Neilsen
#
# Created:     10/01/2013
# Copyright:   (c) p696716 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

pos = set([1,10,100,1000,10000,100000,1000000])

def main():
    n = 0
    p = 0
    t = 1
    # while there are still digits to gather
    while pos:
        s = list(str(n))
        # while this number hasn't been exhausted
        while s:
            if p in pos:
                pos.remove(p)
                t *= int(s.pop(0))
            else:
                s.pop(0)
            p += 1
        n += 1
    print(t)
if __name__ == '__main__':
    main()
