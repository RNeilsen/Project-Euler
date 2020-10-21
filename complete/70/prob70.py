"""This module finds the value of n in 1 < n < ubound for which
phi(n) is a digit permutation of n, and which minimises n/phi(n)
(where phi is the Euler totient function)."""

ubound = 10**7

from sympy.ntheory import totient
from time import time

def main():
	starttime = time()
	min = ubound
	best = 1
	
	for n in range(2,ubound):
		t = totient(n)
		if ispermut(t, n):
			if min * t > n:
				min = n / t
				best = n
				print("New best:", n, "-->", min, "after", round(time() - starttime,3), "seconds")
	
	print(best, totient(best))
	print("Completed in", time() - starttime, "seconds.")

def ispermut(ina,inb):
	"""Determines whether one integer is a digit permutation of the other"""
	return sorted(str(ina)) == sorted(str(inb))
	# a = str(ina)
	# b = str(inb)
	
	# lista = [0 for i in range(10)]
	# listb = [0 for i in range(10)]
	# for c in a:
		# lista[int(c)] += 1
	# for c in b:
		# listb[int(c)] += 1
	
	# return lista == listb
	
if __name__ == '__main__':
	main()