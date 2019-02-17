import numpy as np
import transformtomatrix as tfm
import igraph
#initialize random degree distribution based on an Erdos Renyi graph
# the p is the likelihood of any link to be established
def rand_degree_init(size,p):
        #calculate ER graph
        g = igraph.Graph.Erdos_Renyi(size,p)
        #calculate the degree distribution of the ER graph
        degree = g.degree_distribution()
        #change the format so it is easier workable
        h1 = list(degree.bins())
        h = np.zeros([1,size],dtype=int)
        d = np.zeros([1,size],dtype=int)
        for k in range(0,len(h1)):
                n = int(h1[k][0])
                #print n
                h[0,n] = int(h1[k][2])
        i = 0
        for k in range(0,size):
                for j in range(0,h[0,k]):
                        d[0,i] = k
                        i = i+1
        #d is still the degree distribution, just slightly formatted                
        return d
