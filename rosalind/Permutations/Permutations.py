'''
Created on Dec 18, 2012

@author: Mike
'''

import math

def permute(n):
    if n == 1:
        return [[1]]
    permutations = []
    for item in permute(n-1):
        for i in range(0, n):
            new_item = item[:i] + [n] + item[i:]
            permutations.append(new_item)
    return permutations
            

if __name__ == '__main__':
    
    num = 5
    
    print math.factorial(num)
    for p in permute(num):
        print " ".join([str(q) for q in p])
    

    

# Think optimal substructure for this problem.
        