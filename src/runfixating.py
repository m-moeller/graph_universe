import numpy as np
import subprocess as sp

def runfixating(Bd,size,direction,r,option,option2,option3):
        #calculates the fixation probalitiy and time for a given graph
	output = sp.check_output('release/fixating'+' '+Bd+' '+size+' '+direction+' '+r+' '+option+' '+option2+' '+option3,shell=True)
	outputarr = output.split('\n')
	return outputarr

	
	
