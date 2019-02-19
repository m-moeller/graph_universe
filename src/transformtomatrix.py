import numpy as np

def transformtomatrix(string,size):
	#initialize array for the adjacency matrix
	admat = np.zeros([size,size],dtype=int)
	#extra counter for finding out which value from string has already been written into newarray
	k = 0
	#outer loop for going through the adjacency matrix 
	for j in range(0,size):
		#inner loop for going through a single row/line
		for i in range(0,size-j):
			#links to self or not
			if i == 0:
				admat[j,j] = 0
			#if not to self, write from string into admat
			else:
				admat[i+j,j] = int(string[k])
				admat[j,i+j] = int(string[k])
				k+=1
	string = ''
	adstring = admat.flatten()
	for j in range(0,len(adstring)):
		string += str(adstring[j])
	#print string	
	return admat,string
