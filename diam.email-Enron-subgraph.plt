#
# Undirected graph - shortest path. G(12231, 18453). Diam: avg:4.36  eff:5.49  max:14 (Mon Sep  9 04:02:16 2019)
#

set title "Undirected graph - shortest path. G(12231, 18453). Diam: avg:4.36  eff:5.49  max:14"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'diam.email-Enron-subgraph.png'
plot 	"diam.email-Enron-subgraph.tab" using 1:2 title "" with linespoints pt 6
