"""This program finds the maximal sum over all downward-stepping paths
through a  triangle of numbers, presented as a space-delimeted text file
with each row on a separate line"""

infile = "p067_smalltri.txt"
infile = "p067_triangle.txt"

def main():
	triangle = getinput(infile)
	triangle.reverse()
	maxsums = triangle
	
	# iterates through the triangle bottom-up, taking the best possible
	# sum from each of the two entries below and adding the entry on
	# this row (the triangle is reversed so this works 'forward' instead of
	# 'backwards')
	for i in range(1, len(triangle)):
		for j in range(len(maxsums[i])):
			maxsums[i][j] = (triangle[i][j]
					+ max(maxsums[i-1][j], maxsums[i-1][j+1]))
	print(maxsums[-1][0])
		

def getinput(p):
	"""takes a text file consisting of lines of space-separated integers,
	and returns as a list of lists of ints"""
	f = open(p)
	list = []
	for line in f:
		list.append([int(x) for x in line[:-1].split(' ')])
	f.close()
	return list
	
if __name__ == '__main__':
	main()