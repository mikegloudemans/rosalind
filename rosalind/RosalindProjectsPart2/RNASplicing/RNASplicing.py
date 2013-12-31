'''
Created on Mar 9, 2013

@author: Mike
'''

import re

def getSeqWithExons(filename):
    f = open(filename)
    f.readline()
    mySeq = ""
    nextSeq = f.readline()
    while not nextSeq.startswith(">"):
        mySeq += nextSeq.strip()
        nextSeq = f.readline()
    
    introns = []
    currentSeq = ""
    for line in f:
        if line.startswith(">"):
            introns.append(currentSeq)
            currentSeq = ""
            continue
        else:
            currentSeq += line.strip()
    introns.append(currentSeq)
    
    print mySeq
    print introns
    
    return (mySeq, introns)

def rev_comp(sequence):
    init = ["A", "C", "G", "T"]
    final = ["T", "G", "C", "A"]
    sequence = sequence[::-1]
    seq2 = ""
    for i in range(len(sequence)):
        seq2 += final[init.index(sequence[i])]
    return seq2

def splice(sequence, introns):
    for intron in introns:
        index = sequence.find(intron)
        while index != -1:
            sequence = sequence[:index] + sequence[index+len(intron):]
            index = sequence.find(intron)
    return sequence

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
    return None

def transcribe(sequence):
    transcript = ''
    for letter in sequence:
        if letter == "T":
            transcript += "U"
        else:
            transcript += letter
    return transcript

if __name__ == '__main__':
    data = getSeqWithExons("data.txt")
    sequence = data[0]
    introns = data[1]
    
    rev = rev_comp(sequence)
    
    spl1 = transcribe(splice(sequence, introns))
    spl2 = transcribe(splice(rev, introns))
    
    ind1 = spl1.find("AUG")
    if ind1 != -1:
        prot1 = translate(spl1[ind1:])
        if prot1:
            print prot1
        
#    print spl2
#    ind2 = spl2.find("AUG")
#    if ind2 != -1:
#        prot2 = translate(spl2[ind2:])
#        if prot2:
#            print prot2
    
            