'''
Created on Dec 21, 2012

@author: Mike
'''

def words(n, alphabet):
    if n == 1:
        return alphabet
    else:
        word_list = []
        for letter in alphabet:
            for word in words(n-1,alphabet):
                word_list.append(letter + word)
        return word_list

if __name__ == '__main__':
    f = open("Alphabet.txt")
    alphabet = f.readline().split()
    k = int(f.readline())
    print "\n".join(words(k, alphabet))