'''
Created on May 10, 2013

@author: Mike
'''
   
def longest_subseq(sequence):
    # Dynamic programming algorithm to find longest increasing subsequence.
    all_seqs = []
    for num in sequence:
        maxLength = 0
        longestSeq = []
        for s in all_seqs:
            if s[len(s)-1] < num and len(s) > maxLength:
                maxLength = len(s)
                longestSeq = s
        all_seqs.append(longestSeq + [num])
    
    bestLength = 0
    bestSubseq = []
    for s in all_seqs:
        if len(s) > bestLength:
            bestLength = len(s)
            bestSubseq = s
            
    return bestSubseq
        
    
if __name__ == '__main__':
    f = open("data.txt")
    numEntries = (int)(f.readline())
    data = f.readline()
    seq = []
    for d in data.split():
        seq.append(int(d))
    f.close()
    
#    print seq
    for num in longest_subseq(seq):
        print num,
    print
    
    seq.reverse()
    decreasing = longest_subseq(seq)
    decreasing.reverse()
    for num in decreasing:
        print num,
    print