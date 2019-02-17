#! /bin/bash

Update="Bd"			# Update Rule --- 'Bd' for birth in first step according to fitness, death in second step random choice || 'dB' accordingly the other way round
popSize="16"			# Population Size
direction="undirected"		# directedness of the graph --- possible values: 'undirected' or 'directed'
fitness="2" 			# fitness of the mutants
category="custom"			# category of the graph: 'ER' for Erdos-Reny, 'BB' for Barabasi-Albert, 'WS' for Watts-Strogatz, 'geo' for geometric or 'custom' for a custom graph 
arg1=0111111110000000100000000111111110000000000000001000000000000000100000000000000010000000000000001000000000000000100000000000000010000000000000000100000000000000010000000000000001000000000000000100000000000000010000000000000001000000000000000100000000000000	# secondary parameter for the category of graph: 'GNM' or 'GNP' for Erdos Reny, double power of preference for Barabasi, int dimension for small world, bool periodic for geometric, adjacency matrix as a string of numbers for custom
echo ${#arg1}
arg2=0			# tertiary parameter for the category of graph: probability for every edge in Erdos-Reny GNP and geometric, number of edges for Erdos-Reny GNM, m for Barabasi, probability of rewiring for small world, 0 for custom
#output="conditional"  		#possible values: 'probability', 'conditional', 'unconditional' and 'all'
./fixating $Update $popSize $direction $fitness $category $arg1 $arg2 #$output
