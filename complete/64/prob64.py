"""This module finds how many continued fractions for sqrt(N) with N <= MAXN
have an odd period. 

Warning: very inefficient, takes ~10 min for MAXN = 10000"""

MAXN = 10000

from sympy.ntheory.continued_fraction import continued_fraction_periodic

def main():
	# generate a list of square numbers to skip for convenience
	n = 1
	squares = set()
	while n**2 <= MAXN:
		squares.add(n**2)
		n+=1 
	
	N = 1
	count = 0
	
	while N <= MAXN:
		if N not in squares:
			if len(continued_fraction_periodic(0,1,N)[1]) % 2 == 1:
				count += 1
				# print(N, "counted")
			# else:
				#print(N, "not counted")
		N += 1
	
	print(count)

if __name__ == '__main__':
	main()