#-------------------------------------------------------------------------------
# Name:        prob44
# Purpose:     Project Euler problem 44
#
# Author:      Richard Neilsen
#
# Created:     26-07-2013
# Copyright:   (c) Richard Neilsen 2013
#-------------------------------------------------------------------------------

lpents = [1,5]
spents = set(lpents)

def morepents():
    max=2*len(lpents) + 1
    for i in range(len(lpents)+1,max):
        lpents.append( i*(3*i-1) // 2 )
    spents = set(lpents)

def main():
    i = 0
    d = 0

    # find first
    while d == 0:
        while lpents[-1] < 2 * lpents[i]:
            morepents()
            print(len(lpents), lpents[:20])

        j = i-1
        diff = lpents[i] - lpents[j]
        while diff < lpents[i-1] and j >= 0:
            if lpents[i] + lpents[j] in spents and diff in spents:
                d = diff
                print("First d:", lpents[i],lpents[j], d)
            j -= 1
        i += 1

    # find better
    while lpents[i] - lpents[i-1] < d:
        while lpents[-1] < 2 * lpents[i]:
            morepents()

        j = i-1
        diff = lpents[i] - lpents[j]
        while diff < d and j >= 0:
            if lpents[i] + lpents[j] in spents and diff in spents:
                d = diff
                print("New d:", lpents[i], lpents[j], d)
            j -= 1
        i += 1

    print(d)

if __name__ == '__main__':
    main()
