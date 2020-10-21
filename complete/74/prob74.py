"""Finds the number of numbers less than UBOUND whose iterated
sum of the factorials of its digits generates a chain of numbers
exactly CLENGTH numbers long"""

from time import time
from sympy import factorial

UBOUND = 100000
CLENGTH = 60

def digfactsum(n):
	sum = 0
	for d in str(n):
		sum += factorial(int(d))
	return sum

def main():
	count = 0
	for n in range(1,UBOUND):
		nums = set()
		cl = 0
		c = n
		while c not in nums:
			nums.add(c)
			cl += 1
			c = digfactsum(c)
		
		if cl == CLENGTH:
			count += 1
	print(count)

		
if __name__ == '__main__':
	starttime = time()
	main()
	print("Completed in", time() - starttime)