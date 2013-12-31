'''
Created on Jul 24, 2013

@author: Mike
'''

if __name__ == '__main__':
    f = open("data.txt")
    set1 = [float(i) for i in f.readline().strip().split()]
    set2 = [float(i) for i in f.readline().strip().split()]
    f.close()
    
    # Establish spectral convolution
    spec_conv = []
    for peak1 in set1:
        for peak2 in set2:
            spec_conv.append(peak1-peak2)
    spec_conv.sort()
    # Find multiplicity of most common element in spectral convolution
    spec_conv = [round(i,6) for i in spec_conv]
    
    
    counts = [spec_conv.count(elem) for elem in spec_conv]
    max_mult = max(counts)
    print max_mult
    print spec_conv[counts.index(max_mult)]