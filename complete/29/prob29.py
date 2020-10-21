#-------------------------------------------------------------------------------
# Name:        prob29
# Purpose:     Project Euler problem 29
#
# Author:      Richard Neilsen
#
# Created:     13/12/2012
# Copyright:   (c) p696716 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

bound = 100

def main():
    s = set()
    for a in range(2,bound+1):
        for b in range(2,bound+1):
            s.add(a**b)
    print(len(s))

if __name__ == '__main__':
    main()
