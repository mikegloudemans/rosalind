'''
Created on Mar 5, 2013

@author: Mike
'''

if __name__ == '__main__':
    f1 = open("file1.txt","w")
    f2 = open("file2.txt", "w")
    f3 = open("file3.txt", "w")
    
    for i in range(1000):
        for j in range(1000):
            f1.write("aaaaaa")
            f2.write("gaattc")
            if (i%2 == 0):
                f3.write("aaaaaa")
            else:
                f3.write("gaattc")
        f1.write("\n")
        f2.write("\n")
        f3.write("\n")