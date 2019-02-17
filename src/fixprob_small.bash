#! /bin/bash
#rm gengsize7.txt
#rm adsize7.txt

##SBATCH --mail-user=mmoeller@evolbio.mpg.de
##SBATCH --mail-type=FAIL
#SBATCH --mem=1GB
#SBATCH --time=10-00:00
#SBATCH --job-name=fullgraph	   		 	    # Job Name
#SBATCH -t 10						    # Walltime (minutes)
#SBATCH -o ./slurmoutput/%J.output.txt    		    # Output file
##SBATCH -e ./%J.error.txt	    	            	    # Error file
#SBATCH -N 1  	 					    # Number of nodes
#SBATCH -n 1  		 				    # Number of tasks

admat=$1
#fit=$2
#evol=$3
size=$2
#line=$3

#directory='../data/fixation_size_'
#directory+=$size
#directory+='_fitness_'
#directory+=$fit
#directory+='_'
#directory+=$evol
#directory+='_full.txt'
#echo $directory
#output=$(./release/fixating $evol $size undirected $fit custom $admat 0) #>> $directory
#output2=${line}i${output} 

./release/fixating Bd $size undirected 0.55 custom $admat 0 >> ../data/fixation_size_8_fitness_055_Bd_full.txt
./release/fixating Bd $size undirected 0.65 custom $admat 0 >> ../data/fixation_size_8_fitness_065_Bd_full.txt
./release/fixating Bd $size undirected 0.75 custom $admat 0 >> ../data/fixation_size_8_fitness_075_Bd_full.txt
./release/fixating Bd $size undirected 0.85 custom $admat 0 >> ../data/fixation_size_8_fitness_085_Bd_full.txt
./release/fixating Bd $size undirected 0.95 custom $admat 0 >> ../data/fixation_size_8_fitness_095_Bd_full.txt
./release/fixating Bd $size undirected 1.05 custom $admat 0 >> ../data/fixation_size_8_fitness_105_Bd_full.txt
./release/fixating Bd $size undirected 1.15 custom $admat 0 >> ../data/fixation_size_8_fitness_115_Bd_full.txt

./release/fixating Bd $size undirected 1.25 custom $admat 0 >> ../data/fixation_size_8_fitness_125_Bd_full.txt
./release/fixating Bd $size undirected 1.35 custom $admat 0 >> ../data/fixation_size_8_fitness_135_Bd_full.txt
./release/fixating Bd $size undirected 1.45 custom $admat 0 >> ../data/fixation_size_8_fitness_145_Bd_full.txt
./release/fixating Bd $size undirected 1.55 custom $admat 0 >> ../data/fixation_size_8_fitness_155_Bd_full.txt
./release/fixating Bd $size undirected 1.65 custom $admat 0 >> ../data/fixation_size_8_fitness_165_Bd_full.txt
./release/fixating Bd $size undirected 1.75 custom $admat 0 >> ../data/fixation_size_8_fitness_175_Bd_full.txt
./release/fixating Bd $size undirected 1.85 custom $admat 0 >> ../data/fixation_size_8_fitness_185_Bd_full.txt
./release/fixating Bd $size undirected 1.95 custom $admat 0 >> ../data/fixation_size_8_fitness_195_Bd_full.txt
#./release/fixating Bd $size undirected 2.0 custom $admat 0 >> ../data/fixation_size_8_fitness_200_Bd_full.txt

#unset directory
unset admat
#unset fit
#unset evol
unset size
#unset line
#unset output

