'''
Created on Jan 24, 2013

@author: Mike
'''

def getWords(alphabet, length):
    if length == 0:
        return [""]
    words = []
    for letter in alphabet:
        words.extend([letter + word for word in getWords(alphabet, length-1)])
    return [""] + words

if __name__ == '__main__':
    f = open("data.txt")
    alphabet = f.readline().strip().split()
    wordLength = int(f.readline().strip())
    for word in getWords(alphabet, wordLength)[1:]:
        print word