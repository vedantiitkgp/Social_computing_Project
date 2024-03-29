import snap
import statistics

# Taking input from text file 
G1 = snap.LoadEdgeList(snap.PUNGraph,"/home/vedant/Social_computing/Social_Epinions/soc-Epinions1.txt",0,1)
G2 = snap.LoadEdgeList(snap.PUNGraph, "/home/vedant/Social_computing/Citation_network/Cit-HepPh.txt", 0, 1)
G3 = snap.LoadEdgeList(snap.PUNGraph, "/home/vedant/Social_computing/Enron_email_network/Email-Enron.txt", 0, 1)
G4 = snap.LoadEdgeList(snap.PUNGraph, "/home/vedant/Social_computing/P2P_gutella_network/p2p-Gnutella04.txt", 0, 1)

#Taking Input of which sub graph to proceed
 
sub_graph_name = raw_input("Enter the name of subgraph ")

#### Task 1

### Task 1.1

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
	snap.SaveEdgeList(soc_epinions1_subgraph, "soc-Epinions1-subgraph-edge.txt", "Save as tab-separated list of edges")
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
	snap.SaveEdgeList(cit_heph_subgraph, "cit-Heph-subgraph-edge.txt", "Save as tab-separated list of edges")
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
	snap.SaveEdgeList(email_enron_subgraph, "email-Enron-subgraph-edge.txt", "Save as tab-separated list of edges")
if(sub_graph_name=="p2p-Gnutella04-subgraph"):

	list4=[]
	for i in G4.Nodes():
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
	snap.SaveEdgeList(p2p_gnutella04_subgraph, "p2p-Gnutella04-subgraph-edge.txt", "Save as tab-separated list of edges")

### Task 1.2

## Task 1.2.1

# Task 1.2.1.1
if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Calculating no of nodes
	print "Number of nodes in soc-Epinions1-subgraph: " + str(len(v1))

if(sub_graph_name=="cit-HepPh-subgraph"):
	# Calculating no of nodes
	print "Number of nodes in cit-HepPh-subgraph: " + str(len(v2))

if(sub_graph_name=="email-Enron-subgraph"):
	# Calculating no of nodes
	print "Number of nodes in email-Enron-subgraph: " + str(len(v3))
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Calculating no of nodes
	print "Number of nodes in p2p-Gnutella04-subgraph: " + str(len(v4))

# Task 1.2.1.2

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
	print "Number of edges in cit-HepPh-subgraph: " + str(edge)
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

## Task 1.2.2

# Task 1.2.2.1

if(sub_graph_name=="soc-Epinions1-subgraph"):
	CntV1 = snap.TIntPrV()

	# Get degree distribution pairs (degree, count)
	snap.GetDegCnt(soc_epinions1_subgraph, CntV1)

	print "Number of nodes of degree = 7 in soc-Epinions1-subgraph: " + str(CntV1[6].GetVal2())
if(sub_graph_name=="cit-HepPh-subgraph"):
	CntV2 = snap.TIntPrV()

	# Get degree distribution pairs (degree, count)
	snap.GetDegCnt(cit_heph_subgraph, CntV2)

	print "Number of nodes of degree = 7 in cit-HepPh-subgraph: " + str(CntV2[6].GetVal2())

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

# Task 1.2.2.2

if(sub_graph_name=="soc-Epinions1-subgraph"):
	Mx_degree_id =[] 
	result_degree = snap.TIntV() 
	snap.GetDegSeqV(soc_epinions1_subgraph,result_degree)
	for i in range(0, result_degree.Len()): 
		if(result_degree[i]==CntV1[CntV1.Len()-1].GetVal1()):
			Mx_degree_id.append(i)

	print "Node id(s) with highest degree in soc-Epinions1-subgraph: " + str(Mx_degree_id)
if(sub_graph_name=="cit-HepPh-subgraph"):
	Mx_degree_id =[] 
	result_degree = snap.TIntV() 
	snap.GetDegSeqV(cit_heph_subgraph,result_degree)
	for i in range(0, result_degree.Len()): 
		if(result_degree[i]==CntV2[CntV2.Len()-1].GetVal1()):
			Mx_degree_id.append(i)

	print "Node id(s) with highest degree in cit-HepPh-subgraph: " + str(Mx_degree_id)
if(sub_graph_name=="email-Enron-subgraph"):
	Mx_degree_id =[] 
	result_degree = snap.TIntV() 
	snap.GetDegSeqV(email_enron_subgraph,result_degree)
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

# Task 1.2.2.3
if(sub_graph_name=="soc-Epinions1-subgraph"):

	# Plotting the degree distribution

	snap.PlotOutDegDistr(soc_epinions1_subgraph, "soc-Epinions1-subgraph", "Undirected graph degree Distribution")
	print "Degree distribution of soc-Epinions1-subgraph: " + "outDeg.soc-Epinions1-subgraph.png"
if(sub_graph_name=="cit-HepPh-subgraph"):

	# Plotting the degree distribution
	
	snap.PlotOutDegDistr(cit_heph_subgraph, "cit-HepPh-subgraph", "Undirected graph degree Distribution")
	print "Degree distribution of cit-HepPh-subgraph: " + "outDeg.cit-HepPh-subgraph.png"
if(sub_graph_name=="email-Enron-subgraph"):

	# Plotting the degree distribution
	
	snap.PlotOutDegDistr(email_enron_subgraph, "email-Enron-subgraph", "Undirected graph degree Distribution")
	print "Degree distribution of email-Enron-subgraph: " + "outDeg.email-Enron-subgraph.png"
if(sub_graph_name=="p2p-Gnutella04-subgraph"):

	# Plotting the degree distribution
	
	snap.PlotOutDegDistr(p2p_gnutella04_subgraph, "p2p-Gnutella04-subgraph", "Undirected graph degree Distribution")
	print "Degree distribution of p2p-Gnutella04-subgraph: " + "outDeg.p2p-Gnutella04-subgraph.png"

## Task 1.2.3

# Task 1.2.3.1
if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Calculating the full diameter 
	print "Approximate full diameter in soc-Epinions1-subgraph with sampling 10 nodes: " + str(snap.GetBfsFullDiam(soc_epinions1_subgraph, 10))
	print "Approximate full diameter in soc-Epinions1-subgraph with sampling 100 nodes: " + str(snap.GetBfsFullDiam(soc_epinions1_subgraph, 100))
	print "Approximate full diameter in soc-Epinions1-subgraph with sampling 1000 nodes: " + str(snap.GetBfsFullDiam(soc_epinions1_subgraph, 1000))

	value = [snap.GetBfsFullDiam(soc_epinions1_subgraph, 10),snap.GetBfsFullDiam(soc_epinions1_subgraph, 100),snap.GetBfsFullDiam(soc_epinions1_subgraph, 1000)]

	print "Approximate full diameter in soc-Epinions1-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value),2)) + "," + str(round(statistics.variance(value),2))
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Calculating the full diameter 
	print "Approximate full diameter in cit-HepPh-subgraph with sampling 10 nodes: " + str(snap.GetBfsFullDiam(cit_heph_subgraph, 10))
	print "Approximate full diameter in cit-HepPh-subgraph with sampling 100 nodes: " + str(snap.GetBfsFullDiam(cit_heph_subgraph, 100))
	print "Approximate full diameter in cit-HepPh-subgraph with sampling 1000 nodes: " + str(snap.GetBfsFullDiam(cit_heph_subgraph, 1000))

	value = [snap.GetBfsFullDiam(cit_heph_subgraph, 10),snap.GetBfsFullDiam(cit_heph_subgraph, 100),snap.GetBfsFullDiam(cit_heph_subgraph, 1000)]

	print "Approximate full diameter in cit-HepPh-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value),2)) + "," + str(round(statistics.variance(value),2))
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

# Task 1.2.3.2

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Calculating the effective diameter

	print "Approximate Effective diameter in soc-Epinions1-subgraph with sampling 10 nodes: " + str(round(snap.GetBfsEffDiam(soc_epinions1_subgraph,10,v1,True)[0],3))
	print "Approximate Effective diameter in soc-Epinions1-subgraph with sampling 100 nodes: " + str(round(snap.GetBfsEffDiam(soc_epinions1_subgraph,100,v1,True)[0],3))
	print "Approximate Effective diameter in soc-Epinions1-subgraph with sampling 1000 nodes: " + str(round(snap.GetBfsEffDiam(soc_epinions1_subgraph,1000,v1,True)[0],3))

	value_new = [snap.GetBfsEffDiam(soc_epinions1_subgraph,10,v1,True)[0],snap.GetBfsEffDiam(soc_epinions1_subgraph,100,v1,True)[0],snap.GetBfsEffDiam(soc_epinions1_subgraph,1000,v1,True)[0]]

	print "Approximate Effective diameter in soc-Epinions1-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value_new),3)) + "," + str(round(statistics.variance(value_new),4))
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Calculating the effective diameter

	print "Approximate Effective diameter in cit-HepPh-subgraph with sampling 10 nodes: " + str(round(snap.GetBfsEffDiam(cit_heph_subgraph,10,v2,True)[0],3))
	print "Approximate Effective diameter in cit-HepPh-subgraph with sampling 100 nodes: " + str(round(snap.GetBfsEffDiam(cit_heph_subgraph,100,v2,True)[0],3))
	print "Approximate Effective diameter in cit-HepPh-subgraph with sampling 1000 nodes: " + str(round(snap.GetBfsEffDiam(cit_heph_subgraph,1000,v2,True)[0],3))

	value_new = [snap.GetBfsEffDiam(cit_heph_subgraph,10,v2,True)[0],snap.GetBfsEffDiam(cit_heph_subgraph,100,v2,True)[0],snap.GetBfsEffDiam(cit_heph_subgraph,1000,v2,True)[0]]

	print "Approximate Effective diameter in cit-HepPh-subgraph with sampling nodes(mean and variance):" + str(round(statistics.mean(value_new),3)) + "," + str(round(statistics.variance(value_new),4))
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

# Task 1.2.3.3

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Plotting the distribution of shortest Length

	snap.PlotShortPathDistr(soc_epinions1_subgraph,"soc-Epinions1-subgraph","Undirected graph - shortest path")
	print "Shortest path distribution of soc-Epinions1-subgraph is in :" + "diam.soc-Epinions1-subgraph.png"
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Plotting the distribution of shortest Length

	snap.PlotShortPathDistr(cit_heph_subgraph,"cit-HepPh-subgraph","Undirected graph - shortest path")
	print "Shortest path distribution of cit-HepPh-subgraph is in :" + "diam.cit-HepPh-subgraph.png"
if(sub_graph_name=="email-Enron-subgraph"):
	# Plotting the distribution of shortest Length

	snap.PlotShortPathDistr(email_enron_subgraph,"email-Enron-subgraph","Undirected graph - shortest path")
	print "Shortest path distribution of email-Enron-subgraph is in :" + "diam.email-Enron-subgraph.png"
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Plotting the distribution of shortest Length

	snap.PlotShortPathDistr(p2p_gnutella04_subgraph,"p2p-Gnutella04-subgraph","Undirected graph - shortest path")
	print "Shortest path distribution of p2p-Gnutella04-subgraph is in :" + "diam.p2p-Gnutella04-subgraph.png"

## Task 1.2.4

# Task 1.2.4.1

if(sub_graph_name=="soc-Epinions1-subgraph"):

	# Finding the components of the network
	# Calculating the fraction of largest connected component

	largest_connected = snap.GetMxScc(soc_epinions1_subgraph)

	node=0
	for i in largest_connected.Nodes():
		node = node + 1

	print "Fraction of nodes in largest connected component in soc-Epinions1-subgraph :" + str(round(node*1.0/len(v1),3))

if(sub_graph_name=="cit-HepPh-subgraph"):

	# Finding the components of the network
	# Calculating the fraction of largest connected component

	largest_connected = snap.GetMxScc(cit_heph_subgraph)

	node=0
	for i in largest_connected.Nodes():
		node = node + 1

	print "Fraction of nodes in largest connected component in cit-HepPh-subgraph :" + str(round(node*1.0/len(v2),3))
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

# Task 1.2.4.2

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Getting no of edge bridges in th network
	EdgeV = snap.TIntPrV()
	snap.GetEdgeBridges(soc_epinions1_subgraph, EdgeV)

	edge_bridge = 0
	for i in EdgeV:
		edge_bridge = edge_bridge +1
	print "Number of edge bridges in soc-Epinions1-subgraph :" + str(edge_bridge)
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Getting no of edge bridges in th network
	EdgeV = snap.TIntPrV()
	snap.GetEdgeBridges(cit_heph_subgraph, EdgeV)

	edge_bridge = 0
	for i in EdgeV:
		edge_bridge = edge_bridge +1
	print "Number of edge bridges in cit-HepPh-subgraph :" + str(edge_bridge)
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

# Task 1.2.4.3

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Calculating no of Articulation points 

	ArtNIdV = snap.TIntV()
	snap.GetArtPoints(soc_epinions1_subgraph, ArtNIdV)

	art_point=0
	for NI in ArtNIdV:
		art_point = art_point +1
	print "Number of articulation points in soc-Epinions1-subgraph :" + str(art_point)
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Calculating no of Articulation points 

	ArtNIdV = snap.TIntV()
	snap.GetArtPoints(cit_heph_subgraph, ArtNIdV)

	art_point=0
	for NI in ArtNIdV:
		art_point = art_point +1
	print "Number of articulation points in cit-HepPh-subgraph :" + str(art_point)
if(sub_graph_name=="email-Enron-subgraph"):
	# Calculating no of Articulation points 

	ArtNIdV = snap.TIntV()
	snap.GetArtPoints(email_enron_subgraph, ArtNIdV)

	art_point=0
	for NI in ArtNIdV:
		art_point = art_point +1
	print "Number of articulation points in email-Enron-subgraph :" + str(art_point)
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Calculating no of Articulation points 

	ArtNIdV = snap.TIntV()
	snap.GetArtPoints(p2p_gnutella04_subgraph, ArtNIdV)

	art_point=0
	for NI in ArtNIdV:
		art_point = art_point +1
	print "Number of articulation points in p2p-Gnutella04-subgraph :" + str(art_point)

# Task 1.2.4.4

if(sub_graph_name=="soc-Epinions1-subgraph"):
	#Plotting the distribution of sizes of connected components

	snap.PlotSccDistr(soc_epinions1_subgraph,"soc-Epinions1-subgraph","Undirected Scc Distribution")
	print "Component size Distribution of soc-Epinions1-subgraph is in :" + 'scc.soc-Epinions1-subgraph.png'
if(sub_graph_name=="cit-HepPh-subgraph"):
	#Plotting the distribution of sizes of connected components

	snap.PlotSccDistr(cit_heph_subgraph,"cit-HepPh-subgraph","Undirected Scc Distribution")
	print " Component size Distribution of cit-HepPh-subgraph is in :" + 'scc.cit-HepPh-subgraph.png'
if(sub_graph_name=="email-Enron-subgraph"):
	#Plotting the distribution of sizes of connected component
	snap.PlotSccDistr(email_enron_subgraph,"email-Enron-subgraph","Undirected Scc Distribution")
	print "Component size Distribution of email-Enron-subgraph is in :" + 'scc.email-Enron-subgraph.png'
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	#Plotting the distribution of sizes of connected components

	snap.PlotSccDistr(p2p_gnutella04_subgraph,"p2p-Gnutella04-subgraph","Undirected Scc Distribution")
	print "Component size Distribution of p2p-Gnutella04-subgraph is in :" + 'scc.p2p-Gnutella04-subgraph.png'

## Task 1.2.5

# Task 1.2.5.1

if(sub_graph_name=="soc-Epinions1-subgraph"):
	#Compute Average Clustering coeffiecient
	print "Average Clustering coeffiecient in soc-Epinions1-subgraph :" + str(round(snap.GetClustCf(soc_epinions1_subgraph, -1),4))
if(sub_graph_name=="cit-HepPh-subgraph"):
	#Compute Average Clustering coeffiecient
	print "Average Clustering coeffiecient in cit-HepPh-subgraph :" + str(round(snap.GetClustCf (cit_heph_subgraph, -1),4))
if(sub_graph_name=="email-Enron-subgraph"):
	#Compute Average Clustering coeffiecient
	print "Average Clustering coeffiecient in email-Enron-subgraph :" + str(round(snap.GetClustCf (email_enron_subgraph, -1),4))	
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	#Compute Average Clustering coeffiecient
	print "Average Clustering coeffiecient in p2p-Gnutella04-subgraph :" + str(round(snap.GetClustCf (p2p_gnutella04_subgraph, -1),4))

# Task 1.2.5.2

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Computing no of Triads
	print "Number of Triads in soc-Epinions1-subgraph :" + str(snap.GetTriads(soc_epinions1_subgraph,-1))
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Computing no of Triads
	print "Number of Triads in cit-HepPh-subgraph :" + str(snap.GetTriads(cit_heph_subgraph,-1))
if(sub_graph_name=="email-Enron-subgraph"):
	# Computing no of Triads
	print "Number of Triads in email-Enron-subgraph :" + str(snap.GetTriads(email_enron_subgraph,-1))
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Computing no of Triads
	print "Number of Triads in p2p-Gnutella04-subgraph :" + str(snap.GetTriads(p2p_gnutella04_subgraph,-1))

# Task 1.2.5.3

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Clustering coeffiecient of a random node
	Rand = snap.TRnd(42)
	Rand.Randomize()
	RandNode1=soc_epinions1_subgraph.GetRndNId(Rand)
	print "Clustering coefficient of random node " + str(RandNode1) + " in soc-Epinions1-subgraph : " + str(round(snap.GetNodeClustCf(soc_epinions1_subgraph, RandNode1),4))
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Clustering coeffiecient of a random node
	Rand = snap.TRnd(42)
	Rand.Randomize()
	RandNode2=cit_heph_subgraph.GetRndNId(Rand)
	print "Clustering coefficient of random node " + str(RandNode2) + " in cit-HepPh-subgraph : " + str(round(snap.GetNodeClustCf(cit_heph_subgraph, RandNode2),4))
if(sub_graph_name=="email-Enron-subgraph"):
	# Clustering coeffiecient of a random node
	Rand = snap.TRnd(42)
	Rand.Randomize()
	RandNode3=email_enron_subgraph.GetRndNId(Rand)
	print "Clustering coefficient of random node " + str(RandNode3) + " in email-Enron-subgraph : " + str(round(snap.GetNodeClustCf(email_enron_subgraph, RandNode3),4)) 
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Clustering coeffiecient of a random node
	Rand = snap.TRnd(42)
	Rand.Randomize()
	RandNode4=p2p_gnutella04_subgraph.GetRndNId(Rand)
	print "Clustering coefficient of random node " + str(RandNode4) + " in p2p-Gnutella04-subgraph : " + str(round(snap.GetNodeClustCf(p2p_gnutella04_subgraph, RandNode4),4))

# Task 1.2.5.4

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Number of node Triads of a random node
	print "Number of triads of random node  " + str(RandNode1) + "  participates in soc-Epinions1-subgraph: " + str(snap.GetNodeTriads(soc_epinions1_subgraph, RandNode1))
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Number of node Triads of a random node
	print "Number of triads of random node  " + str(RandNode2) + "  participates in cit-HepPh-subgraph: " + str(snap.GetNodeTriads(cit_heph_subgraph, RandNode2))
if(sub_graph_name=="email-Enron-subgraph"):
	# Number of node Triads of a random node
	print "Number of triads of random node  " + str(RandNode3) + "  participates in email-Enron-subgraph: " + str(snap.GetNodeTriads(email_enron_subgraph, RandNode3))
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Number of node Triads of a random node
	print "Number of triads of random node  " + str(RandNode4) + "  participates in p2p-Gnutella04-subgraph: " + str(snap.GetNodeTriads(p2p_gnutella04_subgraph, RandNode4))

# Task 1.2.5.5

if(sub_graph_name=="soc-Epinions1-subgraph"):
	# Calculating no  of edges in particular triads
	print"Number of edges that participate in at least one triad in soc-Epinions1-subgraph : " + str(snap.GetTriadEdges(soc_epinions1_subgraph))
if(sub_graph_name=="cit-HepPh-subgraph"):
	# Calculating no  of edges in particular triads
	print"Number of edges that participate in at least one triad in cit-HepPh-subgraph : " + str(snap.GetTriadEdges(cit_heph_subgraph))
if(sub_graph_name=="email-Enron-subgraph"):
	# Calculating no  of edges in particular triads
	print"Number of edges that participate in at least one triad in email-Enron-subgraph : " + str(snap.GetTriadEdges(email_enron_subgraph))
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	# Calculating no  of edges in particular triads
	print"Number of edges that participate in at least one triad in p2p-Gnutella04-subgraph : " + str(snap.GetTriadEdges(p2p_gnutella04_subgraph))

# Task 1.2.5.6
if(sub_graph_name=="soc-Epinions1-subgraph"):
	#Plotting clustering coefficient 
	snap.PlotClustCf(soc_epinions1_subgraph, "soc-Epinions1-subgraph", "Undirected graph - clustering coefficient")
	print "Clustering coefficient distribution of soc-Epinions1-subgraph is in :" + 'ccf.soc-Epinions1-subgraph.png'
if(sub_graph_name=="cit-HepPh-subgraph"):
	#Plotting clustering coefficient 
	snap.PlotClustCf(cit_heph_subgraph, "cit-Heph-subgraph", "Undirected graph - clustering coefficient")
	print "Clustering coefficient distribution of cit-HepPh-subgraph is in :" + 'ccf.cit-Heph-subgraph.png'
if(sub_graph_name=="email-Enron-subgraph"):
	#Plotting clustering coefficient 
	snap.PlotClustCf(email_enron_subgraph, "email-Enron-subgraph", "Undirected graph - clustering coefficient")
	print "Clustering coefficient distribution of email-Enron-subgraph is in :" + 'ccf.email-Enron-subgraph.png'
if(sub_graph_name=="p2p-Gnutella04-subgraph"):
	#Plotting clustering coefficient 
	snap.PlotClustCf(p2p_gnutella04_subgraph, "p2p-Gnutella04-subgraph", "Undirected graph - clustering coefficient")
	print "Clustering coefficient distribution of p2p-Gnutella04-subgraph is in :" + 'ccf.p2p-Gnutella04-subgraph.png'


#### End Part 1 ############
