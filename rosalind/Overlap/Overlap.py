'''
Created on Jan 21, 2013

@author: Mike
'''

def adjacent(seq1, seq2, k):
#    print seq2[0:k], seq1[len(seq1)-k:]
    if seq2[0:k] == seq1[len(seq1)-k:]:
        return True
    else:
        return False

if __name__ == '__main__':
    # Read in data
    f = open("data.txt")
    currentSeq = ""
    dSeqs = {}
    seqContent = ""
    for line in f:
        if line.startswith(">"):
            if seqContent != "":
                dSeqs[currentSeq] = seqContent
                seqContent = ""
            currentSeq = line[1:].strip()
        else:
            seqContent += line.strip()
    dSeqs[currentSeq] = seqContent
    
#    print dSeqs
            
    for seq1 in dSeqs.keys():
        for seq2 in dSeqs.keys():
#            print seq1, seq2
            if seq1 == seq2:
                continue
            if adjacent(dSeqs[seq1], dSeqs[seq2], 3):
                print seq1 + " " + seq2

            