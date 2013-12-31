'''
Created on Dec 21, 2012

@author: Mike
'''

# A simple alteration of the algorithm from the Permutations problem.

import math

def permute(n):
    if n == 1:
        return [[1], [-1]]
    permutations = []
    for item in permute(n-1):
        for i in range(0, n):
            new_item = item[:i] + [n] + item[i:]
            permutations.append(new_item)
            new_item_2 = item[:i] + [-n] + item[i:]
            permutations.append(new_item_2)
    return permutations
            

if __name__ == '__main__':
    
    num = 5
    
    permutations = permute(num)
        
    print len(permutations)
    for p in permutations:
        print " ".join([str(q) for q in p])
    