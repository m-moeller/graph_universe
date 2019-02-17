#! /bin/bash
#rm gengsize7.txt
#rm adsize7.txt

#SBATCH --mail-user=mmoeller@evolbio.mpg.de
#SBATCH --mail-type=FAIL
#SBATCH --mem=1GB
#SBATCH --time=10-00:00
#SBATCH --job-name=fullgraph	   		 	    # Job Name
#SBATCH -t 10						    # Walltime (minutes)
#SBATCH -o ./%J.output.txt    		   		    # Output file
#SBATCH -e ./%J.error.txt	    	            	    # Error file
#SBATCH -N 1  	 					    # Number of nodes
#SBATCH -n 1  		 				    # Number of tasks
##rm gengsize4.txt
##rm adsize4.txt

#rm supvsamp/fixation_size_8_fitness_0_Bd_full.txt
#rm supvsamp/fixation_size_8_fitness_100_Bd_full.txt
#rm supvsamp/fixation_size_8_fitness_125_Bd_full.txt
#rm supvsamp/fixation_size_8_fitness_150_Bd_full.txt
#rm supvsamp/fixation_size_8_fitness_175_Bd_full.txt

#rm supvsamp/fixation_size_8_fitness_075_dB_full.txt
#rm supvsamp/fixation_size_8_fitness_100_dB_full.txt
#rm supvsamp/fixation_size_8_fitness_125_dB_full.txt
#rm supvsamp/fixation_size_8_fitness_150_dB_full.txt
#rm supvsamp/fixation_size_8_fitness_175_dB_full.txt

#geng 4 -c >> gengsize4.txt
#showg -a gengsize4.txt >> adsize4.txt
for i in {0..11117}

do
   
   admat=""
   for j in {1..8}
     do
     
     iterator=$((i * 10 + j +2))
     admat+=$(head -n "${iterator}" "../data/adsize8.txt" | tail -n 1)
     done
   if [ $(($i%1000)) == 0 ]
   then
	echo $(($i/1000))
	echo $SECONDS
	SECONDS=0
   fi   
   ./fixprob_small.bash $admat 8 >/dev/null
   
   #sleep 0.001	
done
