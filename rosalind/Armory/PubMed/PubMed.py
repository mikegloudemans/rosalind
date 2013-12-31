'''
Created on Mar 7, 2013

@author: Mike
'''

from Bio import Entrez

if __name__ == '__main__':
    author = "Durrani OM"
    year = "2012"
    
    Entrez.email = "michael.gloudemans@duke.edu"
    
    handle = Entrez.esearch(db="pubmed", term= "\"" + author + "\"[Author] " + year+"[dp]")
    record = Entrez.read(handle)
    
    entryCount = record["Count"]
    
    handle = Entrez.esearch(db="pubmed", term= "\"" + author + "\"[Author] " + year+"[dp]", retmax = entryCount)
    record = Entrez.read(handle)
    
    print sorted(record["IdList"])[0]
    
    