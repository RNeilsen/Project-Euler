#-------------------------------------------------------------------------------
# Name:        prob36
# Purpose:     Project Euler problem 36
#
# Author:      Richard Neilsen
#
# Created:     09/01/2013
# Copyright:   (c) p696716 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

ubound = 1000000

def main():
    total = 0
    for n in range(ubound):
        b10 = str(n)
        b2 = bin(n)[2:]

        # make sure doesn't end in 0
        if b10[-1] != 0 and b2[-1] != 0:
            if b10 == b10[::-1] and b2 == b2[::-1]:
                total += n

    print(total)

if __name__ == '__main__':
    main()
