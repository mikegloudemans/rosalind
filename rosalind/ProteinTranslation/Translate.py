'''
Created on Jan 22, 2013

@author: Mike Gloudemans
'''

import re

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
    for i in range(0,len(seq),3):
        codon = seq[i:i+3]
        nextAA = getAminoAcid(codon)
        if nextAA == 'stop':
            return protein
        protein += nextAA
    return protein

def transcribe(sequence):
    transcript = ''
    for letter in sequence:
        if letter == "T":
            transcript += "U"
        else:
            transcript += letter
    return transcript

if __name__ == '__main__':
    f = open("sequence.txt")
    sequence = f.readline().strip()
    protein = translate(sequence)
    
    print protein
    
    w = open("results.txt", "w")
    w.write(protein)
    w.close()