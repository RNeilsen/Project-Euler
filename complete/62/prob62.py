"""This module finds the smallest Pth power for which exactly N of its permutations
are also Pth powers"""

N = 5
P = 3

def main():
	n = 1
	size = 1
	while True:
		# construct a dict of cubes with size digits
		cubes = {}
		c = n**P
		while c < 10**size:
			counts = getdigitcount(c)
			# print(n, c, counts)
			if counts not in cubes:
				cubes[counts] = [c]
			else:
				cubes[counts].append(c)
			n += 1
			c = n**P
			
		for c in cubes.keys():
			if len(cubes[c]) == N:
				print(cubes[c])
				return

		size += 1
		
	
def getdigitcount(n):
	"""Outputs a 10-tuple counting the instances of each digit 0-9 
	in the decimal representation of n"""
	s = str(n)
	counts = [0 for i in range(10)]
	for d in range(10):
		counts[d] = s.count(str(d))
	return tuple(counts)

if __name__ == '__main__':
	main()