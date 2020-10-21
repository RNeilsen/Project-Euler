#-------------------------------------------------------------------------------
# Name:        prob47
# Purpose:     Project Euler problem 47
#
# Author:      Richard Neilsen
#
# Created:     13-09-2013
# Copyright:   (c) Richard Neilsen 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from numthry import *

def main():
    cont = True
    n = 2
    while cont:
        if len(primefact(n+3)) == 4:
            if len(primefact(n+2)) == 4:
                if len(primefact(n+1)) == 4:
                    if len(primefact(n)) == 4:
                        print(n)
                        cont = False
                    else:
                        n += 1
                else: n += 2
            else: n += 3
        else: n += 4

if __name__ == '__main__':
    main()
