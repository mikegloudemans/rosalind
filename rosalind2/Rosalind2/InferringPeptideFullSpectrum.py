'''
Created on Dec 13, 2013

@author: Michael
'''

import math

if __name__ == '__main__':
    
    weightMap = {"A": 71.03711, "C" : 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
             "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
             "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}
    
    f = open("data.txt")
    
    total_mass = float(f.readline().strip())
    
    ions = []
    
    while True:
        try:
            ions.append(float(f.readline().strip()))
        except:
            break
    
    print ions
    
    last1 = ions[0]
    ions.remove(last1)
    for ion in ions:
        if abs(total_mass - last1 - ion) < 0.001:
            ions.remove(ion)
    protein = ""
    while ions != []:
        for i in range(1,len(ions)):
            found = False
            for aa in weightMap.keys():
                if abs(ions[i]-last1-weightMap[aa]) < 0.001:
                    protein += aa
                    last1 = ions[i]
                    ions.remove(last1)
                    for ion in ions:
                        if abs(total_mass - last1 - ion) < 0.001:
                            ions.remove(ion)
                    found = True
                    print protein, last1
                    break
            if found:
                break
    
    print protein
        