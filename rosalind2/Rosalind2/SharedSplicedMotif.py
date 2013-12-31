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
    answers = []
    for i in range(len(seq1)+1):
        newarr = (len(seq2)+1) * [0]
        newans = (len(seq2)+1) * [""]
        dp.append(newarr)
        answers.append(newans)
             
    for i in range(1,len(seq1)+1):
        for j in range(1,len(seq2)+1):
            if(seq1[i-1] == seq2[j-1]) and (dp[i-1][j-1] + 1 > dp[i-1][j]) and (dp[i-1][j-1] + 1 > dp[i][j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
                answers[i][j] = answers[i-1][j-1] + seq1[i-1]
            elif dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                answers[i][j] = answers[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
                answers[i][j] = answers[i][j-1]
                
    print answers[len(answers)-1][len(answers[0])-1]
                
                