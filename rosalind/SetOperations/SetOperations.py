'''
Created on Jan 24, 2013

@author: Mike
'''

def readSet(line):
    line = line.strip()
    line = line[1:len(line)-1]
    newSet = set([int(l.strip()) for l in line.split(",")])
    return newSet

def printSet(s,w):
    
    text = "{" + ", ".join([str(item) for item in sorted([i for i in s])]) + "}"
    w.write(text + "\n")

if __name__ == '__main__':
    f = open("data.txt")
    nodes = int(f.readline().strip())
    set1 = readSet(f.readline())
    set2 = readSet(f.readline())
    allNums = set(range(1,nodes+1))
    
    w = open("results.txt", "w")
    
    printSet(set1.union(set2),w)
    printSet(set1.intersection(set2),w)
    printSet(set1.difference(set2),w)
    printSet(set2.difference(set1),w)
    printSet(allNums.difference(set1),w)
    printSet(allNums.difference(set2),w)
    
    w.close()
    
    
