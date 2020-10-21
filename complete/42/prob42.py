#-------------------------------------------------------------------------------
# Name:        prob42
# Purpose:     Project Euler problem 42
#
# Author:      Richard Neilsen
#
# Created:     25-07-2013
# Copyright:   (c) Richard Neilsen 2013
#-------------------------------------------------------------------------------

import io, string

trinums = set()

def main():
    # open the file and store the words in a list
    f = open('.\words.txt', 'r')
    raw = f.readline()
    raw = raw.replace('"','')
    words = raw.split(',')

    # unlikely that any words will have an alpha value greater than the 50th
    # triangular number
    calctrinums(50)

    # d is the alphavalues of each letter, case ignored
    d = {}
    for l in range(len(string.ascii_uppercase)):
        d[string.ascii_uppercase[l]] = l+1
        d[string.ascii_lowercase[l]] = l+1

    # test each word and count all triangular words
    numtriwords = 0
    for w in words:
        wscore = 0
        for l in list(w):
            wscore += d[l]
        if wscore in trinums:
            numtriwords += 1

    print(numtriwords)

def calctrinums(n):
    total = 0
    for i in range(1,n):
        total += i
        trinums.add(total)

if __name__ == '__main__':
    main()
