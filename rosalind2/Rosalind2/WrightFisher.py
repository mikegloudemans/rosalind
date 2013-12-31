'''
Created on Dec 11, 2013

@author: Michael
'''

import math

if __name__ == '__main__':
    data = [int(r) for r in raw_input().strip().split()]
    
    probs = [0.0]*(2*data[0] + 1)
    probs[data[1]] = 1.0
    
    #recessive_prob = (2*data[0] - data[1])*1.0/2*data[0]
    #print probs
    for i in range(data[2]):
        new_probs = [0]*len(probs)
        for j in range(len(probs)):
            for k in range(len(probs)):
                dom_prob = k*1.0/(2*data[0])
                next_prob = probs[k]*(dom_prob**j)*((1-dom_prob)**(2*data[0]-j))*(math.factorial(2*data[0])/math.factorial(2*data[0]-j)/math.factorial(j))
                new_probs[j] += next_prob
        probs = new_probs
        # print sum(probs)
        # print [round(n,4) for n in new_probs]
        
    print sum(probs[:len(probs)-data[3]])
    