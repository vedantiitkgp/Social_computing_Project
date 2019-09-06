import snap 

# Taking input from text file 
G1 = snap.LoadEdgeList(snap.PUNGraph,"/home/vedant/Social_computing/Social_Epinions/soc-Epinions1.txt",0,1)

# Creating a new list with taking odd edges
new_list = []

for i in G1.Nodes():
	node = i.GetId()
	if(node%2!=0):
		new_list.append(node)

# Making it a set
new_list = set(new_list)
new_list = list(new_list)

v = snap.TIntV()

# Defining the snap vector
for i in range(len(new_list)):
	v.Add(new_list[i])

# Creating the subgraph
soc_epinions1_subgraph = snap.GetSubGraph(G1,v)

print "Number of nodes in soc-Epinions1-subgraph: " + str(len(v))

# Counting no of edges
edge =0
for i in soc_epinions1_subgraph.Edges():
	edge = edge +1

print "Number of edges in soc-Epinions1-subgraph: " + str(edge)

# Getting the degree distribution

CntV = snap.TIntPrV()

# Get degree distribution pairs (degree, count)
snap.GetDegCnt(soc_epinions1_subgraph, CntV)

print "Number of nodes of degree = 7 in soc-Epinions1-subgraph: " + str(CntV[6].GetVal2())

Mx_degree_id =[] 
result_degree = snap.TIntV() 
snap.GetDegSeqV(soc_epinions1_subgraph,result_degree)
for i in range(0, result_degree.Len()): 
	if(result_degree[i]==CntV[CntV.Len()-1].GetVal1()):
		Mx_degree_id.append(i)

print "Node id(s) with highest degree in soc-Epinions1-subgraph: " + str(Mx_degree_id)

# Plotting the degree distribution

snap.PlotOutDegDistr(soc_epinions1_subgraph, "soc-Epinions1-subgraph", "Undirected graph degree Distribution")

print "Degree distribution of soc-Epinions1-subgraph: " + str(outDeg.soc-Epinions1-subgraph.png)