"""This module finds minimal sum of nodes on a path through a matrix in INFILE,
from top left to bottom right, travelling only right and down"""

INFILE = "p082_matrix.txt"


def main():
    m = getinput(INFILE)
    width = len(m[0])
    height = len(m)
    print("height =", height, "width =", width)
    # print(m)
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

    target = (height-1, width-1)

    while target not in visitednodes:
        # look through all visited nodes and find neighbour with lowest pathsum

        bestsum = dudsum
        bestxy = (0,0)

        for curnode in visitednodes:
            (y,x) = curnode
            # print((y,x))

            # these flags record whether we have already visited both right and down from a node (why??)
            rightnodevisited = False
            downnodevisited = False


            if x < width - 1:  # curnode is not on the right edge, test its right neighbour
                if (y,x+1) not in visitednodes:  # right neighbour has not yet been visited
                    if visitednodes[curnode] + m[y][x+1] < bestsum:  # path to right neighbour has lowest known sum
                        bestsum = visitednodes[curnode] + m[y][x+1]
                        bestxy = (y, x+1)
                else:
                    rightnodevisited = True

            if y < height - 1:  # curnode is not on the bottom edge, test its lower neighbour
                if (y+1,x) not in visitednodes:
                    if visitednodes[curnode] + m[y+1][x] < bestsum:
                        bestsum = visitednodes[curnode] + m[y+1][x]
                        bestxy = (y+1, x)
                else:
                    downnodevisited = True

            if rightnodevisited and downnodevisited:
                # what was supposed to go here?
                pass

        visitednodes[bestxy] = bestsum

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
