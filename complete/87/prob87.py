"""This program finds how many numbers less than the target can be expressed as the sum of
a prime square, a prime cube, and a prime fourth power"""

from sympy import sieve

target = 50000000

def main():
    prime_squares = []
    prime_cubes = []
    prime_4thpwrs = []

    n = 1
    while sieve[n]**2 <= target:
        prime_squares.append(sieve[n]**2)
        if n**3 <= target:
            prime_cubes.append(sieve[n]**3)
        if n**4 <= target:
            prime_4thpwrs.append(sieve[n]**4)
        n += 1

    sums = set()

    for sq in prime_squares:
        for cb in prime_cubes:
            for fp in prime_4thpwrs:
                if sq + cb + fp < target:
                    sums.add(sq + cb + fp)

    # i = j = k = 0
    # while i < len(prime_squares):
    #     while prime_cubes[j] < target - prime_squares[i]:
    #         while prime_4thpwrs[k] < target - (prime_squares[i] + prime_cubes[j]):
    #             sums.add(prime_4thpwrs[k] + prime_cubes[j] + prime_squares[i])
    #             k += 1
    #         j += 1
    #     i += 1

    print(len(sums))


from time import time

if __name__ == '__main__':
    starttime = time()
    main()
    print("Completed in", time() - starttime, "seconds")