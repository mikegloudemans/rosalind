'''
Created on Dec 18, 2012

@author: Mike
'''

if __name__ == '__main__':
    f = open("Population.txt")
    pop = f.readline().strip().split()
    exp = 0
    exp += (int(pop[0])+int(pop[1])+int(pop[2]))*2.0
    exp += int(pop[3])*1.5
    exp += int(pop[4])*1
    print exp