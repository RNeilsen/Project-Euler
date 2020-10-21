#-------------------------------------------------------------------------------
# Name:        prob48
# Purpose:     Project Euler problem 48
#
# Author:      Richard Neilsen
#
# Created:     13-09-2013
# Copyright:   (c) Richard Neilsen 2013
#-------------------------------------------------------------------------------

def main():
    sum = 0
    for n in range(1,1001):
        sum += pow(n,n,10**10)
    print(sum)

if __name__ == '__main__':
    main()