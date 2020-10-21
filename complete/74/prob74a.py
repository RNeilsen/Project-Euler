"""Finds the number of numbers less than UBOUND whose iterated
sum of the factorials of its digits generates a chain of numbers
exactly CLENGTH numbers long"""

from time import time
from sympy import factorial

UBOUND = 1000000
CLENGTH = 60

def digfactsum(n):
	sum = 0
	for d in str(n):
		sum += factorial(int(d))
	return sum

def main():
	chains = dict()
	count = 0
	for n in range(1,UBOUND):
		c = n
	
		tempchain = []
		
		cont = True
		while cont:
			# keep repeating until we find something already in chains
			# or we re-enter the tempchain (finding a new shortchain)
			if c in chains:
				# we've hit a known value! Add tempchain to chains
				tempchain.reverse()
				i = chains[c]
				for t in tempchain:
					i+= 1
					chains[t] = i
				cont = False
			elif c in tempchain:
				# we've reentered the tempchain! New shortchain found!
				reentry = tempchain.index(c)
				shortlength = len(tempchain) - reentry
				for t in tempchain[reentry:]:
					chains[t] = shortlength
				tempchain.reverse()
				i = shortlength
				for t in tempchain[shortlength:]:
					i += 1
					chains[t] = i
				cont = False
			else:
				# just another value in the current chain, keep going
				tempchain.append(c)
				c = digfactsum(c)
		if chains[n] == CLENGTH:
			count += 1
		
	print(count)
		
if __name__ == '__main__':
	starttime = time()
	main()
	print("Completed in", time() - starttime)
