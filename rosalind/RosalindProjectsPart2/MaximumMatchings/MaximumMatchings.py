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
    Acount = 0
    Ccount = 0
    Gcount = 0
    Ucount = 0
    
    for base in seq:
        if base == "A":
            Acount += 1
        if base == "C":
            Ccount += 1
        if base == "G":
            Gcount += 1
        if base == "U":
            Ucount += 1
            
    print seq    
    
    matchings = 1
    
    if Acount >= Ucount:
        matchings *= math.factorial(Acount) / math.factorial(Acount-Ucount)
    else:
        matchings *= math.factorial(Ucount) / math.factorial(Ucount-Acount)
        
    if Ccount >= Gcount:
        matchings *= math.factorial(Ccount) / math.factorial(Ccount-Gcount)
    else:
        matchings *= math.factorial(Gcount) / math.factorial(Gcount-Ccount)
        
    print matchings
    