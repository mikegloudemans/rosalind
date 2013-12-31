'''
Created on May 12, 2013

@author: Mike
'''

if __name__ == '__main__':
    f = open("data.txt")
    N = int(f.readline().strip())
    seq = f.readline().strip()
    CG_content = [float(num) for num in f.readline().strip().split()]
    f.close()
    
    expectations = []
    for cont in CG_content:
        prob = 1
        for char in seq:
            if char == 'C' or char == 'G':
                prob *= (cont/2)
            else:
                prob *= ((1-cont)/2)
        
        expected = prob*(N-len(seq)+1)
        print expected,
        expectations.append(expected)