'''
Created on Jan 21, 2013

@author: Mike
'''

def combine(read1, read2, max_overlap):
    # Return combined reads if they are combinable, otherwise return null.
    for i in range(max_overlap, max_overlap/2, -1):
        if adjacent(read1, read2, i):
            new_sequence = read1 + read2[i:]
            #print read1, read2, new_sequence
            return new_sequence
    return 0

def adjacent(seq1, seq2, k):
    if seq2[0:k] == seq1[len(seq1)-k:]:
        return True
    else:
        return False

if __name__ == '__main__':
    f = open("data.txt")
    reads = []
    for line in f:
        reads.append(line.strip())
    f.close()
        
    max_overlap = len(reads[0])
    
    while (len(reads)>1):
        for i in range(len(reads)):
            comboFound = False
            for j in range(len(reads)):
                if i == j:
                    continue
                combined = combine(reads[i],reads[j], max_overlap)
                if combined == 0:
                    continue
                else:
                    seq1 = reads[i]
                    seq2 = reads[j]
                    reads.remove(seq1)
                    reads.remove(seq2)
                    reads.append(combined)
                    comboFound = True
                    break
            if comboFound == True:
                break
    
    w = open("assembly.txt", 'w')
    w.write(reads[0])
    print reads[0]
    w.close()
                    