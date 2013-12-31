'''
Created on Dec 19, 2012

@author: Mike
'''

import math

if __name__ == '__main__':
    f = open("Genome.txt")
    seq = f.readline()
    GC = [float(n) for n in f.readline().split()]
    probs = []
    for num in GC:
        p = 0
        for base in seq:
            if base == "G" or base == "C":
                p += math.log10(num/2)
            if base == "T" or base == "A":
                p += math.log10((1-num)/2)
        probs.append(p)
    print " ".join([str(item) for item in probs])