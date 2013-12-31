'''
Created on Mar 5, 2013

@author: Mike
'''

from Bio import ExPASy
from Bio import SwissProt

if __name__ == '__main__':
    protein = 'Q9JT70'
    handle = ExPASy.get_sprot_raw(protein)
    record = SwissProt.read(handle)
    
    refs = [r for r in record.cross_references if "GO" in r]
    refs = [r[2] for r in refs if "P:" in r[2]]
    
    for r in refs:
        print r[2:]