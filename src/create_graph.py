#import cairo
import numpy as np
import igraph
import transformtomatrix as tfm
import runfixating as rf

#creates a plot for a custom graph
#transformtomatrix can be used to convert the short notation for a undirected graph, which has only n*(n-1)/2 characters, to the full adjacency matrix in string format
a = tfm.transformtomatrix('0111101101',5)
#a = np.array([[0,1,1,1,0,0,1,0,0,0],[1,0,1,0,1,0,0,1,0,0],[1,1,0,0,0,1,0,0,1,0],[1,0,0,0,1,1,1,0,0,0],[0,1,0,1,0,1,0,1,0,0],[0,0,1,1,1,0,0,0,1,0],[1,0,0,1,0,0,0,1,1,0],[0,1,0,0,1,0,1,0,1,0],[0,0,1,0,0,1,1,1,0,0],[1,1,1,0,0,1,0,0,0,0]])
#Size of the graph
size = 5
#Initialize adjacency matrix
admat = np.zeros([size,size], dtype=int)
adstrline =a
#remove spaces if some should exist
adstr = adstrline.replace(' ','')

#Fill up the adjacency matrix based on the string format
for k in range(0,size):
        for j in range(0,size):
                admat[k,j]=int(adstr[k+j*size])

g = igraph.Graph.Adjacency(admat.tolist())
gund = g.as_undirected()
layout = gund.layout('kk')

#Commented out part are some ways of changing the layout if you want it to be in a certain format, though usually the automatically generated format suffices
#print layout[:]

#for k in range(0,3):
#    layout[k][0]= k
#    layout[k][1]= 2
#layout[1][1] = 1.75
    #print k*np.pi/size
#for k in range(2,5):
#    layout[k][0]= np.sin((k-2.0)/(size-4.0)*2*np.pi)+0.5
#    layout[k][1]= np.cos((k-2.0)/(size-4.0)*2*np.pi)
#for k in range(5,8):
#    layout[k][0]= np.sin((k-3.0)/(size-4.0)*2*np.pi)-0.5
#    layout[k][1]= np.cos((k-3.0)/(size-4.0)*2*np.pi)
#layout[1][1]= -0.2    
    
#print layout[:]

#mean1 = (layout[0][0]+layout[1][0])/2.0
#mean2 = (layout[0][1]+layout[1][1])/2.0
#print mean1,mean2

#layout[0][0]=layout[0][0]+(layout[0][0]-mean1)
#layout[1][0]=layout[1][0]+(layout[1][0]-mean1)

#layout[0][1]=layout[0][1]+(layout[0][1]-mean2)
#layout[1][1]=layout[1][1]+(layout[1][1]-mean2)

#Change color of the generated graph
gund.vs['color']='blue'
#Save figure
igraph.plot(gund,layout = layout,vertex_size=50,margin=100).save(fname='trial_figures/s' + str(size) + 'min_gen_trial.png')
