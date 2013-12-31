'''
Created on Dec 13, 2013

@author: Michael
'''

if __name__ == '__main__':
    weightMap = {"A": 71.03711, "C" : 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841, "G": 57.02146, "H": 137.05891, "I": 113.08406,
             "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111, "S": 87.03203,
             "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333}
    
    f = open("data.txt")
    
    ions = []
    
    while True:
        try:
            ions.append(float(f.readline().strip()))
        except:
            break
        
    max_diff = max(weightMap.values())
        
    best_ending_at = [""]*len(ions)
    for i in range(1,len(ions)):
        for j in range(i-1, -1, -1):
            best_length = 0
            if ions[i] - ions[j] > max_diff + 1:
                break
            for key in weightMap.keys():
                if abs(ions[i]-ions[j]-weightMap[key]) < 0.001:
                    if len(best_ending_at[j]) + 1 > best_length:
                        best_length = len(best_ending_at[j]) + 1
                        best_ending_at[i] = best_ending_at[j] + key
        
    best_length = 0
    best_protein = ""
    for i in range(1,len(best_ending_at)):
        if len(best_ending_at[i]) > best_length:
            best_length = len(best_ending_at[i])
            best_protein = best_ending_at[i]
    
    print best_protein