"""This module finds an ordered cycle of N-2 4-digit numbers,
such that the last 2 digits of each are the first 2 digits
of the next, and such that each figurate (polygonal) number type
from triangular to N-gonal is represented by one element."""

N = 8

def main():
	figurates = [{}]
	
	# Next block constructs lists of figurate numbers
	# figurates[p] is a dict of the (p+2)-gonal numbers
	for p in range(1,N-1):
		n = 1
		figurates.append({})
		fig = 1
		while fig < 1000:
			fig = n*(p*n + 2 - p) // 2
			n += 1
		while fig < 10000:
			(first2, last2) = (fig // 100, fig % 100)
			if first2 not in figurates[p]:
				figurates[p][first2] = []
			if last2 >= 10 and first2 != last2 :
				# only include numbers w/o a third digit of 0
				figurates[p][first2].append(last2)
			fig = n*(p*n + 2 - p) // 2
			n += 1
	
	# WLOG can assume the first number in the set is N-gonal
	cycles = []
	for m in figurates[N-2].keys():
		for n in figurates[N-2][m]:
			cycles.append((set(range(1,N-2)),[m, n]))
	
	# 
	while len(cycles[0][0]) > 0:
		ptc = cycles[0][0] # polygons to cover
		cyc = cycles[0][1] # current cycle
		
		# run through the types this cycle has yet to cover
		for p in ptc:
			if cyc[-1] in figurates[p]:
				for last2 in figurates[p][cyc[-1]]:
					newptc = ptc - {p}
					newcyc = cyc + [last2]
					
					if newptc == set() and last2 == cyc[0]:
						sum = 0
						for n in range(len(newcyc)-1):
							sum += 100*(newcyc[n]) + newcyc[n+1]
						print(newcyc, sum)
						return
						
					cycles.append((newptc, newcyc))
		
		del cycles[0]
	
if __name__ == '__main__':
    main()