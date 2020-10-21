#-------------------------------------------------------------------------------
# Name:        prob22
# Purpose:     Project Euler, problem 22
#
# Author:      Richard Neilsen
#
# Created:     06-08-2012
# Copyright:   (c) Richard Neilsen 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys, io, string

def main():
    f = open('./names.txt', 'r')
    names = []
    for line in f:
        raw = line
    f.close()

    raw = raw.replace('"','')
    names = raw.split(',')

    names.sort()

    d = {}
    for l in range(len(string.ascii_uppercase)):
        d[string.ascii_uppercase[l]] = l+1
        d[string.ascii_lowercase[l]] = l+1

    total = 0
    for n in range(len(names)):
        namescore = 0
        for l in list(names[n]):
            namescore += d[l]
        total += namescore * (n+1)

    print(total)

if __name__ == '__main__':
    main()
