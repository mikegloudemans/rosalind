'''
Created on Jan 24, 2013

@author: Mike
'''


def removeCluster(edges):
    # Remove all connected edges in a single cluster from a tree
    # Return number of elements in removed cluster.
    cluster = set(edges.pop())
    for i in range(len(edges)-1,-1,-1):
        if edges[i][0] in cluster or edges[i][1] in cluster:
            cluster = cluster.union(edges[i])
            edges.remove(edges[i])
    return len(cluster)
    

if __name__ == '__main__':
    f = open("graph.txt")
    nodes = int(f.readline().strip())
    edges = [[int(num) for num in l.strip().split()] for l in f.read().splitlines()]
    #print edges
    
    total_clusters = 0
    unclustered = nodes
    
    while edges != []:
        unclustered -= removeCluster(edges)
        total_clusters += 1
        #print edges
        
    edgesToAdd = total_clusters + unclustered - 1
    print edgesToAdd