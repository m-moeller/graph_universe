import numpy as np
import transformtomatrix as tfm
import igraph

def degree_init(size,degree):
        #number of nodes with a fixed degree
        n = len(degree)
        if sum(degree)%2 == 1:
                return -1
        #sort just to make sure, we look from now on at the connections that aren't yet filled instead of at the absolute degree
        connections = np.random.permutation(np.asarray(degree))
        #initialize the adjacency matrix
        admat = np.zeros([size,size],dtype=int)
        #initialze all nodes that don't have all connections filled yet
        v_nodes = range(0,size)

        for k in range(0,n):

                #only need to connect if there are still connections to be filled
                if connections[k]!=0:
                        #since the current node immediately connects up to its degree limit, it can be removed from the list of nodes with open connections
                        v_nodes.remove(k)
                        # randomly chose between all the nodes that still have open connections
                        places = np.random.permutation(v_nodes)[0:connections[k]]
                        #set the respective value in the adjaceny matrix to zero
                        #print places
                        if places.size == 0:
                                #print 'array not sucessfully filled'
                                return -1
                        admat[places,k] = 1
                        admat[k,places] = 1
                        connections[k] = connections[k] - places.size
                        for h in range(k+1,n):
                                # reduce the number of needed connections for every node the current node connected with
                                if admat[h,k]==1:
                                        connections[h] = connections[h]-1
                                        # remove any node that hits 0 connections
                                        if connections[h]==0:
                                                v_nodes.remove(h)
                #print admat
                #print connections
                #print v_nodes
        if sum(connections) != 0:
                #print 'array not sucessfully filled'
                return -1
        return admat
                

