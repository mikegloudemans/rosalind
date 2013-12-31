'''
Created on Dec 16, 2012

@author: Mike
'''

if __name__ == '__main__':
    f = open("DNA.txt")
    sequence = f.readline()
    transcript = ''
    for letter in sequence:
        if letter == "T":
            transcript += "U"
        else:
            transcript += letter
    print transcript
            