"""This module finds the value of D less than or equal to UBOUND, that has 
the largest minimal solution x to the Diophantine equation x^2 - Dy^2 = 1 """

import sympy

UBOUND = 65
numsquares = UBOUND
squares = set((n*n for n in range(1,numsquares)))

def main():
	minx = []
	for D in range(1,UBOUND):
		if not issquare(D):
			# print("Trying D =", D)
			y = 1
			while not issquare(1 + D*y*y):
				# print("Not square:", 1 + D*y*y)
				y += 1
			# print("(D,x) =", (D, sympy.sqrt(1+D*y*y)))
			minx.append((D,sympy.sqrt(1 + D*y*y)))
	print(minx)
	
	
def issquare(n):
	global numsquares, squares
	while n >= numsquares**2:
		print("Extending squares:", numsquares, "->", numsquares*2)
		squares = squares.union((i*i for i in range(numsquares, 2*numsquares)))
		numsquares *= 2
	return (n in squares)

		
if __name__ == '__main__':
	main()