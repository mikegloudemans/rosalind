'''
Created on Jan 22, 2013

@author: Mike
'''

def inferRNA(protein):
    numRNAs = {"F": 2, "L": 6, "I": 3, "M": 1, "V": 4, "S": 6, "P": 4, "T": 4, "A": 4, "Y": 2, 
               "H": 2, "Q": 2, "N": 2, "K": 2, "D": 2, "E": 2, "C": 2, "W": 1, "R": 6, "G": 4}
    
    possible = 1
    for char in protein:
        possible = (numRNAs[char] * possible) % 1000000 
    possible = (possible * 3) % 1000000  # Take stop codon into account.
    
    return possible

if __name__ == '__main__':
    f = open("data.txt")
    protein = f.readline().strip();
    print inferRNA(protein);