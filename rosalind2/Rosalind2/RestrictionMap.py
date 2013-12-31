'''
Created on Dec 11, 2013

@author: Michael
'''

def add_data(restmap, data, inverted):
#    print restmap
#    print data
#    print
    if data == []:
        w = open("results.txt", "w")
        w.write(" ".join([str(m) for m in sorted(restmap)]))
        w.close
        print " ".join([str(m) for m in sorted(restmap)])
        return True
    
    next_spot = max(data) if not inverted else max(restmap) - max(data)
    next_data = data[:]
    next_map = restmap[:]
    try:
        for r in restmap:
            next_data.remove(abs(r-next_spot))
        next_map.append(next_spot)
    except: 
        return False
        
    if not add_data(next_map,next_data,False):
        if not add_data(next_map,next_data,True):
            return False
    
    return True


if __name__ == '__main__':
    data = [int(d) for d in open("data.txt").readline().strip().split()]
    
    length = max(data)
    data.remove(length)
    restmap = [0, length]
    
    if not add_data(restmap, data, False):
        add_data(restmap, data,True)