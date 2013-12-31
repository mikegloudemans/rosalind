'''
Created on May 11, 2013

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
    # Parse sequence reads
    f = open("data.txt")
    allReads = []
    for line in f:
        allReads.append(line.strip())
        allReads.append(rev_comp(line.strip()))
        
    # Assemble adjacency graph
    dAdj = {}
    for read in allReads:
        if read[0:len(read)-1] in dAdj.keys():
            if read[1:] in dAdj[read[0:len(read)-1]]:
                continue
            else:
                dAdj[read[0:len(read)-1]].append(read[1:])
        else:
            dAdj[read[0:len(read)-1]] = [read[1:]]
    
    # Print adjacencies
    for key in dAdj.keys():
        for adj in dAdj[key]:
            print "(" + key + ", " + adj + ")"