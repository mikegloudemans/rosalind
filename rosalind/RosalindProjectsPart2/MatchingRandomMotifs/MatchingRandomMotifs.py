'''
Created on May 12, 2013

@author: Mike
'''

if __name__ == '__main__':
    f = open("data.txt")
    data = f.readline().strip().split()
    N = int(data[0])
    CG_content = float(data[1])
    seq = f.readline().strip()
    f.close()
    
    prob = 1
    for char in seq:
        if char == 'C' or char == 'G':
            prob *= (CG_content/2)
        else:
            prob *= ((1-CG_content)/2)
    
    print 1-((1-prob)**N)