"""This module finds the smallest set of NUMPRIMES primes such that any two 
concatenated in any order produces a prime, then calculates the sum of that set."""

NUMPRIMES = 4

from sympy import sieve
from itertools import combinations

def main():
	cont = True
	n = NUMPRIMES
	lowest = -1
	while cont: # this iterates through all subsets of primes up to the n'th prime
		for x in combinations(sieve._list[:n-1], NUMPRIMES - 1):
			l = list(x) + [sieve[n]]
			# print("Testing:", l)
			if testsubset(l):
				s = sum(l)
				print("Valid subset:", l, "->", s)
				if s < lowest or lowest == -1:
					lowest = s
					print("New lowest:", l, "->", lowest)
					
			if 0 < lowest < NUMPRIMES * sieve[n - NUMPRIMES]:
				cont = False
				
		n += 1
		
	print(lowest)
		
def testsubset(l):
"""Tests a set of primes to see if every pairwise concatenation results in a prime"""
	if 2 in l or 5 in l:
		return False
	for x in combinations(l, 2):
		a = x[0]
		b = x[1]
		ab = a * (10**len(str(b))) + b
		ba = b * (10**len(str(a))) + a
		if not (ab in sieve and ba in sieve):
			return False
	return True
	
if __name__ == '__main__':
    main()