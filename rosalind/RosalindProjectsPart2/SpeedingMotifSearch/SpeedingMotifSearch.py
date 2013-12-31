'''
Created on May 12, 2013

@author: Mike
'''

if __name__ == '__main__':
    # Parse file
    f = open("data.txt")
    f.readline()
    seq = ""
    for line in f:
        seq += line.strip()
    
    failure_array = [0]         # The failure array
    all_overlap_lengths = []    # Track lengths of all possible prefixes ending at the current location
    for i in range(1,len(seq)):
        char = seq[i]
        for j in range(len(all_overlap_lengths)-1,-1,-1):
            if char == seq[all_overlap_lengths[j]]:
                all_overlap_lengths[j] += 1
            else:
                all_overlap_lengths.remove(all_overlap_lengths[j])
        if char == seq[0]:
            all_overlap_lengths.append(1)
        failure_array.append(max([0] + all_overlap_lengths))
    
    w = open("results.txt", "w")
    
    for element in failure_array:
        print element,
        w.write(str(element) + "\n")
    w.close()
    
    print len(seq)