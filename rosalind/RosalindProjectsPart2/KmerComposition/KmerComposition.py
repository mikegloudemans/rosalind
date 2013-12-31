'''
Created on May 11, 2013

@author: Mike
'''

def words(n, alphabet):
    if n == 1:
        return alphabet
    else:
        word_list = []
        for letter in alphabet:
            for word in words(n-1,alphabet):
                word_list.append(letter + word)
        return word_list

if __name__ == '__main__':
    # Parse sequence
    f = open("data.txt")
    f.readline()
    sequence = ""
    nextLine = f.readline().strip()
    while nextLine != "":
        sequence += nextLine
        nextLine = f.readline().strip()
    
    # Set up dictionary
    keys = words(4, ["A", "C", "G", "T"])
    dCount = {}
    for k in keys:
        dCount[k] = 0
    
    for i in range(len(sequence)-3):
        dCount[sequence[i:i+4]] += 1
    
    counts = [data[1] for data in sorted(dCount.items())]
    
    for c in counts:
        print c,