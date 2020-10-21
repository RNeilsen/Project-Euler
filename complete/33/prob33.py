#-------------------------------------------------------------------------------
# Name:        prob33
# Purpose:     Project Euler problem 33
#
# Author:      Richard Neilsen
#
# Created:     03/01/2013
# Copyright:   (c) p696716 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    smalls = [(a,b) for a in range(1,10) for b in range(a+1,10)]
    larges = [(a,b) for a in range(10,100) for b in range(a+1,100)]

    d = {}
    for(a,b) in smalls:
        d[(a,b)] = set()
        for (x,y) in larges:
            if a*y == x*b:
                d[(a,b)].add((x,y))

    (e,f) = (1,1)
    for (a,b) in smalls:
        for (x,y) in d[(a,b)]:
            (la,lb) = ( [int(n) for n in list(str(a))],
                        [int(n) for n in list(str(b))])
            (lx,ly) = ( [int(n) for n in list(str(x))],
                        [int(n) for n in list(str(y))])

            for n in range(1,10):
                if n in lx and n in ly:
                    lx.remove(n)
                    ly.remove(n)
                    if (la,lb) == (lx,ly):
                        (e,f) = (e*x, f*y)

    ubound = e
    t = 2
    while t*t < ubound:
        while e % t == 0 and f % t == 0:
            (e,f) = (e // t, f // t)
        t += 1

    print("product:", f)

if __name__ == '__main__':
    main()
