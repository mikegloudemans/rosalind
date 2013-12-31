'''
Created on May 12, 2013

@author: Mike
'''

import math

def nCr(N, k):
    return (math.factorial(N)/(math.factorial(k)*math.factorial(N-k)))

if __name__ == '__main__':
    n = 47
    
    probs = []
    
    cmprob = 0.0
    for i in range(0,2*n):
        prob = (0.5)**(2*n) * nCr(2*n, i)
        cmprob += prob
        probs.append(math.log10(1-cmprob))
        
    w = open("results.txt", "w")
    for p in probs:
        w.write(str(round(p,3)) + " ")
        print round(p,3),
    