"""This module finds the value of n less than ubound for which
n/phi(n) is maximal (where phi is the Euler totient function)"""

ubound = 1000000

from sympy.ntheory import totient

def main():
	max = 0
	best = 1
	
	for n in range(1,ubound):
		cur = n / totient(n)
		if cur > max:
			print("New best:", n, "-->", cur)
			max = cur
			best = n
	
	print(best)

if __name__ == '__main__':
	main()