#-------------------------------------------------------------------------------
# Name:        prob32
# Purpose:     Project Euler problem 32
#
# Author:      Richard Neilsen
#
# Created:     27/12/2012
# Copyright:   (c) p696716 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import itertools

def main():
    s = set()
    for p in itertools.permutations(str(d) for d in range(1,10)):
        for i in range(1,4):
            for j in range(i+1,7):
                n = int("".join(p[:i]))
                m = int("".join(p[i:j]))
                o = int("".join(p[j:]))
                if n*m == o: s.add(o)
    print(sum(s))

if __name__ == '__main__':
    main()
