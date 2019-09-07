import snap
import statistics

# Taking input from text file 
G1 = snap.LoadEdgeList(snap.PUNGraph,"/home/vedant/Social_computing/Social_Epinions/soc-Epinions1.txt",0,1)
G2 = snap.LoadEdgeList(snap.PUNGraph, "/home/vedant/Social_computing/Citation_network/Cit-HepPh.txt", 0, 1)
G3 = snap.LoadEdgeList(snap.PUNGraph, "/home/vedant/Social_computing/Enron_email_network/Email-Enron.txt", 0, 1)
G4 = snap.LoadEdgeList(snap.PUNGraph, "/home/vedant/Social_computing/P2P_gutella_network/p2p-Gnutella04.txt", 0, 1)

#Taking Input of which sub graph to proceed
 
sub_graph_name = input("Enter the name of subgraph")

###Task 1

##Task 1.1
if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Creating a new list with taking odd edges
	list1 = []

	for i in G1.Nodes():
		node = i.GetId()
		if(node%2!=0):
			list1.append(node)

	# Making it a set
	list1 = set(list1)
	list1 = list(list1)

	v1 = snap.TIntV()

	# Defining the snap vector
	for i in range(len(list1)):
		v1.Add(list1[i])

	# Creating the subgraph
	soc_epinions1_subgraph = snap.GetSubGraph(G1,v1)
	print "Number of nodes in soc-Epinions1-subgraph: " + str(len(v1))

if(sub_graph_name=="cit-HepPh-subgraph"):
	# Creating a new list with taking even edges
	list2 = []

	for i in G2.Nodes():
		node = i.GetId()
		if(node%2==0):
			list2.append(node)

	# Making it a set
	list2 = set(list2)
	list2 = list(list2)

	v2 = snap.TIntV()

	# Defining the snap vector
	for i in range(len(list2)):
		v2.Add(list2[i])

	# Creating the subgraph
	cit_heph_subgraph = snap.GetSubGraph(G2,v2)
	print "Number of nodes in cit-Heph-subgraph: " + str(len(v2))

if(sub_graph_name=="email-Enron-subgraph"):
	# Creating a new list with taking  edges multiple of 3
	list3 = []

	for i in G3.Nodes():
		node = i.GetId()
		if(node%3==0):
			list3.append(node)

	# Making it a set
	list3 = set(list3)
	list3 = list(list3)

	v3 = snap.TIntV()

	# Defining the snap vector
	for i in range(len(list3)):
		v3.Add(list3[i])

	# Creating the subgraph
	email_enron_subgraph = snap.GetSubGraph(G3,v3)
	print "Number of nodes in email-Enron-subgraph: " + str(len(v3))
if(sub_graph_name=="p2p-Gnutella04-subgraph"):

	list4=[]
	for i in G4.nodes():
		node = i.GetId()
		list4.append(node)

	# Making it a set
	list4 = set(list4)
	list4 = list(list4)

	v4 = snap.TIntV()

	# Defining the snap vector
	for i in range(len(list4)):
		v4.Add(list4[i])

	p2p_gnutella04_subgraph = G4
	print "Number of nodes in p2p-Gnutella04-subgraph: " + str(len(v4))

## Task 1.2

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Counting no of edges
	edge =0
	for i in soc_epinions1_subgraph.Edges():
		edge = edge +1
	print "Number of edges in soc-Epinions1-subgraph: " + str(edge)
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Counting no of edges
	edge =0
	for i in cit_heph_subgraph.Edges():
		edge = edge +1
	print "Number of edges in cit-Heph-subgraph: " + str(edge)
if(sub_graph_name=="email-Enron-subgraph"):
	# Counting no of edges
	edge =0
	for i in email_enron_subgraph.Edges():
		edge = edge +1
	print "Number of edges in email-Enron-subgraph: " + str(edge)
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Counting no of edges
	edge =0
	for i in p2p_gnutella04_subgraph.Edges():
		edge = edge +1
	print "Number of edges in p2p-Gnutella04-subgraph: " + str(edge)

### Task 2

## Task 2.1

if(sub_graph_name=="soc-Epinions1-subgraph"):
	CntV1 = snap.TIntPrV()

	# Get degree distribution pairs (degree, count)
	snap.GetDegCnt(soc_epinions1_subgraph, CntV1)

	print "Number of nodes of degree = 7 in soc-Epinions1-subgraph: " + str(CntV1[6].GetVal2())
if(sub_graph_name=="cit-Heph-subgraph"):
	CntV2 = snap.TIntPrV()

	# Get degree distribution pairs (degree, count)
	snap.GetDegCnt(cit_heph_subgraph, CntV2)

	print "Number of nodes of degree = 7 in cit-Heph-subgraph: " + str(CntV2[6].GetVal2())
if(sub_graph_name=="email-Enron-subgraph"):
	CntV3 = snap.TIntPrV()

	# Get degree distribution pairs (degree, count)
	snap.GetDegCnt(email_enron_subgraph, CntV3)

	print "Number of nodes of degree = 7 in email-Enron-subgraph: " + str(CntV3[6].GetVal2())
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	CntV4 = snap.TIntPrV()

	# Get degree distribution pairs (degree, count)
	snap.GetDegCnt(p2p_gnutella04_subgraph, CntV4)

	print "Number of nodes of degree = 7 in p2p-Gnutella04-subgraph: " + str(CntV4[6].GetVal2())

##Task 2.2
if(sub_graph_name=="soc-Epinions1-subgraph"):
	Mx_degree_id =[] 
	result_degree = snap.TIntV() 
	snap.GetDegSeqV(soc_epinions1_subgraph,result_degree)
	for i in range(0, result_degree.Len()): 
		if(result_degree[i]==CntV1[CntV1.Len()-1].GetVal1()):
			Mx_degree_id.append(i)

	print "Node id(s) with highest degree in soc-Epinions1-subgraph: " + str(Mx_degree_id)
if(sub_graph_name=="cit-Heph-subgraph"):
	Mx_degree_id =[] 
	result_degree = snap.TIntV() 
	snap.GetDegSeqV(cit_heph_subgraph,result_degree)
	for i in range(0, result_degree.Len()): 
		if(result_degree[i]==CntV2[CntV2.Len()-1].GetVal1()):
			Mx_degree_id.append(i)

	print "Node id(s) with highest degree in cit-Heph-subgraph: " + str(Mx_degree_id)
if(sub_graph_name=="email-Enron-subgraph"):
	Mx_degree_id =[] 
	result_degree = snap.TIntV() 
	snap.GetDegSeqV(email-Enron-subgraph,result_degree)
	for i in range(0, result_degree.Len()): 
		if(result_degree[i]==CntV3[CntV3.Len()-1].GetVal1()):
			Mx_degree_id.append(i)

	print "Node id(s) with highest degree in email-Enron-subgraph: " + str(Mx_degree_id)
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	Mx_degree_id =[] 
	result_degree = snap.TIntV() 
	snap.GetDegSeqV(p2p_gnutella04_subgraph,result_degree)
	for i in range(0, result_degree.Len()): 
		if(result_degree[i]==CntV4[CntV4.Len()-1].GetVal1()):
			Mx_degree_id.append(i)

	print "Node id(s) with highest degree in email-Enron-subgraph: " + str(Mx_degree_id)
## Task 2.3
if(sub_graph_name=="soc-Epinions1-subgraph"):

	# Plotting the degree distribution

	#snap.PlotOutDegDistr(soc_epinions1_subgraph, "soc-Epinions1-subgraph", "Undirected graph degree Distribution")
	print "Degree distribution of soc-Epinions1-subgraph: " + "outDeg.soc-Epinions1-subgraph.png"
if(sub_graph_name=="cit-Heph-subgraph"):

	# Plotting the degree distribution
	
	#snap.PlotOutDegDistr(cit_heph_subgraph, "cit-Heph-subgraph", "Undirected graph degree Distribution")
	print "Degree distribution of cit-Heph-subgraph: " + "outDeg.cit-Heph-subgraph.png"
if(sub_graph_name=="email-Enron-subgraph"):

	# Plotting the degree distribution
	
	#snap.PlotOutDegDistr(email_enron_subgraph, "email-Enron-subgraph", "Undirected graph degree Distribution")
	print "Degree distribution of email-Enron-subgraph: " + "outDeg.email-Enron-subgraph.png"
if(sub_graph_name=="p2p-Gnutella04-subgraph"):

	# Plotting the degree distribution
	
	#snap.PlotOutDegDistr(p2p_gnutella04_subgraph, "p2p-Gnutella04-subgraph", "Undirected graph degree Distribution")
	print "Degree distribution of p2p-Gnutella04-subgraph: " + "outDeg.p2p-Gnutella04-subgraph.png"

### Task 3

## Task 3.1
if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Calculating the full diameter 
	print "Approximate full diameter in soc-Epinions1-subgraph with sampling 10 nodes: " + str(snap.GetBfsFullDiam(soc_epinions1_subgraph, 10))
	print "Approximate full diameter in soc-Epinions1-subgraph with sampling 100 nodes: " + str(snap.GetBfsFullDiam(soc_epinions1_subgraph, 100))
	print "Approximate full diameter in soc-Epinions1-subgraph with sampling 1000 nodes: " + str(snap.GetBfsFullDiam(soc_epinions1_subgraph, 1000))

	value = [snap.GetBfsFullDiam(soc_epinions1_subgraph, 10),snap.GetBfsFullDiam(soc_epinions1_subgraph, 100),snap.GetBfsFullDiam(soc_epinions1_subgraph, 1000)]

	print "Approximate full diameter in soc-Epinions1-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value),2)) + "," + str(round(statistics.variance(value),2))
if(sub_graph_name=="cit-Heph-subgraph"):
	# Calculating the full diameter 
	print "Approximate full diameter in cit-Heph-subgraph with sampling 10 nodes: " + str(snap.GetBfsFullDiam(cit_heph_subgraph, 10))
	print "Approximate full diameter in cit-Heph-subgraph with sampling 100 nodes: " + str(snap.GetBfsFullDiam(cit_heph_subgraph, 100))
	print "Approximate full diameter in cit-Heph-subgraph with sampling 1000 nodes: " + str(snap.GetBfsFullDiam(cit_heph_subgraph, 1000))

	value = [snap.GetBfsFullDiam(cit_heph_subgraph, 10),snap.GetBfsFullDiam(cit_heph_subgraph, 100),snap.GetBfsFullDiam(cit_heph_subgraph, 1000)]

	print "Approximate full diameter in cit-Heph-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value),2)) + "," + str(round(statistics.variance(value),2))
if(sub_graph_name=="email-Enron-subgraph"):
	# Calculating the full diameter 
	print "Approximate full diameter in email-Enron-subgraph with sampling 10 nodes: " + str(snap.GetBfsFullDiam(email_enron_subgraph, 10))
	print "Approximate full diameter in email-Enron-subgraph with sampling 100 nodes: " + str(snap.GetBfsFullDiam(email_enron_subgraph, 100))
	print "Approximate full diameter in email-Enron-subgraph with sampling 1000 nodes: " + str(snap.GetBfsFullDiam(email_enron_subgraph, 1000))

	value = [snap.GetBfsFullDiam(email_enron_subgraph, 10),snap.GetBfsFullDiam(email_enron_subgraph, 100),snap.GetBfsFullDiam(email_enron_subgraph, 1000)]

	print "Approximate full diameter in email-Enron-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value),2)) + "," + str(round(statistics.variance(value),2))
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Calculating the full diameter 
	print "Approximate full diameter in p2p-Gnutella04-subgraph with sampling 10 nodes: " + str(snap.GetBfsFullDiam(p2p_gnutella04_subgraph, 10))
	print "Approximate full diameter in p2p-Gnutella04-subgraph with sampling 100 nodes: " + str(snap.GetBfsFullDiam(p2p_gnutella04_subgraph, 100))
	print "Approximate full diameter in p2p-Gnutella04-subgraph with sampling 1000 nodes: " + str(snap.GetBfsFullDiam(p2p_gnutella04_subgraph, 1000))

	value = [snap.GetBfsFullDiam(p2p_gnutella04_subgraph, 10),snap.GetBfsFullDiam(p2p_gnutella04_subgraph, 100),snap.GetBfsFullDiam(p2p_gnutella04_subgraph, 1000)]

	print "Approximate full diameter in p2p-Gnutella04-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value),2)) + "," + str(round(statistics.variance(value),2))

## Task 3.2

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Calculating the effective diameter

	print "Approximate Effective diameter in soc-Epinions1-subgraph with sampling 10 nodes: " + str(round(snap.GetBfsEffDiam(soc_epinions1_subgraph,10,v1,True)[0],3))
	print "Approximate Effective diameter in soc-Epinions1-subgraph with sampling 100 nodes: " + str(round(snap.GetBfsEffDiam(soc_epinions1_subgraph,100,v1,True)[0],3))
	print "Approximate Effective diameter in soc-Epinions1-subgraph with sampling 1000 nodes: " + str(round(snap.GetBfsEffDiam(soc_epinions1_subgraph,1000,v1,True)[0],3))

	value_new = [snap.GetBfsEffDiam(soc_epinions1_subgraph,10,v1,True)[0],snap.GetBfsEffDiam(soc_epinions1_subgraph,100,v1,True)[0],snap.GetBfsEffDiam(soc_epinions1_subgraph,1000,v1,True)[0]]

	print "Approximate Effective diameter in soc-Epinions1-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value_new),3)) + "," + str(round(statistics.variance(value_new),4))
if(sub_graph_name=="cit-Heph-subgraph"):
	# Calculating the effective diameter

	print "Approximate Effective diameter in cit-Heph-subgraph with sampling 10 nodes: " + str(round(snap.GetBfsEffDiam(cit_heph_subgraph,10,v2,True)[0],3))
	print "Approximate Effective diameter in cit-Heph-subgraph with sampling 100 nodes: " + str(round(snap.GetBfsEffDiam(cit_heph_subgraph,100,v2,True)[0],3))
	print "Approximate Effective diameter in cit-Heph-subgraph with sampling 1000 nodes: " + str(round(snap.GetBfsEffDiam(cit_heph_subgraph,1000,v2,True)[0],3))

	value_new = [snap.GetBfsEffDiam(cit_heph_subgraph,10,v2,True)[0],snap.GetBfsEffDiam(cit_heph_subgraph,100,v2,True)[0],snap.GetBfsEffDiam(cit_heph_subgraph,1000,v2,True)[0]]

	print "Approximate Effective diameter in cit-Heph-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value_new),3)) + "," + str(round(statistics.variance(value_new),4))
if(sub_graph_name=="email-Enron-subgraph"):
	# Calculating the effective diameter

	print "Approximate Effective diameter in email-Enron-subgraph with sampling 10 nodes: " + str(round(snap.GetBfsEffDiam(email_enron_subgraph,10,v3,True)[0],3))
	print "Approximate Effective diameter in email-Enron-subgraph with sampling 100 nodes: " + str(round(snap.GetBfsEffDiam(email_enron_subgraph,100,v3,True)[0],3))
	print "Approximate Effective diameter in email-Enron-subgraph with sampling 1000 nodes: " + str(round(snap.GetBfsEffDiam(email_enron_subgraph,1000,v3,True)[0],3))

	value_new = [snap.GetBfsEffDiam(email_enron_subgraph,10,v3,True)[0],snap.GetBfsEffDiam(email_enron_subgraph,100,v3,True)[0],snap.GetBfsEffDiam(email_enron_subgraph,1000,v3,True)[0]]

	print "Approximate Effective diameter in email-Enron-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value_new),3)) + "," + str(round(statistics.variance(value_new),4))
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Calculating the effective diameter

	print "Approximate Effective diameter in p2p-Gnutella04-subgraph with sampling 10 nodes: " + str(round(snap.GetBfsEffDiam(p2p_gnutella04_subgraph,10,v4,True)[0],3))
	print "Approximate Effective diameter in p2p-Gnutella04-subgraph with sampling 100 nodes: " + str(round(snap.GetBfsEffDiam(p2p_gnutella04_subgraph,100,v4,True)[0],3))
	print "Approximate Effective diameter in p2p-Gnutella04-subgraph with sampling 1000 nodes: " + str(round(snap.GetBfsEffDiam(p2p_gnutella04_subgraph,1000,v4,True)[0],3))

	value_new = [snap.GetBfsEffDiam(p2p_gnutella04_subgraph,10,v4,True)[0],snap.GetBfsEffDiam(p2p_gnutella04_subgraph,100,v4,True)[0],snap.GetBfsEffDiam(p2p_gnutella04_subgraph,1000,v4,True)[0]]

	print "Approximate Effective diameter in p2p-Gnutella04-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value_new),3)) + "," + str(round(statistics.variance(value_new),4))

## Task 3.3

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Plotting the distribution of shortest Length

	#snap.PlotShortPathDistr(soc_epinions1_subgraph,"soc-Epinions1-subgraph","Undirected graph - shortest path")
	print "Shortest path distribution of soc-Epinions1-subgraph is in :" + "diam.soc-Epinions1-subgraph.png"
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Plotting the distribution of shortest Length

	#snap.PlotShortPathDistr(cit_heph_subgraph,"cit-Heph-subgraph","Undirected graph - shortest path")
	print "Shortest path distribution of cit-Heph-subgraph is in :" + "diam.cit-Heph-subgraph.png"
if(sub_graph_name=="email-Enron-subgraph"):
	# Plotting the distribution of shortest Length

	#snap.PlotShortPathDistr(email_enron_subgraph,"email-Enron-subgraph","Undirected graph - shortest path")
	print "Shortest path distribution of email-Enron-subgraph is in :" + "diam.email-Enron-subgraph.png"
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Plotting the distribution of shortest Length

	#snap.PlotShortPathDistr(p2p_gnutella04_subgraph,"p2p-Gnutella04-subgraph","Undirected graph - shortest path")
	print "Shortest path distribution of p2p-Gnutella04-subgraph is in :" + "diam.p2p-Gnutella04-subgraph.png"

### Task 4

## Task 4.1

if(sub_graph_name=="soc-Epinions1-subgraph"):

	# Finding the components of the network
	# Calculating the fraction of largest connected component

	largest_connected = snap.GetMxScc(soc_epinions1_subgraph)

	node=0
	for i in largest_connected.Nodes():
		node = node + 1

	print "Fraction of nodes in largest connected component in soc-Epinions1-subgraph :" + str(round(node*1.0/len(v1),3))

if(sub_graph_name=="cit-Heph-subgraph"):

	# Finding the components of the network
	# Calculating the fraction of largest connected component

	largest_connected = snap.GetMxScc(cit_heph_subgraph)

	node=0
	for i in largest_connected.Nodes():
		node = node + 1

	print "Fraction of nodes in largest connected component in cit-Heph-subgraph :" + str(round(node*1.0/len(v2),3))
if(sub_graph_name=="email-Enron-subgraph"):

	# Finding the components of the network
	# Calculating the fraction of largest connected component

	largest_connected = snap.GetMxScc(email_enron_subgraph)

	node=0
	for i in largest_connected.Nodes():
		node = node + 1

	print "Fraction of nodes in largest connected component in email-Enron-subgraph :" + str(round(node*1.0/len(v3),3))
if(sub_graph_name=="p2p-Gnutella04-subgraph"):

	# Finding the components of the network
	# Calculating the fraction of largest connected component

	largest_connected = snap.GetMxScc(p2p_gnutella04_subgraph)

	node=0
	for i in largest_connected.Nodes():
		node = node + 1

	print "Fraction of nodes in largest connected component in p2p-Gnutella04-subgraph :" + str(round(node*1.0/len(v4),3))

## Task 4.2

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Getting no of edge bridges in th network
	EdgeV = snap.TIntPrV()
	snap.GetEdgeBridges(soc_epinions1_subgraph, EdgeV)

	edge_bridge = 0
	for i in EdgeV:
		edge_bridge = edge_bridge +1
	print "Number of edge bridges in soc-Epinions1-subgraph :" + str(edge_bridge)
if(sub_graph_name=="cit-Heph-subgraph"):
	# Getting no of edge bridges in th network
	EdgeV = snap.TIntPrV()
	snap.GetEdgeBridges(cit_heph_subgraph, EdgeV)

	edge_bridge = 0
	for i in EdgeV:
		edge_bridge = edge_bridge +1
	print "Number of edge bridges in cit-Heph-subgraph :" + str(edge_bridge)
if(sub_graph_name=="email-Enron-subgraph"):
	# Getting no of edge bridges in th network
	EdgeV = snap.TIntPrV()
	snap.GetEdgeBridges(email_enron_subgraph, EdgeV)

	edge_bridge = 0
	for i in EdgeV:
		edge_bridge = edge_bridge +1
	print "Number of edge bridges in email-Enron-subgraph :" + str(edge_bridge)
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Getting no of edge bridges in th network
	EdgeV = snap.TIntPrV()
	snap.GetEdgeBridges(p2p_gnutella04_subgraph, EdgeV)

	edge_bridge = 0
	for i in EdgeV:
		edge_bridge = edge_bridge +1
	print "Number of edge bridges in p2p-Gnutella04-subgraph :" + str(edge_bridge)

# Calculating no of Articulation points 

ArtNIdV = snap.TIntV()
snap.GetArtPoints(soc_epinions1_subgraph, ArtNIdV)

art_point=0
for NI in ArtNIdV:
	art_point = art_point +1

