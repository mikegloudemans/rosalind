'''
Created on May 11, 2013

@author: Mike

Solution to the Rosalind problem "Error Correction in Reads"

'''

def rev_comp(sequence):
    init = ["A", "C", "G", "T"]
    final = ["T", "G", "C", "A"]
    sequence = sequence[::-1]
    seq2 = ""
    for i in range(len(sequence)):
        seq2 += final[init.index(sequence[i])]
    return seq2

def oneDifference(word1, word2):
    # Returns true if two words have exactly one or zero different letters between them.
    diffs = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diffs += 1
            if diffs > 1:
                return False
    
    return diffs == 1

if __name__ == '__main__':
    
    # Parse file
    f = open("data.txt")
    seqs = []
    for line in f:
        if line.startswith(">"):
            continue
        seqs.append(line.strip())
        
    # Count number of appearances of each sequence and its reverse complement
    seqCounts = {}
    for s in seqs:
        if s in seqCounts.keys():
            seqCounts[s] += 1
        elif rev_comp(s) in seqCounts.keys():
            seqCounts[rev_comp(s)] += 1
        else:
            seqCounts[s] = 1
    
#    print seqCounts
    
    # Determine which reads must be corrected
    corrections = {}
    for s1 in seqCounts.keys():
        if seqCounts[s1] != 1:
            continue
        else:
            for s2 in seqCounts.keys():
                if (oneDifference(s1,s2) and seqCounts[s2] > 1):
                    corrections[s1] = s2
                    break
                if (oneDifference(rev_comp(s1),s2) and seqCounts[rev_comp(s1)] > 1):
                    corrections[s1] = rev_comp(s2)
                    break
                    
    # Print output in proper format
    for s in corrections.keys():
        print s + "->" + corrections[s]
        