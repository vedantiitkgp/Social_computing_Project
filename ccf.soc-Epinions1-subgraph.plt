#
# Undirected graph - clustering coefficient. G(37939, 102004). Average clustering: 0.0768  OpenTriads: 8596609 (0.9748)  ClosedTriads: 221969 (0.0252) (Mon Sep  9 03:54:09 2019)
#

set title "Undirected graph - clustering coefficient. G(37939, 102004). Average clustering: 0.0768  OpenTriads: 8596609 (0.9748)  ClosedTriads: 221969 (0.0252)"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Node degree"
set ylabel "Average clustering coefficient"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'ccf.soc-Epinions1-subgraph.png'
plot 	"ccf.soc-Epinions1-subgraph.tab" using 1:2 title "" with linespoints pt 6
