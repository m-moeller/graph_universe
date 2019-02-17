import numpy as np

def transformtomatrix(string,size):
	#initialize array for the adjacency matrix
	admat = np.zeros(size**2,dtype=int)
	#extra counter for finding out which value from string has already been written into newarray
	k = 0
	#outer loop for going through the adjacency matrix 
	for j in range(0,size):
		#inner loop for going through a single row/line
		for i in range(0,size-j):
			#links to self or not
			if i == 0:
				admat[j*(size+1)] = 0
			#if not to self, write from string into admat
			else:
				admat[i+j*(size+1)] = int(string[k])
				admat[i*size+j*(size+1)] = int(string[k])
				k+=1
	string = ''
	for j in range(0,len(admat)):
		string += str(admat[j])
	#print string	
	return string
