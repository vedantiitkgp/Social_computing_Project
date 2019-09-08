#
# Undirected graph degree Distribution. G(17226, 103954). 5471 (0.3176) nodes with out-deg > avg deg (12.1), 1994 (0.1158) with >2*avg.deg (Mon Sep  9 03:56:31 2019)
#

set title "Undirected graph degree Distribution. G(17226, 103954). 5471 (0.3176) nodes with out-deg > avg deg (12.1), 1994 (0.1158) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Out-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'outDeg.cit-HepPh-subgraph.png'
plot 	"outDeg.cit-HepPh-subgraph.tab" using 1:2 title "" with linespoints pt 6
