"""This module finds the smallest maximum integer M, for which the number of cuboids with
integer dimensions up to MxMxM, whose shortest path along the walls from one corner to
its opposite diagonal is an integer, exceeds <target>."""

# Problem: This program gives correct answers for M <= 11, but at M=12 it finds 24 cuboids
# when there are 25. It's then one short up to M=20, where it misses another 3.
# EDIT: Solved this

target = 1000000

from math import sqrt


def isnat(num):
    return abs(float(num) - round(num)) < 0.000000001


def findshortest(l, w, h):
    """Find the shortest path along any faces of an l*w*h cuboid"""
    a = findshortestalongbase(l, w, h)
    return a    # seems to always be a...
    # b = findshortestalongbase(w, h, l)
    # c = findshortestalongbase(h, l, w)
    # shortest = min(a,b,c)
    # print("shortest for", (l,w,h), "is", shortest)
    return shortest


def findshortestalongbase(l, w, h):
    """Find the shortest path along the base of an l*w*h cuboid"""

    if h == w:
        return 2*sqrt(h**2 + (l/2)**2)

    # Stationary points of the path length function occur at hl/(h+w) and hl/(h-w)
    opta = h*l / (h+w)
    optb = h*l / (h-w)
    if opta > l:
        return sqrt(h**2 + optb**2) + sqrt(w**2 + (l-optb)**2)
    else:
    # if optb < 0 or optb > l:      # experimentally, never seems to need the subsequent option
        return sqrt(h**2 + opta**2) + sqrt(w**2 + (l-opta)**2)

    return min(sqrt(h**2 + opta**2) + sqrt(w**2 + (l-opta)**2),
               sqrt(h**2 + optb**2) + sqrt(w**2 + (l-optb)**2))


def main():
    starttime = time()
    M = 1
    l = w = h = 1
    numpaths = 0
    out = []
    while numpaths < target:
        M += 1

        # Assume l >= w >= h
        l += 1
        for w in range(1, l+1):
            for h in range(1, w+1):
                shortestpath = findshortest(l,w,h)
                if isnat(shortestpath):
                    # print("Int path found for", (l,w,h), ":", shortestpath)
                    numpaths += 1
        out.append((M, numpaths))
        if M % 100 == 0:
            print("M =", M, ":", numpaths, "cuboids found in", round(time() - starttime, 1), "seconds")
    print(M, numpaths)
    print(out)

from time import time


if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")