import numpy as np
import scipy.spatial
import runfixating as rf
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_pdf import PdfPages
import heat_heterogeneity as het
import generators as gen
#generates full heat heterogeneity vs fixation probability plot for smaller sizes
#size of the population
size = 4
#r is the fitness value
r = 1.75
#e is the data with the full data for a given size
e = open('../data/fixation_size_' + str(size) + '_fitness_175_Bd_full.txt','r')


lines = e.readlines()

#numberOfGraphs is the total number of possible graphs for a given size
numberAll = (6,21,112,853,11117,261080,11716571)
numberOfGraphs = numberAll[size-4]


#times are the fixation times of all graphs
times = np.zeros((numberOfGraphs), dtype=float)
#probs are the fixation probabilities of all graphs
probs = np.zeros((numberOfGraphs), dtype=float)
#admat are the adjacency matrices for all graphs
admat = np.zeros([size,size], dtype=int)
#heat is the square root of heat heterogeneity
heat = np.zeros(numberOfGraphs, dtype=float)

#fill up the vectors times, probs, heat
for i in range(0,numberOfGraphs):
                timeLine = lines[7*i+3]
                times[i] = float(timeLine)
                
                probLine = lines[7*i+1]
                
                #print probLine
               
                probs[i] = float(probLine)
                adstrline = lines[7*i]
                adstr = adstrline.replace(' ','')

                for k in range(0,size):
                        for j in range(0,size):
                                admat[k,j]=int(adstr[k+j*size])
       
                heat[i] = het.het(admat)
#corr is the correlation between probs and heat
corr = np.corrcoef(probs[:],heat[:])
print corr

#admatstar is the adjacency matrix of the star
admatstar = gen.generalstar_generator(size,1)
#calculate the fixation probability and time of the star
adflat = admatstar.flatten()
adstring = ''
for j in range(0,len(adflat)):
        adstring += str(adflat[j])

outputgeneral = rf.runfixating('Bd',str(size),'undirected',str(r),'custom',adstring,'0')
#startime, starprob and starhet are the fixation time, probability and the square root of the heat heterogeneity of the star, respectively
startime = outputgeneral[3]
starprob = outputgeneral[1]
#starhet = np.sqrt(het.het(admatstar))
#calculate the fixation prob and time of the fully connected graph
outputfully = rf.runfixating('Bd',str(size),'undirected',str(r),'ER','GNP','1')
fullyprob = outputfully[1]
fullytime = outputfully[3]
#calculate the fixation prob and time of the ring
outputring = rf.runfixating('Bd',str(size),'undirected',str(r),'WS','1','0')
ringprob = outputring[1]
ringtime = outputring[3]
#plot everything
#plt.rcParams.update({'font.size': 22})

#plot2 = plt.figure(1, figsize=(10.0,10.0))
#plt.plot(probs[:],times[:],'o', color = '0.5',alpha=0.7)

#plt.plot(starprob,startime,'k*',label='star',alpha=1,markersize=10)
#plt.plot(ringprob,ringtime,'ko',label='ring',alpha=1,markerfacecolor='None',markersize=10)
#plt.plot([0,1],[fullytime,fullytime],'k--',label='well-mixed',alpha=1)
#plt.plot([fullyprob,fullyprob],[0,1000],'k--',label='well-mixed2',alpha=1)



#plt.legend(['all','star','ring','well-mixed'],loc=4,numpoints=1)
#plt.xlim([float(fullyprob)-0.05,float(starprob)+0.05])
#plt.ylim([0,float(startime)+20])
#plt.ylabel("fixation time")
#plt.xlabel("fixation probability")
#plt.title("full plot size " + str(size))
#plt.subplots_adjust(bottom=0.17, left=0.14)
#plt.savefig('FULL' + str(size) + 'r2.png')
#plt.show()
