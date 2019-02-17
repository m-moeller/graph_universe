import numpy as np
import scipy.spatial
import runfixating as rf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_pdf import PdfPages

import generators as gen
import time

#size of the population
size = 8
#fitness of the mutant
r = 2
#number of runs for random generators; The more runs, the higher the likelihood it hits most possible combinations
m = 100

#number of all possible graphs of a certain size
numberALL = (1, 1, 1, 2, 6, 21, 112, 853, 11117, 261080,11716571)
#choose the number for the relevant size
number = numberALL[size]


#Open data file with fixation probability and time of all possible graphs
e = open('../data/fixation_size_' + str(size) + '_fitness_' + string_fitness[counter] + '_Bd_full.txt','r')
lines = e.readlines()

#Initialize file for all fixation probabilities and times
times = np.zeros(number, dtype=float)
probs = np.zeros(number, dtype=float)
#admat = np.zeros([number,size,size], dtype=int)

#Initialize vector for the graphs that have at least one node with only one connection
probs_1c = np.zeros(0)
times_1c = np.zeros(0)
#Initialize vector for the graphs that have at least one node with only two connection
#probs_2c = np.zeros(0)
#times_2c = np.zeros(0)

#h = 0

#Counter for big sizes as indication how long it's going to take 
#start = time.time()

#Loop to read out the file with all probabilities and times
for i in range(0,number):
                #read out the time
                timeLine = lines[7*i+3]
                times[i] = float(timeLine)
                #read out the probability
                probLine = lines[7*i+1]
                probs[i] = float(probLine)
                #Read out the adjacency matrix as a string
                adstrline = lines[7*i]
                adstr = adstrline.replace(' ','')
                admat = np.zeros([size,size], dtype=int)
                #Convert from string format to matrix format
                for k in range(0,size):
                        for j in range(0,size):
                                admat[k,j]=int(adstr[k+j*size])

                #Counter for big sizes as indication how long it's going to take    
                #if h<i:
                #    print h/number
                #    h = h +number/100
                #    end = time.time()
                 #   print(end - start)
                #Check for a node with only one connection 
                if min(sum(admat))==1:
                    probs_1c = np.append(probs_1c,probs[i])
                    times_1c = np.append(times_1c,times[i])
                    

#create new combination of fixation probability and time to look into extreme graphs in a certain direction (for example, high time and low probability)
#newdir=times-(607*probs)

#Sort in a direction 
#arg = np.argsort(-probs)

#Sort the adjacency matrices, too, in that direction
#admatsorted = admat[arg]
#probssorted = probs[arg]

#Show the n most extreme graphs in a certain direction
#print admatsorted[number-5:number]
#print times[arg[number-5:number]],probs[arg[number-5:number]]

#close data file
e.close()

#Generate random detour graphs

#Initialize vectors for fixation probability and times of the detour graphs
randdetourtimes = np.zeros(0, dtype=float)
randdetourprobs = np.zeros(0, dtype=float)
#Initialize matrix for the adjacency matrix of the detour graphs
admat = np.zeros([size,size], dtype=int)

#For-loop for the creation of the detour graphs
#k controls the length of the detour
for k in range(2,size-3):
        #h is the number of reruns to create graphs with the same detour length
        for h in range(0,m):
                #generate detour graph
                admat = gen.rand_detour_generator(size,k)
                #convert adjacency matrix to string
                adflat = admat.flatten()
                adstring = ''
                for j in range(0,len(adflat)):
                        adstring += str(adflat[j])
                #run algorithm to determine fixation probability and time of the detour graph        
                outputranddetour = rf.runfixating('Bd',str(size),'undirected',str(r),'custom',adstring,'0')
                randdetourtimes = np.append(randdetourtimes, outputranddetour[3])
                randdetourprobs = np.append(randdetourprobs, outputranddetour[1])

#Generate some specific detour graphs in case they were missed by the random version

#Initialize vectors for fixation probability and times of the detour graphs                
detourtimes = np.zeros(size, dtype=float)
detourprobs = np.zeros(size, dtype=float)

#For-loop for the creation of the detour graphs
#k controls the length of the detour
for k in range(1,size-2):
        #generate detour graph
        admat = gen.detour_generator(size,k)
        #convert adjacency matrix to string
        adflat = admat.flatten()
        adstring = ''
        for j in range(0,len(adflat)):
                adstring += str(adflat[j])
        #run algorithm to determine fixation probability and time of the detour graph   
        outputdetour= rf.runfixating('Bd',str(size),'undirected',str(r),'custom',adstring,'0')
        detourtimes[k] = outputdetour[3]
        detourprobs[k] = outputdetour[1]

#Generate simple kite graphs

#Initialize vectors for fixation probability and times of the kite graphs           
kitetimes = np.zeros(size, dtype=float)
kiteprobs = np.zeros(size, dtype=float)

#For-loop for the creation of the kite graphs
#k controls the length of the tail
for k in range(0,size):
        #generate kite graph
        admat = gen.kite_generator(size,k)
        #convert adjacency matrix to string
        adflat = admat.flatten()
        adstring = ''
        for j in range(0,len(adflat)):
                adstring += str(adflat[j])
        #run algorithm to determine fixation probability and time of the kite graph   
        outputkite = rf.runfixating('Bd',str(size),'undirected',str(r),'custom',adstring,'0')
        kitetimes[k] = outputkite[3]
        kiteprobs[k] = outputkite[1]

#Generate random comet-kite graphs

#Initialize vectors for fixation probability and times of the comet-kite graphs           
cometkitetimes = np.zeros(0, dtype=float)
cometkiteprobs = np.zeros(0, dtype=float)

#For-loop for the creation of the comet-kite graphs
#k controls the number of nodes in the central region
for k in range(1,size):
        #l controls the number of tails
        for l in range(1,min(3,size-k+1)):
            #h is the number of reruns to create graphs with the same number of central nodes and tails
            for h in range(0,m):
                    #Create comet-kite graphs
                    admat = gen.rand_cometkite_generator(size,k,l)
                    #convert adjacency matrix to string
                    adflat = admat.flatten()
                    adstring = ''
                    for j in range(0,len(adflat)):
                            adstring += str(adflat[j])
                    #run algorithm to determine fixation probability and time of the comet-kite graph          
                    outputcometkite = rf.runfixating('Bd',str(size),'undirected',str(r),'custom',adstring,'0')
                    cometkitetimes = np.append(cometkitetimes, outputcometkite[3])
                    cometkiteprobs = np.append(cometkiteprobs, outputcometkite[1])





#Generate generalized star graphs

#Initialize vectors for fixation probability and times of the generalized star graphs  
generaltimes = np.zeros(0, dtype=float)
generalprobs = np.zeros(0, dtype=float)

#For-loop for the creation of the generalized star graphs
#k controls the number of nodes in the 'center'
for k in range(0,int(np.floor(size/2))):
        #h controls the number of connections between the central graphs; h=0 means no nodes in the center are connected, h=max means all of them
        for h in range(0,m):
                #generate the generalized star graph
                admat = gen.rand_generalstar_generator(size,k+1,float(h)/float(m))
                #convert adjacency matrix to string
                adflat = admat.flatten()
                adstring = ''
                for j in range(0,len(adflat)):
                        adstring += str(adflat[j])
                #run algorithm to determine fixation probability and time of the generalized star graph    
                outputgeneral = rf.runfixating('Bd',str(size),'undirected',str(r),'custom',adstring,'0')
                generaltimes = np.append(generaltimes, outputgeneral[3])
                generalprobs = np.append(generalprobs, outputgeneral[1])

#Generate coupled star graphs

#Initialize vectors for fixation probability and times of the coupled star graphs  
coupledtimes = np.zeros(int(np.floor((size-2)/2)), dtype=float)
coupledprobs = np.zeros(int(np.floor((size-2)/2)), dtype=float)

#For-loop for the creation of the generalized star graphs
#k controls the number of nodes connected to the second center
for k in range(0,int(np.floor((size-2)/2))):
        #generate the coupled star graph
        admat = gen.coupled_generator(size,k+1)
        #convert adjacency matrix to string
        adflat = admat.flatten()
        adstring = ''
        for j in range(0,len(adflat)):
                adstring += str(adflat[j])
        #run algorithm to determine fixation probability and time of the coupled star graph 
        outputcoupled = rf.runfixating('Bd',str(size),'undirected',str(r),'custom',adstring,'0')
        coupledtimes[k] = outputcoupled[3]
        coupledprobs[k] = outputcoupled[1]

#Check fixation probability and time of the fully connected graph
outputfully = rf.runfixating('Bd',str(size),'undirected',str(r),'ER','GNP','1')
fullyprob = outputfully[1]
fullytime = outputfully[3]

#Check fixation probability and time of the ring graph
outputring = rf.runfixating('Bd',str(size),'undirected',str(r),'WS','1','0')
ringprob = outputring[1]
ringtime = outputring[3]

#Add the kites to the comet-kites since they're just a subcategory
cometkite_probs_plot = np.append(cometkiteprobs, kiteprobs)
cometkite_times_plot = np.append(cometkitetimes, kitetimes)

#Add the deterministically generated detour graphs to the randomly generated detour graphs since they're also just a subcategory
detour_probs_plot = np.append(randdetourprobs,detourprobs[1:size-2])
detour_times_plot = np.append(randdetourtimes,detourtimes[1:size-2])

#Create the figure
plot1 = plt.figure(1, figsize=(10.0,10.0))
#Plot the fixation probability and time of all graphs
plt.plot(probs,times,'o', color = '0.5')
#Plot the fixation probability and time of all graphs with only one connection
plt.plot(probs_1c,times_1c, 'o', color = '0.8')
#plt.plot(probs_2c,times_2c, 'bo')
#Plot the fixation probability and time of the comet-kite graphs
plt.plot(cometkite_probs_plot,cometkite_times_plot,'go',alpha=0.7)
#Plot the fixation probability and time of the detour graphs
plt.plot(detour_probs_plot,detour_times_plot,'bo',alpha=0.7)
#Plot the fixation probability and time of the generalized star graphs
plt.plot(generalprobs[:],generaltimes[:],'ro',alpha=0.7)
#Plot the fixation probability and time of the coupled star graphs
plt.plot(coupledprobs[:],coupledtimes[:],'r*',alpha=1,markersize=15)
#Increase font size for better readability
plt.rcParams.update({'font.size': 20})

#Increase tick size to read plot better
ax = plt.gca()
ax.xaxis.set_tick_params(width=2)
ax.xaxis.set_tick_params(length=10)
ax.yaxis.set_tick_params(width=2)
ax.yaxis.set_tick_params(length=10)
#Pad x-axis between figure and tick text
#ax.tick_params(axis='x', pad=30)
#ax.tick_params(labelsize=6)

#Plot star graph
#plt.plot(generalprobs[0],generaltimes[0],'k*',label='star',alpha=1,markersize=10)
#Plot ring graph
#plt.plot(ringprob,ringtime,'ko',label='ring',alpha=1)
#Plot fully connected graph
plt.plot([-1,1],[fullytime,fullytime],'k--',label='well-mixed',alpha=1)
plt.plot([fullyprob,fullyprob],[-2000,2000],'k--',label='well-mixed2',alpha=1)

#Change limit for the x axis
plt.xlim([-0.04,0.69])
#Change limit for the y axis
plt.ylim([-20,420])
#label for the y axis
plt.ylabel("Average fixation time")
#label for the x axis
plt.xlabel("Fixation probability")
#Title for the figure
#plt.title("full plot size " + str(size))
#Save figure
plt.savefig('overview_greytones2' + str(size) + 'r' + str(r) + '.png',dpi=300)
#close figure
plt.close()
#plt.show()
