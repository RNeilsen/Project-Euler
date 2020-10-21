"""This module finds the value of D less than or equal to ubound, that has 
the largest minimal solution x to the Diophantine equation x^2 - Dy^2 = 1 

We do this, for each D, by incrementing y and testing 1 + Dy^2 to find a
value that is a square. When we do, its square root is our minimal value
of x."""

import math

ubound = 100

def main():
	# Create a Dlist of all non-square D values up to ubound
	Dlist = list(range(2,ubound+1))
	for n in range(2, 1 + math.floor(math.sqrt(ubound))):
		Dlist.remove(n*n)

	for D in Dlist:
		n = 2
		lowsquare = (n-1)**2
		highsquare = n**2
		
		y = 1
		lasty = str(y)
		xsq = 1 + D*(y**2)
		
		cont = True
		while cont:
			while xsq > highsquare:
				dbstr = (lowsquare, highsquare)
				n += 1
				lowsquare = highsquare
				highsquare = (n)**2
				if len(str(y)) > len(lasty):
					print("Resquaring on D =", D, ", y =", y)
					lasty = str(y)
			if xsq == highsquare:
				cont = False
			else:
				y += 1
				xsq = 1 + D*(y**2)
			
		print("(D,x) =", (D, n))
			
			
		
if __name__ == '__main__':
	main()