#
# Undirected graph - clustering coefficient. G(17226, 103954). Average clustering: 0.2522  OpenTriads: 2806109 (0.9490)  ClosedTriads: 150897 (0.0510) (Mon Sep  9 03:59:11 2019)
#

set title "Undirected graph - clustering coefficient. G(17226, 103954). Average clustering: 0.2522  OpenTriads: 2806109 (0.9490)  ClosedTriads: 150897 (0.0510)"
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
set output 'ccf.cit-Heph-subgraph.png'
plot 	"ccf.cit-Heph-subgraph.tab" using 1:2 title "" with linespoints pt 6
