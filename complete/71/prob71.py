"""Finds the numerator of the largest fraction strictly less than NUM/DEN,
with a denominator less than or equal to UBOUND"""

from sympy import fraction
from math import floor
from time import time

UBOUND = 10**6
NUM = 3
DEN = 7

def main():
	starttime = time()
	bestn = 0
	bestd = 1
	for d in [i for i in range(1, UBOUND) if i != 7]:
		n = floor(NUM * d / DEN)
		if n * bestd > bestn * d:
			# Include some code to reduce the fraction n / d here!
			(bestn, bestd) = (n, d)
			print("New best fraction:", n, "/", d, "in", time() - starttime, "seconds")
	print(bestn, "in", time() - starttime, "seconds.")
		
if __name__ == '__main__':
	main()