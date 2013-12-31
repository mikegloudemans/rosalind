'''
Created on Mar 8, 2013

@author: Mike
'''

# NOTE: See the Rosalind website for an elegant method that solves this problem with a 4-line function.

if __name__ == '__main__':

    months = 100
    lifespan = 16
    
    wabbitNums = [1,1]
    born = [1,0]
    
    for i in range(2,months):
        # Set born[i]
        born.append(wabbitNums[i-2])
        if (i > lifespan):
            born[i] -= born[i-lifespan-1]
        
        # Set wabbitNums[i]
        wabbitNums.append(wabbitNums[i-1] + born[i])
        if (i >= lifespan):
            wabbitNums[i] -= born[i-lifespan]

    print wabbitNums[months-1]