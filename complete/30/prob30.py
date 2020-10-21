#-------------------------------------------------------------------------------
# Name:        Prob30
# Purpose:     Project Euler problem 30
#
# Author:      Richard Neilsen
#
# Created:     18/12/2012
# Copyright:   (c) p696716 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

power = 5

def main():
    # find upper bound
    n = 1
    while 10**n - 1 < n * (9**power):
        n += 1
    ubound = n * (9**power)
    print("ubound:", ubound)

    # find sum
    for n in range(2,ubound):
        total = 0
        if n == sum(int(d)**5 for d in str(n)):
            total += n

    print("total:", total)

if __name__ == '__main__':
    main()
