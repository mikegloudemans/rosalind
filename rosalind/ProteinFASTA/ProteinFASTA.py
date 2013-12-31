'''
Created on Jan 22, 2013

@author: Mike
'''

import urllib

if __name__ == '__main__':
    f = urllib.urlopen("http://www.uniprot.org/uniprot/uniprot_id.fasta")
    for line in f:
        print line