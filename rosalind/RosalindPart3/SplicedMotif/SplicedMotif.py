'''
Created on Jul 15, 2013

@author: Mike
'''

# NOTE: After looking at how other people did this problem,
# the way I did it is a bit foolish. It's much easier to just
# take the first letter that appears as a match to the motif.

def find_next_letter(sequence, startIndex, motifIndex, motif):
    # Recursive function to find position of next letter in motif
    
    if motifIndex + 1 > len(motif):
        return []
    if startIndex > len(sequence):
        return False
    
    for i, base in enumerate(sequence[startIndex:]):
#        print motifIndex
#        print motif[motifIndex]
#        print base
        if base == motif[motifIndex]:
            result = find_next_letter(sequence, startIndex + i + 1, motifIndex + 1, motif)
            if result != False:
                return [startIndex + i + 1] + result
    
    return False

if __name__ == '__main__':
    # Parse file
    f = open("data.txt")
    f.readline()
    seq = ""
    for line in f:
        if line.startswith(">"):
            break
        seq += line.strip()
    motif = ""
    for line in f:
        motif += line.strip()
        
    for index in find_next_letter(seq, 0, 0, motif):
        print index,
    