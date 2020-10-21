"""This module finds the sum of the digits in the numerator of the Nth
convergent of the continued fraction for Euler's constant e"""

N = 100

from sympy.ntheory.continued_fraction import continued_fraction_reduce

def main():
	l = [i for i in [[1, 2*n, 1] for n in range(1,N//3 + 2)]]
	l = ([2] + sum(l, []))  # flatten list
	
	num = continued_fraction_reduce(l[:N]).p
	print(sum([int(c) for c in str(num)]))	
	
if __name__ == '__main__':
	main()