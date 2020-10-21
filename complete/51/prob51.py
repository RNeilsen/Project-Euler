#-------------------------------------------------------------------------------
# Name:        prob51
# Purpose:     Project Euler problem 51
#
# Author:      Richard Neilsen
#
# Created:     16-09-2013
# Copyright:   (c) Richard Neilsen 2013
#-------------------------------------------------------------------------------

import sympy, itertools

def main():
	cont = True
	digits = 1
	n = 0
	while cont:
		p = sympy.sieve[n]
		plist = set()
		while p < 10**digits:
			# Only use primes that have at least 3 repeated digits, which are 0, 1 or 2,
			# and ignore the last digit when checking (there won't be eight primes if the 
			# last digit is cycled)
			s = str(p)
			for j in range(2):
				if containreps(s[:-1], str(j), 3):
					poslist = [i for i in range(len(str(p))) if s[i] == str(j)]
					comblist = itertools.combinations(poslist, 3)
					for comb in comblist:
						family = []
						for j in range(10):
							const = int(''.join( [(str(j) if i in comb else s[i]) for i in range(len(s))] ))
							if const in sympy.sieve:
								family.append(const)
						if len(family) >= 8:
							print(family)
							cont = False
							
			n += 1
			p = sympy.sieve[n]
		
		for p in plist:
			s = str(p)
			poslist = [i for i in range(len(str(p))) if s[i] == 0]
			
		digits += 1

def containreps(l, elems, n):
	# determines whether a list l contains at least n repeated elements from elems
	# returns True or False
	for e in elems:
		if l.count(e) >= n:
			return True
	return False

if __name__ == '__main__':
    main()


	