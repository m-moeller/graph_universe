import numpy as np
import transformtomatrix as tfm
import igraph
import matplotlib
matplotlib.use('Agg')
#import degree_initialization as di
#import rand_degree_init as rdi
import runfixating as rf
#import degree_continuity as dc
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.backends.backend_pdf import PdfPages
from collections import OrderedDict

#psuppadstring = ['010000101111010111011011011101011110','0100000101000001011110010111001101100111010011110','0100000010100000010100000010111100010111000110110001110100011110','001000000001000000110100000001011111000101111000110111000111011000111101000111110']
#Strings for the adjacency matrices of the  'strong' suppressors from size 6 onwards
suppadstring = ['011000100100100011010011001101001110','0110000100100010001110100111001101100111010011110','0110000010010000100011110100111100110111001110110011110100111110','010010000101000000010100000001001111100001111000110111000111011000111101000111110','0100100000101000000001010000000010011111100001111100011011110001110111000111101100011111010001111110']
#Strings for the adjacency matrices of the l-graph (only exists for even numbers of nodes) from size 6 onwards
ladstring = ['011100100011100111101011011101011110','0','0111100010000111100111111010111110110111011110110111110101111110','0','0111110000100000111110011111111010111111101101111110111011110111110111011111101101111111010111111110']

#Size of the graph
size = 10
#Number of spots we evaluate the function
n = 1000
#Initialize some vectors to fill for various kinds of graphs
probs = np.zeros(n,dtype=float)
suppprobs = np.zeros(n,dtype=float)
lprobs = np.zeros(n,dtype=float)
fullyprobs = np.zeros(n,dtype=float)
ringprobs = np.zeros(n,dtype=float)
times = np.zeros(n,dtype=float)
supptimes = np.zeros(n,dtype=float)
ltimes = np.zeros(n,dtype=float)
fullytimes = np.zeros(n,dtype=float)
ringtimes = np.zeros(n,dtype=float)

#Initialize the fitness vector
r = np.zeros(n,dtype=float)

for k in range(0,n):
        r[k] = 0+k*0.01

        #calculate the fixation probability and time for the 'strong' suppressors
        outputsupp = rf.runfixating('Bd',str(size),'undirected',str(r[k]),'custom',suppadstring[size-6],'0')
        suppprobs[k] = outputsupp[1]
        supptimes[k] = outputsupp[3]
        
        #calculate the fixation probability and time for the l-graphs
        outputl = rf.runfixating('Bd',str(size),'undirected',str(r[k]),'custom',ladstring[size-6],'0')
        lprobs[k] = outputl[1]
        ltimes[k] = outputl[3]

        ##calculate the fixation probability and time for the fully connected graph as a reference
        outputfully = rf.runfixating('Bd',str(size),'undirected',str(r[k]),'ER','GNP','1')
        fullyprobs[k] = outputfully[1]
        fullytimes[k] = outputfully[3]

#Increase font size
plt.rcParams.update({'font.size': 22})

#Create plot
plot1 = plt.figure(1, figsize=(10.0,10.0))

#Plot 'strong' suppressor difference from fully connected graph
plt.plot(r[:],suppprobs[:]-fullyprobs[:],'b-')
#Plot l-graph difference from fully connected graph
plt.plot(r[:],lprobs[:]-fullyprobs[:],'m-')
#Plot lines to mark the spots where r=1 and where difference=0
plt.plot([1,1],[-0.5,0.5],'k--')
plt.plot([0.1,10],[0,0],'k--')

#Rescale to log plot for better viewing
plt.xscale('log')

#Set limits for the axes
plt.xlim([0.1,10])
plt.ylim([-0.010,0.005])

#save figure
plt.subplots_adjust(bottom=0.10, left=0.20)
plt.savefig('rvsphi_log_size' + str(size) + '.png')
