'''
Created on Jul 14, 2013

@author: Mike
'''

import math

if __name__ == '__main__':
    
    # Parse file
    f = open("data.txt")
    seq = ""
    for line in f:
        if line.startswith(">"):
            continue
        seq = seq + line.strip()
        
    # Count appearances
    ATpairs = 0
    CGpairs = 0
    
    for base in seq:
        if base == "A":
            ATpairs += 1
        if base == "C":
            CGpairs += 1
            
    print seq    
    print math.factorial(ATpairs) * math.factorial(CGpairs)
    