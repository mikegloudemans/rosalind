'''
Created on Dec 13, 2013

@author: Michael
'''

lookup = {}

def find_total_matchings(seq):
    
    if seq in lookup.keys():
        return lookup[seq]
    
    if len(seq) == 0:
        return 1
    
    if len(seq) == 2:
        pairings = 2 if "ACGU".index(seq[0]) == "UGCA".index(seq[1]) else 1
        lookup[seq] = pairings
        return pairings
    
    pairings = 0
    for i in range(1,len(seq)):
        pairings_to_add = (find_total_matchings(seq[1:i]) * find_total_matchings(seq[i+1:]))
        if "ACGU".index(seq[0]) == "UGCA".index(seq[i]):
            pairings_to_add *= 2
        print i, pairings_to_add, seq
        pairings += pairings_to_add
    
    lookup[seq] = pairings   
    return pairings % 1000000
    

if __name__ == '__main__':
    f = open("data.txt")
    
    f.readline()
    seq = f.readline().strip()
    
    print find_total_matchings(seq)
        