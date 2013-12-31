'''
Created on Dec 18, 2012

@author: Mike
'''

if __name__ == '__main__':
    f = open("Population.txt")
    pop = f.readline().strip().split()
    homo_dom = float(pop[0])
    het= float(pop[1])
    homo_rec = float(pop[2])
    total = homo_dom + het + homo_rec
    
    probrec = (homo_rec/total)*((homo_rec-1)/(total-1))
    probrec += (homo_rec/total)*(het/(total-1))*(1.0/2)
    probrec += (het/total)*(homo_rec/(total-1))*(1.0/2)
    probrec += (het/total)*((het-1)/(total-1))*(1.0/4)
    
    print 1-probrec
    