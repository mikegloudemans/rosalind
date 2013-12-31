'''
Created on Jan 24, 2013

@author: Mike
'''

def partialPerms(items, choices):
    perms = 1
    while (choices > 0):
        perms = (perms * items) % 1000000
        items -= 1
        choices -= 1
    return perms
    
if __name__ == '__main__':
    data = open("data.txt").readline().split()
    items, choices = int(data[0]), int(data[1])
    print partialPerms(items, choices)
