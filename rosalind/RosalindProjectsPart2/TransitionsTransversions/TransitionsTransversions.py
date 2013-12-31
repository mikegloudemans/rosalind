'''
Created on May 11, 2013

@author: Mike
'''

def transversion_transition_ratio(s1,s2):
    transversions = 0
    transitions = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            continue
        if (s1[i] == "G" and s2[i] == "A") or (s1[i] == "A" and s2[i] == "G") or \
            (s1[i] == "C" and s2[i] == "T") or (s1[i] == "T" and s2[i] == "C"):
            transitions += 1
            continue
        transversions += 1
        
    return transitions*1.0/transversions
        

if __name__ == '__main__':
    
    f = open("data.txt")
    f.readline()
    seq1 = ""
    for line in f:
        if line.strip().startswith(">"):
            break
        seq1 += line.strip()
    
    seq2 = ""
    for line in f:
        if line.strip() == "":
            break
        seq2 += line.strip()
    
    print transversion_transition_ratio(seq1, seq2)