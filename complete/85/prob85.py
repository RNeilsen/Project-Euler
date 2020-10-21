"""This finds the area of a rectangular grid with the closest number to target rectangles inside"""

target = 2000000

from math import sqrt, ceil

def main():
    bestdiff = target + 1
    for w in range(1, ceil(sqrt(target))):
        (lbound, ubound) = (1, w)

        # binary search on h values to find h with closest to target number of rectangles
        while ubound - lbound > 1:
            h = (lbound + ubound) // 2

            # find number of rectangles for w * h grid
            numrects = 0
            for i in range(1,w+1):
                for j in range(1, h+1):
                    numrects += (w - i + 1)*(h - j + 1)

            diff = abs(target - numrects)
            if diff < bestdiff:
                bestdiff = diff
                bestarea = w * h
                print ("New best diff:", numrects, "rectangles on", w, "x", h, "=", bestarea)

            # print current number of rectangles and update bounds on h
            if numrects < target:
                lbound = h
            elif numrects > target:
                ubound = h
            else:
                print("Exact solution found:", w, "x", h, "contains", numrects, "rectangles.")
                return

    print(bestarea)


from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")