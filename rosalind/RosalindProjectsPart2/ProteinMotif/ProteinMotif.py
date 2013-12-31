'''
Created on Mar 8, 2013

@author: Mike
'''

import re

from Bio import ExPASy
from Bio import SwissProt

if __name__ == '__main__':
    f = open("data.txt")
    proteins = [line.strip() for line in f]
    
    pattern = "(N)(?!P).[ST](?!P)."
    
    for p in proteins:
        handle = ExPASy.get_sprot_raw(p)
        record = SwissProt.read(handle)
        seq = record.sequence
        
        starts = []
        
        for i in range(len(seq)-3):
            if re.match(pattern, seq[i:i+4]):
                starts.append(str(i+1))
                
        if starts != []:
            print p
            print (" ").join(starts)
        
        
#        locs = re.finditer(pattern, seq)
#        
#        if locs:
#            for l in locs:
#                starts.append(str(l.start()+1))
#                    
#            print (" ").join(starts)
#        