'''
Created on May 12, 2013

@author: Mike
'''

import math

def nCr(N, k):
    return (math.factorial(N)/(math.factorial(k)*math.factorial(N-k)))

if __name__ == '__main__':
    N = 1862
    k = 1223
    
    result = 0
    while (k <= N):
        result = (result + nCr(N,k))%1000000
        k += 1
    
    print result