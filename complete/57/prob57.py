"""This module finds how many of the first elements in this sequence converging 
to sqrt2 have a numerator with more decimal digits than the denominator:
sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + 1/(2 + ...))))"""

maxiters = 1000

def main():
    n = 1
    count = 0
    num = 1
    den = 2
    while n < maxiters:
        if len(str(num+den))>len(str(den)):
            print(num, "/", den)
            count += 1
        num += 2*den
        (num,den) = (den,num)
        n += 1
    print(count)
    

if __name__ == '__main__':
    main()
