# Prob52 of Project Euler
# By Richard Neilsen

def main():
	n = 1
	cont = True
	
	while cont:
		x = 10**n
		n += 1
		while 6*x < 10**n:
			digits = sorted(str(x))
			valid = True
			for i in range(2,7):
				if sorted(str(x*i)) != digits:
					valid = False
			if valid:
				print(x, 2*x, 3*x, 4*x, 5*x, 6*x)
				cont = False
				break
			else:
				x += 1
	
	
if __name__ == '__main__':
    main()