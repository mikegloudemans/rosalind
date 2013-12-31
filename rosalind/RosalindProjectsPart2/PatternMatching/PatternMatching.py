'''
Created on May 11, 2013

@author: Mike
'''
currentNum = 2

def newTree(word):
    global currentNum
    currentNum += 1
    if word == "":
        return {}
    else:
        newDict = {}
        numToUse = currentNum
        newDict[(word[0],numToUse)] = newTree(word[1:])
        return newDict
    
def print_adjacencies(d):
    for key1 in d.keys():
        for key2 in d[key1].keys():
            print key1[1], key2[1], key2[0]
        print_adjacencies(d[key1])
    

if __name__ == '__main__':
    # Parse data
    f = open("data.txt")
    allSeqs = []
    for line in f:
        line = line.strip();
        if line == "":
            continue
        allSeqs.append(line)
    f.close()
#    print allSeqs
    
    tree = {}
    for seq in allSeqs:
        nextNode = {}
        assigned = False
        for key in tree.keys():
            if seq[0] == key[0]:
                nextNode = tree[key]
                assigned = True
        if not assigned:
            numToUse = currentNum
            tree[(seq[0],numToUse)] = newTree(seq[1:])
            continue
        for i in range(1,len(seq)): # Will fail if given a one-letter sequence
            letter = seq[i]
            for key in nextNode.keys():       
                if letter == key[0]:
                    nextNode = nextNode[key]
                    break
            else:
                numToUse = currentNum
                nextNode[(letter,numToUse)] = newTree(seq[i+1:])
                break          
#    print tree
    
    for key in tree.keys():
        print "1 " + str(key[1]) + " " + key[0]
    
    print_adjacencies(tree)
        
    
    