import numpy as np
import transformtomatrix as tfm
import igraph
import runfixating as rf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_pdf import PdfPages

#import fileinput
#import cProfile

#pr = cProfile.Profile()
#pr.enable()
#rank = 0
#from mpi4py import MPI
#comm = MPI.COMM_WORLD
#rank = comm.Get_rank()

#size of the network
size = 8
#Fitness of mutant
r = 1.25
#b is the number of bits for each individual
b = size*(size-1)/2
#n is the number of individuals
n = 40
#m is the number of evolutionary steps
m= 1000
#top gives the number of chosen individuals per evolutionary step
top = 5
#mutchance gives the chance to mutate
mutchance = 2.0/b
#print mutchance

#Initialize number of unique graphs of a certain size
numberALL = (1, 1, 1, 2, 6, 21, 112, 853, 11117, 261080,11716571)
#Choose the number for the current size
number = numberALL[size]

#The part commented out here is in case you want to plot the path of the graphs chosen by the algorithm
e = open('../data/fixation_size_' + str(size) + '_fitness_125_Bd_full.txt','r')
lines = e.readlines()

times = np.zeros(number, dtype=float)
probs = np.zeros(number, dtype=float)

outputfully = rf.runfixating('Bd',str(size),'undirected',str(r),'ER','GNP','1')
fullyprob = outputfully[1]
fullytime = outputfully[3]

plt.plot([0,1],[fullytime,fullytime],'k--',label='well-mixed',alpha=1)
plt.plot([fullyprob,fullyprob],[0,2000],'k--',label='well-mixed2',alpha=1)    
    
for i in range(0,number):
                timeLine = lines[7*i+3]
                times[i] = float(timeLine)
                probLine = lines[7*i+1]
                probs[i] = float(probLine)
plt.plot(probs,times,'o', color = '0.5')
    
ax = plt.gca()
ax.xaxis.set_tick_params(width=2)
ax.xaxis.set_tick_params(length=10)
ax.yaxis.set_tick_params(width=2)
ax.yaxis.set_tick_params(length=10)
ax.tick_params(axis='x', pad=30)
    
plt.xlim([0.14,0.36])
plt.ylim([-20,320])

#Initialize value for checking whether graphs are fully connected
h=0
#if rank == 0:
if 1:
    #create graphs until one is fully connected
    while h==0:
        temp=""
        #create random number between 0 and 2^b 
        for i in range(0,b):
            randind = np.random.randint(2)
            #convert that number to binary so you get a string of length b
            temp += bin(randind)[2:]
        #transform the string into a matrix
        print temp
        print tfm.transformtomatrix(temp,size)
        (tempmat,a) = tfm.transformtomatrix(temp,size)
        #convert the matrix into a format that is readable for igraph
        g = igraph.Graph.Adjacency(tempmat.tolist())
        #check connectivity of the graph
        if g.vertex_disjoint_paths() > 0:
            h = 1
    
    tind = [temp]
    #print temp
    h=0
    #create graphs until you have n-1 fully connected graphs
    for j in range(1,n):
        while h==0:
            temp=""
            #create random number between 0 and 2^b 
            for i in range(0,b):
                randind = np.random.randint(2)
                #convert that number to binary so you get a string of length b
                temp += bin(randind)[2:]
            #transform the string into a matrix
            (tempmat,a)= tfm.transformtomatrix(temp,size)
            #convert the matrix into a format that is readable for igraph
            g = igraph.Graph.Adjacency(tempmat.tolist())
            #check connectivity of the graph
            if g.vertex_disjoint_paths() > 0:
                h = 1
            
        tind.append(temp)
        h=0
    #print tind
    #ind needs to be a numpy array to use certain functionalities
    ind = np.array(tind)
    #initialize fitness
    fit = np.zeros(n,dtype=float)
    time = np.zeros(n,dtype=float)
    #cross chooses the partners for crossover
    cross = np.zeros([2,n],dtype=int)
    #main loop for the evolution
    plot1 = plt.figure(1, figsize=(10.0,10.0))
    for j in range(0,m):
        #inner  loop for fitness calculation
        for i in range(0,n):
            #fit[i] =int(ind[i],2) #only this line needs to be changed for our problem
            indnorm = str(ind[i])
            (tempmat,rfmat)= tfm.transformtomatrix(indnorm,size)
            #convert the matrix into a format that is readable for igraph
            g = igraph.Graph.Adjacency(tempmat.tolist())
            #calculate fitness; if the graph isn't connected, the fitness is set to the lowest possible value 0(this shouldn't happen, but it's there as a failsafe)
            if g.vertex_disjoint_paths() == 0:
                fit = 0
            #print rfmat
            else:
                output = rf.runfixating('Bd',str(size),'directed',str(r),'custom',rfmat,'0')
                fitnorm = float(output[1])
                time[i] = float(output[3])
                fit[i] = fitnorm
            
            #send the individual to one of the threads
        #    comm.send(indnorm, dest=i+1)
            
        #for i in range(0,n):
            #receive the fitness of one of the individuals            
        #    fitnorm = comm.recv( source=i+1)
        #    fit[i] = fitnorm

        #print 'fit', fit
        #x is the array of the fittest individuals
        x = ind[np.argsort(fit)][:top]
        plt.plot(fit[np.argsort(fit)],time[np.argsort(fit)],'co',alpha=0.7)
        plt.plot(fit[np.argsort(fit)][:top],time[np.argsort(fit)][:top],'co')
        #chooses the first partner for crossover
        cross[0]= np.random.randint(top,size =n)
        #chooses the second partner for crossover
        cross[1] = np.random.randint(top,size=n)
        #inner loop for the crossover and mutation step
        for i in range(0,n):
            while h==0:
                newstring = ''
                #inner loop over each value inside an individual
                for k in range(0,b):
                    #decides whether to take value from either partner
                    if np.random.rand() < 0.5:
                        tempstring = x[cross[0][i]][k]
                    else:
                        tempstring = x[cross[1][i]][k]
                    #decides to mutate a value based on mutchance
                    if np.random.rand() < mutchance:
                        newstring = newstring + bin(np.abs(int(tempstring,2)-1))[2:]
                        #print 'mutated'
                    else:
                        #print 'not mutated'
                        newstring = newstring + tempstring
                        #transform the string into a matrix
                (tempmat,a) = tfm.transformtomatrix(newstring,size)
                #convert the matrix into a format that is readable for igraph
                g = igraph.Graph.Adjacency(tempmat.tolist())
                #check connectivity of the graph    
                if g.vertex_disjoint_paths() > 0:
                    h = 1
            #print 'newstring', newstring
            ind[i] = newstring
            h = 0
            
    print(fit[np.argsort(fit)][:top])
    print(x)

    plt.savefig('genalgo_path' + str(size) + 'r' + str(r) + '.png',dpi=600)

#all the other threads only calculate the fitness of one individual
#if rank != 0:
#    ind = '0'
#    fit = 0
    #the thread needs to do this calculation m times
#    for j in range(0,m):
        #receive the individual from thread zero
#        ind = comm.recv( source = 0)
        #transform the string into a matrix
#        (tempmat,rfmat)= tfm.transformtomatrix(ind,size)
        #convert the matrix into a format that is readable for igraph
#        g = igraph.Graph.Adjacency(tempmat.tolist())
        #calculate fitness; if the graph isn't connected, the fitness is set to the lowest possible value 0(this shouldn't happen, but it's there as a failsafe)
#        if g.vertex_disjoint_paths() == 0:
#            fit = 0
        #print rfmat
#        else:
#            output = rf.runfixating('Bd',str(size),'directed','2','custom',rfmat,'0')
#            fit = float(output[3])

#        comm.send(fit,dest=0)
#pr.disable()
#pr.print_stats(sort='cumtime')
