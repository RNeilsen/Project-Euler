"""This module finds minimal sum of nodes on a path through a matrix in INFILE,
from the left edge to the right edge, travelling only up, down and right"""

INFILE = "p082_matrix.txt"

def main():
    m = getinput(INFILE)
    width = len(m[0])
    height = len(m)
    print("height =", height, "width =", width)
    # print(m)

    # Verify that m is a valid matrix (all rows same length, no negative values)
    # Build the dudsum value as the sum of all values in the matrix
    dudsum = 1
    bestsum = m[0][0]
    for l in m:
        if len(l) != width:
            print("ERROR:", INFILE, "contains rows of different lengths.")
            return()
        for num in l:
            dudsum += num
            if num <= 0:
                print(num, "is non-positive!")
                return()
        if l[0] < bestsum:
            bestsum = l[0]

    # Build the visitednodes dict by incorporating all possible starting nodes
    visitednodes = dict()
    for i in range(height):
        visitednodes[(i,0)] = m[i][0]

    print(m)
    print(visitednodes)

    rightmostvisited = 0

    while rightmostvisited < width - 1:
        bestsum = dudsum

        for curnode in visitednodes:
            (y,x) = curnode  # coordinates of curnode
            if (y, x+1) not in visitednodes:
                if visitednodes[curnode] + m[y][x+1] < bestsum:
                    bestsum = visitednodes[curnode] + m[y][x+1]
                    bestxy = (y, x+1)
            if y > 0 and (y-1, x) not in visitednodes:
                if visitednodes[curnode] + m[y-1][x] < bestsum:
                    bestsum = visitednodes[curnode] + m[y-1][x]
                    bestxy = (y-1, x)
            if y < height - 1 and (y+1, x) not in visitednodes:
                if visitednodes[curnode] + m[y+1][x] < bestsum:
                    bestsum = visitednodes[curnode] + m[y+1][x]
                    bestxy = (y+1, x)

        visitednodes[bestxy] = bestsum
        if bestxy[1] > rightmostvisited:
            rightmostvisited += 1
            if rightmostvisited == width - 1:
                print("Final:", bestsum)
                return

    # old code below, didn't work properly
    # while rightmostvisited != width - 1:
    #     # look through all visited nodes and find neighbour with lowest pathsum
    #
    #     bestsum = dudsum
    #     bestxy = (0,0)
    #
    #     for curnode in visitednodes:
    #         (y,x) = curnode
    #         # print((y,x))
    #
    #         # these flags record whether we have already visited both right and down from a node (why??)
    #         rightnodevisited = False
    #         downnodevisited = False
    #         upnodevisited = False
    #
    #         if x < width - 1:  # curnode is not on the right edge, test its right neighbour
    #             if (y,x+1) not in visitednodes:  # right neighbour has not yet been visited
    #                 if visitednodes[curnode] + m[y][x+1] < bestsum:
    #                     bestsum = visitednodes[curnode] + m[y][x+1]
    #                     bestxy = (y, x+1)
    #             else:
    #                 rightnodevisited = True
    #
    #         if y < height - 1:  # curnode is not on the bottom edge, test its lower neighbour
    #             if (y+1,x) not in visitednodes:  # lower neighbour has not yet been visited
    #                 if visitednodes[curnode] + m[y+1][x] < bestsum:
    #                     bestsum = visitednodes[curnode] + m[y+1][x]
    #                     bestxy = (y+1, x)
    #             else:
    #                 downnodevisited = True
    #
    #         if y > 0:  # curnode is not on the top edge, test its upper neighbour
    #             if (y-1,x) not in visitednodes:  # upper neighbour has not yet been visited
    #                 if visitednodes[curnode] + m[y-1][x] < bestsum:
    #                     bestsum = visitednodes[curnode] + m[y-1][x]
    #                     bestxy = (y-1, x)
    #             else:
    #                 upnodevisited = True
    #
    #         if rightnodevisited and downnodevisited and upnodevisited:
    #             # what was supposed to go here?
    #             pass
    #
    #     print(m)
    #     print(visitednodes)
    #
    #     visitednodes[bestxy] = bestsum
    #     if bestxy[0] == width-1:
    #         print(bestsum)
    #         return
    #     else:
    #         rightmostvisited = max(rightmostvisited, bestxy[0])

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
