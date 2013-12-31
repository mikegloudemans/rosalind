'''
Created on Dec 18, 2012

@author: Mike
'''

if __name__ == '__main__':
    f = open("Seq.txt")
    seq = f.readline().strip()
    motif = f.readline().strip()
    
    locs = []
    for i in range(len(seq)-len(motif)+1):
        if seq[i:i+len(motif)]==motif:
            locs.append(str(i+1))
    
    print (' ').join(locs)
        