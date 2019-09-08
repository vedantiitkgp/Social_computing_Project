#
# Undirected graph degree Distribution. G(12231, 18453). 1902 (0.1555) nodes with out-deg > avg deg (3.0), 1060 (0.0867) with >2*avg.deg (Mon Sep  9 04:46:01 2019)
#

set title "Undirected graph degree Distribution. G(12231, 18453). 1902 (0.1555) nodes with out-deg > avg deg (3.0), 1060 (0.0867) with >2*avg.deg"
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
set output 'outDeg.email-Enron-subgraph.png'
plot 	"outDeg.email-Enron-subgraph.tab" using 1:2 title "" with linespoints pt 6
