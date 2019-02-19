# graph_universe
This code contains various python and bash files to generate the data and the figures in <a href="https://arxiv.org/abs/1810.12807"><b>"Exploring and mapping the universe of evolutionary graphs"</b></a> by <i>Marius Möller, Laura Hindersin</i> and <i> Arne Traulsen</i>.

## Dependencies
The 'fixating' file has to be compiled based on <a href="https://github.com/hindersin/efficientFixation/blob/master/README.md"><b>Exact numerical calculation of fixation probability and time on graphs.</b></a> by <i>Laura Hindersin, Marius Möller, Arne Traulsen</i> and <i>Benedikt Bauer</i> to use most of the code properly.
Furthermore, the software "geng" from the <a href="http://pallini.di.uniroma1.it/"><b>"nauty and tracer suite"</b></a> is required to generate all graphs of a certain size efficiently.

## Description of files

'fixprob_calc.bash' generates the data files for the fixation time and probability most of the python functions are based on to generate the figures.<br>
'create_graph.py' generates a figure for a single specific graph.<br>
'geneticalgo_local.py' runs the genetic algorithm as described in the paper.<br>
'heat_bsize_plot.py' generates the figures with the heat heterogeneity for the bigger sizes where it is not possible anymore to look at all graphs.<br>
'heat_full_plot.py' generates the figures with the heat heterogeneity for the smaller sizes where it is possible to look at all graphs.<br>
'rvsphi.py' generates the figures to compare the fitness against the fixation probability for certain graphs, like the detour graph and the l-graph.<br>
'transitionsplotting.py' generates the figures to compare the fixation probability against time for different sizes, updating mechanisms etc. .<br>
The other python files are simply helping functions for these main files.<br>


## Usage

The main python files can directly be run as long as the dependencies have been downloaded. If you should want to change something, you need to do so inside the file, but most lines are commented.

## License

See <i>LICENSE</i> for details.
