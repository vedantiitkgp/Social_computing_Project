#
# Undirected graph degree Distribution. G(37939, 102004). 5301 (0.1397) nodes with out-deg > avg deg (5.4), 3372 (0.0889) with >2*avg.deg (Mon Sep  9 04:36:04 2019)
#

set title "Undirected graph degree Distribution. G(37939, 102004). 5301 (0.1397) nodes with out-deg > avg deg (5.4), 3372 (0.0889) with >2*avg.deg"
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
set output 'outDeg.soc-Epinions1-subgraph.png'
plot 	"outDeg.soc-Epinions1-subgraph.tab" using 1:2 title "" with linespoints pt 6
