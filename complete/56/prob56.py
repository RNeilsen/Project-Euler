"""This module finds the maximal digit sum of all numbers a^b with a,b < 100"""

max = 100

def digitsum(n):
    return sum(map(int,str(n)))

def main():
    best = 1
    for a in range(2,max):
        for b in range(2,max):
            ds = digitsum(a**b)
            best = (ds if ds>best else best)
    print(best)
    
if __name__ == '__main__':
    main()