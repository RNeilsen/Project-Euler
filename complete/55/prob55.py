"""This module determines how many Lychrel numbers there are that are less than
ten thousand."""

#Project Euler problem 55, by Richard Neilsen

#note: for higher limits the bound on iterations permitted will be higher
limit = 10000
maxiters = 50

def main():
    nLychrel = 0
    for n in range(limit):
        cont = True
        numiters = 0
        i = n
        while cont:
            numiters += 1
            i += reverse(i)
            if ispalindrome(i):
                cont = False
            elif numiters > 50:
                nLychrel += 1
                cont = False
    print(nLychrel)

def reverse(n):
    return int(str(n)[::-1])
    
def ispalindrome(n):
    return n == reverse(n)
    
if __name__ == '__main__':
    main()