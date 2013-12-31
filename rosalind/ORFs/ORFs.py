'''
Created on Jan 22, 2013

@author: Mike
'''

import re

# TODO: NOTE: Many of the functions in this code were taken from other programs from the Rosalind series. In the future, I should
# learn how to import these functions, or set up a module with useful functions for later use!

def getAminoAcid(codon):
    regexes = ['uu[uc]', '(uu[ag])|(cu.)', 'au[acu]', 'aug', 'gu.', '(uc.)|(ag[uc])',
               'cc.', 'ac.', 'gc.', 'ua[uc]', '(ua[ag])|(uga)','ca[uc]','ca[ag]', 'aa[uc]',
               'aa[ag]', 'ga[uc]', 'ga[ag]', 'ug[uc]', 'ugg', '(cg.)|(ag[ag])',
               'gg.']
    aminoAcids = ['F', 'L', 'I', 'M', 'V', 'S', 'P', 'T', 'A', 'Y', 'stop', 'H', 'Q', 'N', 'K',
                  'D', 'E', 'C', 'W', 'R', 'G']
    for i in range(len(regexes)):
        p = re.compile(regexes[i])
        if p.match(codon.lower()):
            return aminoAcids[i]
            

def translate(seq):
    protein = ""
    for i in range(0,len(seq)-2,3):
        codon = seq[i:i+3]
        nextAA = getAminoAcid(codon)
        if nextAA == 'stop':
            return protein
        protein += nextAA
    return None

def makeRNA(sequence):
    dNucs = {"A": "U", "C": "G", "G": "C", "T": "A"}
    return "".join(map(dNucs.get, sequence))[::-1]

def revComp(sequence):
    dNucs = {"A": "U", "C": "G", "G": "C", "U": "A"}
    return "".join(map(dNucs.get, sequence))[::-1]
    
def findORFs(sequence, proteins):
    for i in range(len(sequence)-2):
        if sequence[i:i+3] == "AUG":
            newProt = translate(sequence[i:])
            if newProt != None and not(newProt in proteins):
                print newProt
                proteins.append(newProt)
    return proteins
    
    

if __name__ == '__main__':
    f = open("data.txt")
    sequence = f.readline().strip()
    RNA = makeRNA(sequence)
#    print RNA
#    print revComp(RNA)
    proteins = findORFs(RNA,[])
    findORFs(revComp(RNA),proteins)