"""This program finds the maximal 16-digit string that can be produced by
concatenating arms of a magic 5-gon, as described in Problem 68 of
Project Euler."""

from itertools import permutations

def main():
	highest = 0
	
	for perm in permutations([1,2,3,4,5,6,7,8,9]):
		# no point putting 10 in inner ring (16-digit only), so just try outer 5 nodes
		for i in range(5):
			p = list(perm[:i]) + [10] + list(perm[i:]) 
			
			if ismagic(p):
				n = int(stringify(p))
				if n > highest:
					highest = n
	
	print(highest)
	
def ismagic(list):
	"""Takes a list of 10 numbers and returns true or false
	depending on whether they form a magic 5-gon. Interprets as the outer,
	then inner rings."""
	# if len(list) != 10:
		# return False
	
	sum = list[4] + list[9] + list[5]
	for i in range(4):
		if list[i] + list[i+5] + list[i+6] != sum:
			return False
	
	return True

def stringify(list):
	restart = list.index(min(list[:5]))
	l = list[restart:5] + list[:restart] + list[restart+5:] + list[5:restart+5] + list[restart+5:]
	
	newl = []
	
	for i in range(5):
		newl += [l[i], l[i+5], l[i+6]]
	
	return int(''.join([str(n) for n in newl]))
	
	
		
if __name__ == '__main__':
	main()