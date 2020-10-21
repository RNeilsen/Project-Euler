"""Finds the numerator of the largest fraction strictly less than NUM/DEN,
with a denominator less than or equal to UBOUND"""

from sympy import fraction
from math import floor
from time import time

UBOUND = 10**6
NUM = 3
DEN = 7

def main():
	n = 0
	bestn = 0
	bestd = 1
	for d in range(UBOUND+1):
		# if we can increment n without passing NUM/DEN, do so
		if DEN*(n+1) < NUM*d:
			n += 1
			
		# Check if this fraction is closer to NUM/DEN than bestn/bestd
		if bestn*d < bestd*n:
			(bestn,bestd) = (n,d)
	
	print(bestn, " / ", bestd)
		
if __name__ == '__main__':
	main()