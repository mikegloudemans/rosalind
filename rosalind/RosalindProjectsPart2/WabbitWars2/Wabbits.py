'''
Created on Mar 8, 2013

@author: Mike
'''

if __name__ == '__main__':
    months = 36
    fertility = 5
    
    wabbitNums = [1,1]
    for i in range(2,months):
        wabbitNums.append(wabbitNums[i-2]*fertility + wabbitNums[i-1])
    
    print wabbitNums[months-1]