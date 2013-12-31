'''
Created on Dec 18, 2012

@author: Mike

'''

import operator

if __name__ == '__main__':
    f = open("Sequence.txt")
    current_seq = ''
    total_nucs = 0
    GC = 0
    all_seqs = {}
    for line in f:
        if line.startswith('>'):
            if current_seq != '':
                all_seqs[current_seq] = GC*100.0/total_nucs
            current_seq = line[1:].strip()
            total_nucs = 0
            GC = 0
        else:
            for char in line:
                if char == 'A' or char == 'T':
                    total_nucs += 1
                elif char == "C" or char == "G":
                    total_nucs += 1
                    GC += 1
    all_seqs[current_seq] = GC*100.0/total_nucs
    print all_seqs
    
seqs = sorted(all_seqs.items(), reverse = True, key = operator.itemgetter(1))
print seqs[0][0], "\n", str(seqs[0][1]) + "%"