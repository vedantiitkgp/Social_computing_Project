#
# Undirected Scc Distribution. G(37939, 102004). Largest component has 0.665779 nodes (Mon Sep  9 03:54:08 2019)
#

set title "Undirected Scc Distribution. G(37939, 102004). Largest component has 0.665779 nodes"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Size of strongly connected component"
set ylabel "Number of components"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'scc.soc-Epinions1-subgraph.png'
plot 	"scc.soc-Epinions1-subgraph.tab" using 1:2 title "" with linespoints pt 6
