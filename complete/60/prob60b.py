"""This module finds the smallest set of NUMPRIMES primes such that any two 
concatenated in any order produces a prime, then calculates the sum of that set."""

NUMPRIMES = 5

from sympy import sieve, isprime
from itertools import combinations

def main():
	# cliques[m] is the set of cliques of primes congruent to m, mod 3
	# each element of cliques[m] is a frozenset consisting of a clique of pairwise compatible primes
	# cliques[m] only stores cliques of order 3 or higher - 2-cliques are not stored
	cliques = [set(), set(), set()]
	
	# compats: keys are prime ints, vals are sets of compatible other ints
	# 3 is a special case and is considered in both compats[1]/cliques[1] and compats[2]/cliques[2]
	compats = [{}, {3:set()}, {3:set()}]
	
	lowest = -1
	
	n = 4      # n = which #prime we are testing. 2, 3, and 5, i.e. sieve[1:3], can be skipped
	
	cont = True
	while cont:
		p = sieve[n]
		m = p % 3 # m indexes us into compats[1]/cliques[1] or compats[2]/cliques[2]
		compats[m][p] = set()
		
		for q in compats[m].keys():
			# incorporate p into the compats table
			if testpair(p,q):
				compats[m][q].add(p)
				compats[m][p].add(q)
		
		for q in compats[m][p]:
			# test each q in p's compat set
			for r in compats[m][p] & compats[m][q]:
				# p,q,r are a 3-clique
				cliques[m].add(frozenset((p,q,r)))
				
				# now find any cliques that already contained q and r, and see if p can also be added
				newcliques = set()
				for c in cliques[m]:
					if {q,r} < c:
						valid = True
						for s in (c - {q,r}):
							if p not in compats[m][s]:
								valid = False
								break
						if valid:
							nc = (c | {p})
							if len(nc) == NUMPRIMES:
								if sum(nc) < lowest or lowest == -1:
									lowest = sum(nc)
									print("New lowest:", nc, "-->", sum(nc))
									return
							newcliques.add(nc)
								
				cliques[m] |= newcliques
				
		n += 1
		if p > lowest > 0:
			cont = False
		
def testpair(a,b):
	"""Determines whether two primes produce primes when concatenated in either order"""
	return (isprime(int(str(a) + str(b))) and isprime(int(str(b) + str(a))))
	
	
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