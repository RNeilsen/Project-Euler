"""This module finds how many layers are needed in the Ulam spiral before the
proportion of primes along the diagonals drops below 0.1"""

from sympy import isprime

def main():
    n = 1
    np = [1]
    p = []
    cont = True
    while cont:
        m = (2*n+1)**2
        np.append(m)
        for k in range(1,4):
            if isprime(m - 2*n*k): p.append(m)
            else: np.append(m)
        if 9*len(p) < len(np):
            cont = False
        print(2*n+1, len(p), len(np), len(p)+len(np))
        # if n > 100: cont = False
        n += 1

if __name__ == '__main__':
    main()