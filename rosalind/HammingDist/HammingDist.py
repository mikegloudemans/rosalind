'''
Created on Dec 18, 2012

@author: Mike
'''

if __name__ == '__main__':
    f = open('Seqs.txt')
    seq1 = f.readline().strip()
    seq2 = f.readline().strip()
    
    dist = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            dist += 1
            
    print dist