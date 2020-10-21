"""Finds the number of proper reduced fractions with denominator 
less than or equal to UBOUND"""

from sympy.ntheory import totient

UBOUND = 1000000

def main():
	n = 0
	for d in range(2,UBOUND+1):
		n += totient(d)
	
	print(n)
		
if __name__ == '__main__':
	main()