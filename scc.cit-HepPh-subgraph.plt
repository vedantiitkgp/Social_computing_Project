#
# Undirected Scc Distribution. G(17226, 103954). Largest component has 0.953036 nodes (Mon Sep  9 04:45:06 2019)
#

set title "Undirected Scc Distribution. G(17226, 103954). Largest component has 0.953036 nodes"
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
set output 'scc.cit-HepPh-subgraph.png'
plot 	"scc.cit-HepPh-subgraph.tab" using 1:2 title "" with linespoints pt 6
