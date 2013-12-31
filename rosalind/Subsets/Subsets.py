'''
Created on Jan 24, 2013

@author: Mike
'''

if __name__ == '__main__':
    items = 827
    sets = 1
    while items > 0:
        sets = (sets * 2) % 1000000
        items -= 1
    print sets
    