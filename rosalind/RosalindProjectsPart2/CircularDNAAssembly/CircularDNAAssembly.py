'''
Created on May 11, 2013

@author: Mike
'''

if __name__ == '__main__':
    f = open("data.txt")
    reads = []
    for line in f:
        reads.append(line.strip())
        
    k = len(reads[0])
    
    while len(reads) > 1:
        for i in range(1,len(reads)):
            r = reads[i]
            if reads[0].endswith(r[:len(r)-1]):
                reads[0] = reads[0] + r[len(r)-1]
                reads.remove(r)
                break
            
    print reads[0][:len(reads)-k]