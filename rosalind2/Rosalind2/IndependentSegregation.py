'''
Created on Dec 11, 2013

@author: Michael
'''
import math

if __name__ == '__main__':
    
    n = int(raw_input())
    
    nums = []
    for i in range(0, 2*n+1):
        nums.append(math.factorial(2*n)/math.factorial(2*n-i)/math.factorial(i))
        
    for i in range(1,len(nums)):
        print round(math.log10(sum(nums[i:])*1.0/sum(nums)),5),