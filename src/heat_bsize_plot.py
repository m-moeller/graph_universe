import numpy as np
import transformtomatrix as tfm
import igraph
import matplotlib
matplotlib.use('Agg')
import degree_initialization as di
import rand_degree_init as rdi
import runfixating as rf
import heat_heterogeneity as het
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_pdf import PdfPages
from collections import OrderedDict
#generates heat heterogeneity vs fixation probability plot for a fixed degree distribution and size
#sizes are all the population sizes we want to look at
sizes = range(15,16)

#r = 1.25
#n is the number of graphs generated for the degree distribution
n = 100
#m is the number of different degree distributions that are tried; only relevant to make the correlation more reliable, not relevant for plotting
m = 1

for size in sizes:

        c=0
        while c!=m:  
                #rand_degree_init initializes a random degree distribution based on the Erdos-Renyi algorithm, with a given p
                degree1 = rdi.rand_degree_init(size,0.5)
                degree = degree1.tolist()[0]

                #probs, times, heat, admats are the fixation probability and time as well as the square root of the heat heterogeneity and the adjacency matrix, respectively
                probs = np.zeros([n,4],dtype=float)
                times = np.zeros([n,4],dtype=float)
                heat = np.zeros([n,4],dtype=float)
                admats = np.zeros([n,4,size,size],dtype=int)

                #h records whether a matrix could be generated based on the given degree distribution
                h = 0
                for k in range(0,n):
                        #call degree_init until it managed to generate a graph
                        while h == 0:
                                #degree_init  generates a graph based on a given degree distribution
                                admat = di.degree_init(size,degree)
                                if not isinstance(admat,(int,long)):
                                        h = 1
                        adflat = admat.flatten()
                        adstring = ''
                        for j in range(0,len(adflat)):
                            adstring += str(adflat[j])
                        #calculate the prob, time, admat and heat heterogeneity of the graph for a fitness of 0.5
                        output0 = rf.runfixating('Bd',str(size),'undirected','0.5','custom',adstring,'0')
                        probs[k,0] = output0[1]
                        times[k,0] = output0[3]
                        admats[k,0] = admat
                        heat[k][0] = het.het(admat)
                        
                        #calculate the prob, time, admat and heat heterogeneity of the graph for a fitness of 1.25
                        output1 = rf.runfixating('Bd',str(size),'undirected','1.25','custom',adstring,'0')
                        probs[k,1] = output1[1]
                        times[k,1] = output1[3]
                        admats[k,1] = admat
                        heat[k,1] = het.het(admat)
                        
                        #calculate the prob, time, admat and heat heterogeneity of the graph for a fitness of 2
                        output2 = rf.runfixating('Bd',str(size),'undirected','2','custom',adstring,'0')
                        probs[k,2] = output2[1]
                        times[k,2] = output2[3]
                        admats[k,2] = admat
                        heat[k,2] = het.het(admat)
                        
                        #calculate the prob, time, admat and heat heterogeneity of the graph for a fitness of 1.1
                        output3 = rf.runfixating('Bd',str(size),'undirected','1.1','custom',adstring,'0')
                        probs[k,3] = output3[1]
                        times[k,3] = output3[3]
                        admats[k,3] = admat
                        heat[k][3] = het.het(admat)
                        h = 0
                
                #throw out all duplicate graphs, only relevant for correlation
                #admatsnew = np.zeros([n,3,size,size],dtype=int)
                #probsnew = np.zeros([n,3],dtype=float)
                #heatnew = np.zeros([n,3],dtype=float)
                #l counts the number of unique graphs
                #l = np.zeros(3,dtype=int)
                #for x in range(0,3):
                #    for i in range(0,n):
                #        duplicate=0
                #        for j in range(0,n):
                #                g1 = igraph.Graph.Adjacency(admats[i][x].tolist())
                #                g2 = igraph.Graph.Adjacency(admatsnew[j][x].tolist())
                
                #                if g1.isomorphic(g2):
                #                        duplicate=1
                #        if duplicate==0:
                #                admatsnew[l[x]][x] = admats[i][x]
                #                probsnew[l[x]][x] = probs[i][x]
                #                heatnew[l[x]][x] = heat[i][x]
                #                l[x] = l[x]+1
                    #admatsnew2 = admatsnew[1:l]
                    #probsnew2 = probsnew[1:l]
                    #heatnew2 = heatnew[1:l]
                #print l
                #print probs[:,0],probs[:,1],probs[:,2]
                #plot everything
                #plt.plot(heat[:,1],probs[:,1],'bo')
                #plt.plot(heat[:,2],probs[:,2],'go')
                #if min(l)>10:
                #corr[c] = np.corrcoef(probsnew2[:],heatnew2[:])[0,1]
                        
                c = c+1
                
                #change font size of plot
                plt.rcParams.update({'font.size': 22})
                #initialize plot
                plot1 = plt.figure(1, figsize=(10.0,10.0))
                #Plot heat heterogeneity against fixation probability
                plt.plot(heat[:,0],probs[:,0],'o', color = '0.5')
                #set axis limits
                plt.ylim([min(probs[:,0])-(max(probs[:,0])-min(probs[:,0]))*0.1,max(probs[:,0])+(max(probs[:,0])-min(probs[:,0]))*0.1])               
                plt.xlim([0.03,0.13])
                #change ticks
                ax = plt.gca()
                ax.xaxis.set_tick_params(width=2)
                ax.xaxis.set_tick_params(length=10)
                ax.yaxis.set_tick_params(width=2)
                ax.yaxis.set_tick_params(length=10)
                ax.set_xticks(np.round(np.linspace(0.03, 0.13, 6), 2))
                #label axis
                plt.xlabel("heat heterogeneity")
                plt.ylabel("fixation probability")
                #save and close figure
                plt.savefig('heterogeneity_r_05_size' + str(size) + '.png',bbox_inches='tight')
                plt.clf()
                
                #Initialize figure
                plot1 = plt.figure(1, figsize=(10.0,10.0))
                #Plot heat heterogeneity against fixation probability
                plt.plot(heat[:,1],probs[:,1],'o', color = '0.5')
                #set axis limits
                plt.ylim([min(probs[:,1])-(max(probs[:,1])-min(probs[:,1]))*0.1,max(probs[:,1])+(max(probs[:,1])-min(probs[:,1]))*0.1])
                plt.xlim([0.03,0.13])
                #change ticks
                ax = plt.gca()
                ax.xaxis.set_tick_params(width=2)
                ax.xaxis.set_tick_params(length=10)
                ax.yaxis.set_tick_params(width=2)
                ax.yaxis.set_tick_params(length=10)
                ax.set_xticks(np.round(np.linspace(0.03, 0.13, 6), 2))
                #label axis
                plt.xlabel("heat heterogeneity")
                plt.ylabel("fixation probability")
                #save and close figure
                plt.savefig('heterogeneity_r_125_size' + str(size) + '.png',bbox_inches='tight')
                plt.clf()
                
                #Initialize plot
                plot1 = plt.figure(1, figsize=(10.0,10.0))
                #Plot heat heterogeneity against fixation probalitiy
                plt.plot(heat[:,2],probs[:,2],'o', color = '0.5')
                #set axis limits
                plt.ylim([min(probs[:,2])-(max(probs[:,2])-min(probs[:,2]))*0.1,max(probs[:,2])+(max(probs[:,2])-min(probs[:,2]))*0.1])                
                plt.xlim([0.03,0.13])
                #change ticks
                ax = plt.gca()
                ax.xaxis.set_tick_params(width=2)
                ax.xaxis.set_tick_params(length=10)
                ax.yaxis.set_tick_params(width=2)
                ax.yaxis.set_tick_params(length=10)
                ax.set_xticks(np.round(np.linspace(0.03, 0.13, 6), 2))
                #laben acis
                plt.xlabel("heat heterogeneity")
                plt.ylabel("fixation probability")
                #save and close figure
                plt.savefig('heterogeneity_r_2_size' + str(size) + '.png',bbox_inches='tight')
                plt.clf()
                
                #Initialize figure
                plot1 = plt.figure(1, figsize=(10.0,10.0))
                #plot heat heterogeneity against fixation probability
                plt.plot(heat[:,3],probs[:,3],'o', color = '0.5')
                #set axis limits
                plt.ylim([min(probs[:,3])-(max(probs[:,3])-min(probs[:,3]))*0.1,max(probs[:,3])+(max(probs[:,3])-min(probs[:,3]))*0.1])                
                plt.xlim([0.03,0.13])
                #change ticks
                ax = plt.gca()
                ax.xaxis.set_tick_params(width=2)
                ax.xaxis.set_tick_params(length=10)
                ax.yaxis.set_tick_params(width=2)
                ax.yaxis.set_tick_params(length=10)
                ax.set_xticks(np.round(np.linspace(0.03, 0.13, 6), 2))
                #label axis
                plt.xlabel("heat heterogeneity")
                plt.ylabel("fixation probability")
                #save and close figures
                plt.savefig('heterogeneity_r_11_size' + str(size) + '.png',bbox_inches='tight')
                plt.clf()
        #corrtotal = sum(corr)/m
        #print corr
        #print corrtotal
