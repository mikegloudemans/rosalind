'''
Created on Dec 11, 2013

@author: Michael
'''

if __name__ == '__main__':
    nums = [float(r) for r in raw_input().strip().split()]

    for n in nums:
        print round(1-(n**2)-(1-n)**2,4),