'''
Created on Jan 24, 2013

@author: Mike
'''

import numpy

def readFile(filename):
    f = open(filename)
    sequences = []
    currentSeq = ""
    for line in f:
        if line.startswith(">"):
            if currentSeq != "":
                sequences.append(currentSeq)
                currentSeq = ""
        if not line.startswith(">"):
            currentSeq += line.strip()
    sequences.append(currentSeq)
    return sequences

def pairwiseDists(sequences):
    num = len(sequences)
    dists = numpy.zeros((num,num))
    for i in range(len(sequences)):
        for j in range(i+1, len(sequences)):
            similarity = compare(sequences[i], sequences[j])
            dists[i][j] = similarity
            dists[j][i] = similarity
    return dists
            
def compare(seq1, seq2):
    # Assumes that sequences are the same length
    diff = 0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
            diff += 1
    return diff*1.0/len(seq1)
            
            
if __name__ == '__main__':
    sequences = readFile("data.txt")
    distances = pairwiseDists(sequences)
    for row in distances:
        for num in row:
            print num, "\t",
        print "\n",