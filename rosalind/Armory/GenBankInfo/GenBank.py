'''
Created on Mar 7, 2013

@author: Mike
'''

from Bio import Entrez

if __name__ == '__main__':

    organism = "Dirphia"
    
    startDate = "2007/10/08"
    endDate= "2012/07/30"
    
    Entrez.email = "michael.gloudemans@duke.edu"
    query = "((\"" + startDate + "\"[Publication Date] : \"" + endDate + "\"[Publication Date]))"
    query += " AND \"" + organism + "\"[Organism]" 
    handle = Entrez.esearch(db="nucleotide", term=query)
    record = Entrez.read(handle)
    
    print record['Count']