'''
Created on Dec 13, 2013

@author: Michael
'''

def compare_adjacencies(list1, list2):
    # Determine current number of correct adjacencies.
    
    adjs = 0
    if list1[0] == list2[0]:
        adjs += 1
    if list1[len(list1)-1] == list2[len(list2)-1]:
        adjs += 1
        
    for i in range(1,len(list1)):
        for j in range(1,len(list2)):
            if list1[i-1:i+1] == list2[j-1:j+1] or list1[i-1:i+1] == list2[j:j-2:-1]:
                adjs += 1
                break
    
    return adjs

if __name__ == '__main__':
    f = open("data.txt")
    
    line1 = [int(d) for d in f.readline().strip().split()]
    line2 = [int(d) for d in f.readline().strip().split()]
    
    done = False
    
    if compare_adjacencies(line1, line2) == 11:
        done = True
        
    iterations = 0
    lists = [[line1, []]]
    while not done:
        
        all_lists = []
        best_adjs = 0
        #best_list = pair[0]
        for mylist in lists:
            old_adj = compare_adjacencies(mylist[0], line2) 
            for i in range(10):
                for j in range(10):
                    if i >= j:
                        continue
                    new_list = (mylist[0][:i] + mylist[0][i:j+1][::-1] + mylist[0][j+1:], mylist[1]+[[i,j]])
                    new_adjs = compare_adjacencies(new_list[0], line2)
                    if new_adjs > best_adjs:
                        best_adjs = new_adjs
                        best_list = new_list
                    if new_adjs > old_adj:
                        if new_list[0] not in [a[0] for a in all_lists]:
                            all_lists.append(new_list)
        
        #pair[0] = best_list
        iterations += 1
        
        if best_adjs == 11:
            done = True
            
        lists = all_lists
        
        print iterations
        print len(all_lists)
    
    print iterations
    for b in best_list[1]:
        print " ".join([str(l+1) for l in b])
