"""This module determines how many n-digit numbers are also n-th powers.
Known upper bound is 900: 

- 10^n always has n+1 digits so only 1-9 are valid bases
- 9^100 has fewer than 100 digits

Thus we need only consider b^n for b in 1..9 and n in 1..100"""

def main():
	count = 0
	for b in range(1,10):
		for n in range(1,101):
			bn = b**n
			if len(str(bn)) == n:
				count += 1
				
	print(count)

if __name__ == '__main__':
	main()