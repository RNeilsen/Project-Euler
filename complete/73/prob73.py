"""Finds the number of reduced proper fractions between ln/ld and un/ud
with denominators less than or equal to dbound"""

from sympy.core.numbers import igcd
from time import time

(ln,ld) = (1,3) 	# lower bound numerator & denominator
(un,ud) = (1,2)		# upper bound numerator & denominator
dbound = 12000		# largest allowable denominator

def main():
	lown = 1
	highn = 1
	count = 0
	for d in range(2,dbound+1):
		# while lown/d <= ln/ld, increase lown
		while lown * ld <= ln * d:
			lown += 1
		
		# while highn/d < un/ud, increase highn
		while highn * ud < un * d:
			highn += 1
		
		# print("d =", d, "(lown, highn) =", (lown, highn))
		
		s = ""
		# iterate n through lown -> highn and count coprimes of d
		for n in range(lown, highn):
			if igcd(n,d) == 1:
				count += 1
				s += str(n) + "/" + str(d) + " |"
		
		# print(d, ":", s)
	
	print(count)

		
if __name__ == '__main__':
	starttime = time()
	main()
	print("Completed in", time() - starttime)