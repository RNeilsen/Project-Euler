"""This module finds the least value of n for which the number of ways of partitioning n coins
is divisible by the target"""

target = 1000000

def main():
    n = 1
    ways = [[1]]
    numways = len(ways)

    while n <= 20: # numways % target != 0:
        newways = [[n+1], [n] + [1]]
        numways = 2
        n += 1
        for w in ways[1:]: # skip the first way which will be just be [n]
            newways.append(w + [1])
            numways += 1
            if w[-1] < w[-2]:
                newways.append(w[:-1] + [w[-1] + 1])
                numways += 1
        # print(n, ":", newways)
        ways = newways
        print(n, ":", len(ways), ways)
    print(n)



from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")