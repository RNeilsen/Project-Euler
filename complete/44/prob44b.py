#-------------------------------------------------------------------------------
# Name:        Prob44b
# Purpose:     Project Euler problem 44, attempt 3
#
# Author:      Richard Neilsen
#
# Created:     31-07-2013
# Copyright:   (c) Richard Neilsen 2013
#-------------------------------------------------------------------------------

pents = [1,5]
spents = set(pents)

def morepents():
    l = len(pents)
    for n in range(l+1,2*l):
        p = (3*n*n - n)//2
        pents.append(p)
        spents.add(p)

def main():
    morepents()
    morepents()
    morepents()
    print(pents)
    low = 0
    i = 1
    d = 0
    cont = True

    while cont:
        test = 2*pents[i]
        while test > pents[-1]:
            print(i, pents[i], len(pents), pents[-1])
            morepents()
        for j in range(low,i-1):
            if pents[i]-pents[i-1] > pents[j]:
                low = j
            elif pents[i] + pents[j] in spents:
                if pents[i] + 2*pents[j] in spents:
                    print("P_i =", pents[i], ", P_j =", pents[j])
                    cont = False
        i += 1




if __name__ == '__main__':
    main()
