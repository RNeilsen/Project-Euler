#-------------------------------------------------------------------------------
# Name:        prob26
# Purpose:     Project Euler Problem 26
#
# Author:      Richard Neilsen
#
# Created:     27/09/2012
# Copyright:   (c) Richard Neilsen 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Problem bypassed: 983, see "Form of cyclic numbers" on Cyclic number article
# in Wikipedia

import numthry.py

max = 20
sieve(max)

import decimal
from decimal import Decimal

def main():
    decimal.getcontext().prec = 2*max + 4
    best = 1
    for k in range(1,max):
        rec = Decimal(1)/Decimal(k)


if __name__ == '__main__':
    main()
