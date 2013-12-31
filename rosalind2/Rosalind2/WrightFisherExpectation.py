'''
Created on Dec 12, 2013

@author: Michael
'''

if __name__ == '__main__':
    n = int(raw_input().strip())
    data = [float(r) for r in raw_input().strip().split()]
    
    for d in data:
        print n * d,