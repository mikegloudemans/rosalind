'''
Created on Jan 21, 2013

@author: Mike
'''

if __name__ == '__main__':
    
    # Count number of appearances of each base in each position
    f = open("data.txt")
    bases = ["A", "C", "G", "T"]
    motifs = []
    for line in f:
        motifs.append(line.strip())
    baseCounts = []
    for i in range(len(motifs[0])):
        position = []
        for j in range(len(bases)):
            count = 0
            for k in range(len(motifs)):
                if motifs[k][i] == bases[j]:
                    count += 1
            position.append(count)
        baseCounts.append(position)
    
    # Display consensus sequence.
    
    consensus = ""
    for column in baseCounts:
        maxCount = max(column)
        consensus += bases[column.index(maxCount)]
    print consensus
    
    for i in range(len(bases)):
        newLine = bases[i] + ": "
        for j in range(len(motifs[0])):
            newLine += str(baseCounts[j][i]) + " "
        print newLine.strip()