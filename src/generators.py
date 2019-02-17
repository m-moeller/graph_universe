import numpy as np
import igraph
from random import randint
from random import uniform

def rand_cometkite_generator(size,cnodes,tails):
        admat = np.zeros([size,size],dtype=int)
        #generate the fully connected central region
        for k in range(0,cnodes):
                for h in range(0,cnodes):
                        if k!=h:
                                admat[k,h] = 1                      
        #generate the kite-like tails
        for l in range(cnodes,cnodes+tails):
            admat[l,cnodes-1]=1
            admat[cnodes-1,l]=1
        for l in range(cnodes+tails,size):
                #append to a random earlier node
                k = randint(cnodes,cnodes+tails-1)    
                admat[l,k]=1
                admat[k,l]=1
        return admat
        

       
def rand_ringcometkite_generator(size,cnodes):
        admat = np.zeros([size,size],dtype=int)
        #generate the ring-like connected central region
        for k in range(0,cnodes-1):
                admat[k,k+1] = 1
                admat[k+1,k] = 1
        admat[cnodes-1,0] = 1
        admat[0,cnodes-1] = 1
        #generate the kite-like tails
        for l in range(cnodes,size):
                #append to a random earlier node
                k = randint(0,l-1)    
                admat[l,k]=1
                admat[k,l]=1
                l = l+1
        for k in range(0,size):
                admat[k,k]=0
        return admat 

def cometkite_generator(size,cnodes,kites,comets):
        #generates comet graph
        #cnodes is an int that gives us the number of central nodes
        #kites is a vector that gives us the length of kite-like tails at every central node
        #comets is a vector that gives us the number of comet-like leaves at every central node
        if sum(kites)+sum(comets)+cnodes!=size:
                print 'number of central and non-central nodes does not fit size',sum(kites)+sum(comets)+cnodes
                return 0
        if len(kites)!=cnodes:
                print 'length of kite vector does not fit number of central nodes'
                return 0
        if len(comets)!=cnodes:
                print 'length of comet vector does not fit number of central nodes'
                return 0        

        admat = np.zeros([size,size],dtype=int)
        #generate the fully connected central region
        for k in range(0,cnodes):
                for h in range(0,cnodes):
                        if k!=h:
                                admat[k,h] = 1
        #l records at which node we are right now
        l = cnodes
        #endnodes records at which node we need to append the comet-like leaves
        endnodes = np.zeros(cnodes,dtype=int)
        #generate the kite-like tails
        for k in range(0,len(kites)):
                if kites[k]>0:
                        admat[k,l]=1
                        admat[l,k]=1
                        l = l+1                        
                for h in range(1,kites[k]):
                        admat[l-1,l]=1
                        admat[l,l-1]=1
                        l = l+1
                endnodes[k]=l-1
                if kites[k]==0:
                        endnodes[k]=k

        #print endnodes
        
        #generate the comet-like leaves
        for k in range(0,len(comets)):
                for h in range(0,comets[k]):
                        admat[endnodes[k],l]=1
                        admat[l,endnodes[k]]=1
                        l = l+1
        
        return admat

def coupled_generator(size,a):
        #generates coupled graph
        #a is the number of leaves connected to the first center
        admat = np.zeros([size,size],dtype=int)

        #generate the connections to the first center
        for k in range(1,a+2):
                admat[0,k]=1
                admat[k,0]=1
        
        #generate the connections to the second center
        for k in range(a+2,size):
                admat[1,k]=1
                admat[k,1]=1

        return admat

def detour_generator(size,dlength):
        #generates detour graph
        #dlength is the length of the detour

        
        admat = np.zeros([size,size],dtype=int)

        #generate the detour
        for k in range(0,dlength):
                for h in range(0,size):
                        if (h==k+1) or (h==k-1):
                                admat[k,h]=1
        #generate the two 'outer region' nodes
        admat[0,dlength+1]=1
        admat[dlength+1,0]=1
        admat[dlength,dlength-1]=1

        for h in range(dlength+2,size):
                admat[dlength,h]=1
                admat[dlength+1,h]=1

        #generate the inner region of fully connected nodes
        for k in range(dlength+2,size):
                for h in range(dlength,size):
                        if k!=h:
                                admat[k,h] = 1
        return admat

def rand_detour_generator(size,cnumber):
    #generates detour graph
    #cnumber is the number of nodes in the inner region

    l = 0
    while l==0:
        admat = np.zeros([size,size],dtype=int)
        #generate the inner region of fully connected nodes
        for k in range(0,cnumber):
            for h in range(0,cnumber):
                if k!=h:
                    admat[k,h] = 1
        #onumber is the number of nodes in the outer region
        onumber = randint(2,min(cnumber,size-cnumber-1))
        c_connected=0
        for k in range(cnumber,onumber+cnumber-1):
                #print k-onumber-c_connected+1
            connect = randint(1,k-onumber-c_connected+1)
                
            for h in range(c_connected,connect+c_connected):
                admat[k,h]=1
                admat[h,k]=1
            c_connected += connect
                #print connect, c_connected
        
        for h in range(c_connected,cnumber):
            admat[onumber+cnumber-1,h]=1
            admat[h,onumber+cnumber-1]=1                
        #dnumber is the number of detour nodes
        dnumber = size-cnumber-onumber
        open_nodes=range(cnumber,size)
        for k in range(cnumber+onumber,size):
            open_nodes.remove(k)
            if sum(admat[:,k])<2:
                pos1 = randint(0,len(open_nodes)-1)
                o_connected_1 = open_nodes[pos1]
                open_nodes.remove(o_connected_1)
                        #print k,1
                admat[k,o_connected_1]=1
                admat[o_connected_1,k]=1
            if sum(admat[:,k])<2:
                        #print k,2
                pos2 = randint(0,len(open_nodes)-1)
                o_connected_2 = open_nodes[pos2]

                admat[k,o_connected_2]=1
                admat[o_connected_2,k]=1

            open_nodes = open_nodes+[o_connected_1]
        #print dnumber  
        g = igraph.Graph.Adjacency(admat.tolist())

        #check connectivity of the graph
        l = 1
		
        if g.vertex_disjoint_paths() == 0:
            l = 0 
			
        for h in range(cnumber,cnumber+onumber):
            detour_connected = sum(admat[h,size-dnumber:size])
            if detour_connected == 0:
                l = 0
    return admat

def multi_generator(size,cnumber):
        #generates 'multi-stars' like the coupled star, but with more centers
        #cnumber is the number of centers
        if size%cnumber!=0:
                return 'size not divisible by number of centers!'

        admat = np.zeros([size,size],dtype=int)
        #lnumber records the number of leaves at every center
        lnumber = (size-cnumber)/cnumber

        #generate the line-like connections between the centers
        for k in range(0,cnumber):
                if k!=0:
                        admat[k,k-1]=1
                if k!=(cnumber-1):
                        admat[k,k+1]=1

        #generate the leaves that are connected to the various centers
        for k in range(0,cnumber):
                for h in range(cnumber+k*lnumber,cnumber+(k+1)*lnumber):
                        if k!=h:
                                admat[k,h]=1
                                admat[h,k]=1

        return admat

def comet_generator(size,dlength):
        #generates comet graph

        admat = np.zeros([size,size],dtype=int)
        
        for k in range(0,dlength):
                admat[dlength,k]=1
                admat[k,dlength]=1


        #for k in range(0,dlength):
        #        for h in range(0,size):
        #                if (h==k+1) or (h==k-1):
        #                        admat[k,h]=1

        #admat[dlength,dlength-1]=1

        for k in range(dlength,size):
                for h in range(dlength,size):
                        if k!=h:
                                admat[k,h] = 1
        return admat        
        
def generalstar_generator(size,a):
        #generates the generalized star like the double star, but also with more centers
        #a is the number of centers, size-a is thus the number of leaves which are connected to all the center
        admat = np.zeros([size,size],dtype=int)
        
                
        #generate the connections between all the leaves and the centers
        for k in range(a,size):
                for h in range(0,a):
                
                        admat[h,k]=1
                        admat[k,h]=1
 
        return admat

def rand_generalstar_generator(size,a,p):
        #generates the generalized star like the double star, but also with more centers
        #a is the number of centers, size-a is thus the number of leaves which are connected to all the center
        admat = np.zeros([size,size],dtype=int)
        for k in range(0,a):
                for h in range(0,a):
                        if k!=h:
                                if uniform(0,1)<p:
                                        admat[k,h]=1
                                        admat[h,k]=1
                
        #generate the connections between all the leaves and the centers
        for k in range(a,size):
                for h in range(0,a):
                
                        admat[h,k]=1
                        admat[k,h]=1
 
        return admat
        
def kite_generator(size,dlength):
        #generates kite graph

        admat = np.zeros([size,size],dtype=int)


        for k in range(0,dlength):
                for h in range(0,size):
                        if (h==k+1) or (h==k-1):
                                admat[k,h]=1

        admat[dlength,dlength-1]=1

        for k in range(dlength,size):
                for h in range(dlength,size):
                        if k!=h:
                                admat[k,h] = 1
        return admat