'''
Created on May 11, 2013

@author: Mike
'''

import scipy.misc as sm

if __name__ == '__main__':
    k = 6
    N = 17
    
    prob = 0
    for i in range(N, 2**k + 1):
        prob += sm.comb(2**k, i) * ((1.0/4)**i) * ((3.0/4)**(2**k-i))
        
    print prob