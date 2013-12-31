'''
Created on Dec 16, 2012

@author: Mike
'''

if __name__ == '__main__':
    f = open("DNA.txt")
    sequence = f.readline()
    Acount = sequence.count("A")
    Ccount = sequence.count("C")
    Gcount = sequence.count("G")
    Tcount = sequence.count("T")
    print str(Acount) + " " + str(Ccount) + " " + str(Gcount) + " " + str(Tcount)
        