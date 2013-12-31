'''
Created on Dec 19, 2012

@author: Mike
'''

def rev_comp(sequence):
    init = ["A", "C", "G", "T"]
    final = ["T", "G", "C", "A"]
    sequence = sequence[::-1]
    seq2 = ""
    for i in range(len(sequence)):
        seq2 += final[init.index(sequence[i])]
    return seq2

if __name__ == '__main__':
    f = open("Seq.txt")
    seq = f.readline().strip()
    f.close()
    
    for i in range(4,13):
        for j in range(len(seq)-i+1):
            subseq = seq[j:j+i]
            if subseq == rev_comp(subseq):
                print j+1,i
            