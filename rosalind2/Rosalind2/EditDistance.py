'''
Created on Dec 13, 2013

@author: Michael
'''

if __name__ == '__main__':
    f = open("data.txt")
    
    f.readline()
    seq1 = ""
    nextline = f.readline().strip()
    while not nextline.startswith(">"):
        seq1 += nextline
        nextline = f.readline().strip()
        
    seq2 = ""
    while nextline != "":
        nextline = f.readline().strip()
        seq2 += nextline
        
    dp = []
    answers1 = []
    answers2 = []
    for i in range(len(seq1)+1):
        newarr = (len(seq2)+1) * [0]
        newans = (len(seq2)+1) * [""]
        dp.append(newarr)
        answers1.append(newans)
        answers2.append(newans)
        
    for i in range(1,len(dp)):
        dp[i][0] = dp[i-1][0] + 1
        answers1[i][0] = answers1[i-1][0] + seq1[i-1]
        
    for i in range(1,len(dp[0])):
        dp[0][i] = dp[0][i-1] + 1  
        answers2[0][i] = answers1[0][i-1] + seq2[i-1]     
             
    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1):
            if(seq1[i-1] == seq2[j-1]) and (dp[i-1][j-1] < dp[i-1][j] + 1) and (dp[i-1][j-1] < dp[i][j-1] + 1):
                dp[i][j] = dp[i-1][j-1]
                answers1[i][j] = answers1[i-1][j-1] + seq1[i-1]
                answers2[i][j] = answers2[i-1][j-1] + seq1[i-1]
            elif(seq1[i-1] != seq2[j-1]) and (dp[i-1][j-1] < dp[i-1][j]) and (dp[i-1][j-1] < dp[i][j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
                answers1[i][j] = answers1[i-1][j-1] + seq1[i-1]
                answers2[i][j] = answers2[i-1][j-1] + seq1[i-1]
            elif dp[i-1][j] < dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + 1
                answers1[i][j] = answers1[i-1][j] + "-"
                answers2[i][j] = answers2[i-1][j] + seq1[i-1]
            else:
                dp[i][j] = dp[i][j-1] + 1
                answers1[i][j] = answers1[i][j-1] + "-"
                answers2[i][j] = answers2[i][j-1] + seq2[j-1]
                
    #print dp[len(dp)-1][len(dp[0])-1]
    #print dp
    
    print answers1[len(answers1)-1][len(answers1[0])-1]
    print answers2[len(answers2)-1][len(answers2[0])-1]