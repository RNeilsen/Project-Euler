"""This program is designed to brute-force decrypt a text file, assuming the
plaintext includes standard English words and is encrypted with bitwise XOR"""

from operator import xor

keylength = 3
keydigitlb = 97
keydigitub = 122
infile = "p059_cipher.txt"

def main():
    cipher = getinput(infile)
    f = open('../engwords.txt','r')
    words = f.read().split('\n')
    f.close()
    # through analysis it was discovered that the key to p059_cipher.txt
    # is a = 103, b = 111, c = 100
    for a in range(103,104): #range(keydigitlb, keydigitub+1):
        for b in range(keydigitlb, keydigitub+1):
            for c in range(100,101): #range(keydigitlb, keydigitub+1):
                plain = [xor(cipher[n],[a,b,c][n%keylength]) 
                        for n in range(len(cipher))]
                s = ''.join(map(chr,plain))
                # preliminary check the first 3 'words'
                
                plainwords = s.split(' ')
                real = [x for x in plainwords if x in words]
                if len(real)> 30: print(sum(plain))

def getinput(p):
    """returns a comma-delimited text file as a list of ints"""
    f = open(p)
    list = []
    for line in f:
        list = list + line.strip().split(',')
    f.close()
    return [int(x) for x in list]
    
if __name__ == '__main__':
    main()