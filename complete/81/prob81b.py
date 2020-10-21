"""This module finds minimal sum of nodes on a path through a matrix in INFILE,
from top left to bottom right, travelling only right and down"""

INFILE = "p081_simple_3row.txt"


def main():
    m = getinput(INFILE)
    width = len(m[0])
    height = len(m)
    print(m)
    dudsum = 0 # this will be a value larger than any plausible shortest path

    # Verify that m is a valid matrix (all rows same length, no negative values)
    # and build the dudsum value as the sum of all values in the matrix
    for l in m:
        if len(l) != width:
            print("ERROR:", INFILE, "contains rows of different lengths.")
            return()
        for num in l:
            dudsum += num
            if num <= 0:
                print(num, "is non-positive!")
                return()
    dudsum += 1

    visitednodes = {(0,0): m[0][0]}     # a dict containing the shortest sum path to reach any node

    # bestpathtonode is a dict containing the shortest sum path to reach any node
    bestpathtonode = [[dudsum for j in range(width)] for i in range(height)]
    bestpathtonode[0][0] = m[0][0]

    print(m)
    print(bestpathtonode)

    target = (height-1, width-1)

    wavefront = {(0,0)}

    while target not in visitednodes:
        (y,x) = curnode

        bestsum = dudsum
        bestxy = (0,0)

        for curnode in visitednodes:
            # test right
            if x < width - 1:
                if visitednodes[curnode] + m[y][x+1] < bestsum:
                    bestsum = visitednodes[curnode] + m[y][x+1]
                    bestxy = (x+1,y)
            # test down





    print(visitednodes[target])

def getinput(p, sep=','):
    """takes a text file consisting of lines of sep-separated integers,
    and returns as a list of lists of ints"""
    f = open(p)
    list = []
    for line in f:
        list.append([int(n) for n in line.split(sep)])
    f.close()
    return list


from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")
