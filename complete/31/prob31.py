#-------------------------------------------------------------------------------
# Name:        prob31
# Purpose:     Project Euler problem 31
#
# Author:      Richard Neilsen
#
# Created:     27/12/2012
# Copyright:   (c) p696716 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

target = 200
coins = [1,2,5,10,20,50,100,200]

def waystomake(n, lim):
    if n < 0: return 0
    if n == 0 or n == 1 or lim == 1: return 1
    return sum(waystomake(n-d,d) for d in coins if (d <= lim and d <= n))

def main():
    print(waystomake(target,max(coins)))


if __name__ == '__main__':
    main()
