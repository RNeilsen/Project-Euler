# Prob53 for Project Euler
# by Richard Neilsen

import sympy

def main():
	count = 0
	for n in range(101):
		target = factorial(n) // 1000000
		for r in range(n):
			if factorial(r) * factorial(n-r) <= target: count += 1
	print(count)
			

def factorial(n):
	f = 1
	for i in range(1, n+1):
		f *= i
	return f
	
if __name__ == '__main__':
	main()