#-------------------------------------------------------------------------------
# Name:        prob25
# Purpose:     Project Euler problem 25
#
# Author:      Richard Neilsen
#
# Created:     14/08/2012
# Copyright:   (c) Richard Neilsen 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    fnm = 1
    fn = 1
    n = 2
    target = 10**(1000-1)
    while fn < target:
        fnm,fn = fn, fnm + fn
        n += 1

    print(n)

if __name__ == '__main__':
    main()
