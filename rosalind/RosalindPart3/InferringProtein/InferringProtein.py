'''
Created on Jul 24, 2013

@author: Mike
'''

mass_table = \
{"A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841, "G": 57.02146, "H":137.05891, "I":113.08406, \
"K": 128.09496, "L": 13.08406, "M": 131.04049, "N":114.04293, "P":97.05276, "Q":128.05858, "R":156.10111, "S":87.03203, \
"T": 101.04768, "V": 99.06841, "W": 186.07931, "Y":163.06333}

if __name__ == '__main__':
    f = open("data.txt")
    readings = []
    for line in f:
        readings.append(float(line.strip()))
    readings.sort()
    
    protein = ""
    for i in range(len(readings)-1):
        mass = readings[i+1] - readings[i]
        for key in mass_table.keys():
            if mass_table[key]-0.001 < mass < mass_table[key]+0.001:
                protein += key
                break
            
    print protein